import contextlib
import csv
import importlib.util
import io
import os
import re
import stat
import subprocess
import sys
import tempfile
import unittest
from types import SimpleNamespace
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


def run_cmd(args, **kwargs):
    env = os.environ.copy()
    env.setdefault("PYTHONIOENCODING", "utf-8")
    return subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        capture_output=True,
        env=env,
        **kwargs,
    )


_MODULE_CACHE = {}


def load_script_module(script_name):
    if script_name not in _MODULE_CACHE:
        path = SCRIPTS / script_name
        module_name = script_name.replace("-", "_").replace(".py", "")
        spec = importlib.util.spec_from_file_location(module_name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        _MODULE_CACHE[script_name] = module
    return _MODULE_CACHE[script_name]


def run_analysis_template(args):
    module = load_script_module("analysis-template.py")
    stdout = io.StringIO()
    stderr = io.StringIO()
    old_argv = sys.argv[:]
    sys.argv = ["analysis-template.py"] + args
    try:
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            try:
                module.main()
                code = 0
            except SystemExit as exc:
                code = exc.code if isinstance(exc.code, int) else 1
    finally:
        sys.argv = old_argv
    return SimpleNamespace(returncode=code, stdout=stdout.getvalue(), stderr=stderr.getvalue())


class ScriptSmokeTests(unittest.TestCase):
    def test_shebang_scripts_are_executable(self):
        non_executable = []
        for path in sorted(SCRIPTS.iterdir()):
            if not path.is_file():
                continue
            with path.open("rb") as f:
                if f.readline().startswith(b"#!"):
                    mode = path.stat().st_mode
                    if not (mode & stat.S_IXUSR):
                        non_executable.append(str(path.relative_to(ROOT)))
        self.assertEqual(non_executable, [])

    def test_word_count_help_exits_successfully(self):
        result = run_cmd([str(SCRIPTS / "word-count.sh"), "--help"])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("USAGE:", result.stdout)

    def test_forest_plot_help_does_not_require_matplotlib(self):
        result = run_cmd([sys.executable, str(SCRIPTS / "forest-plot.py"), "--help"])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Generate a forest plot", result.stdout)


class ManuscriptUtilityTests(unittest.TestCase):
    def test_analysis_template_descriptive_handles_categorical_only_data(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            csv_path = tmp_path / "categorical.csv"
            out_dir = tmp_path / "analysis"
            rows = [
                {"sex": "Female", "group": "Control"},
                {"sex": "Male", "group": "Treatment"},
                {"sex": "Female", "group": "Treatment"},
            ]
            with csv_path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["sex", "group"])
                writer.writeheader()
                writer.writerows(rows)

            result = run_analysis_template([
                "--input",
                str(csv_path),
                "--analysis",
                "descriptive",
                "--output-dir",
                str(out_dir),
            ])

            self.assertEqual(result.returncode, 0, result.stderr)
            output = (out_dir / "descriptive_stats.md").read_text(encoding="utf-8")
            self.assertIn("## Continuous Variables", output)
            self.assertIn("No continuous variables detected.", output)
            self.assertIn("## Categorical Variables", output)
            self.assertIn("Female", output)

    def test_analysis_template_chi2_writes_contingency_results(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            csv_path = tmp_path / "outcomes.csv"
            out_dir = tmp_path / "analysis"
            rows = [
                {"group": "Control", "response": "No"},
                {"group": "Control", "response": "No"},
                {"group": "Control", "response": "Yes"},
                {"group": "Treatment", "response": "Yes"},
                {"group": "Treatment", "response": "Yes"},
                {"group": "Treatment", "response": "No"},
            ]
            with csv_path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["group", "response"])
                writer.writeheader()
                writer.writerows(rows)

            result = run_analysis_template([
                "--input",
                str(csv_path),
                "--analysis",
                "chi2",
                "--outcome",
                "response",
                "--group",
                "group",
                "--output-dir",
                str(out_dir),
            ])

            self.assertEqual(result.returncode, 0, result.stderr)
            output_path = out_dir / "chi2_response_by_group.md"
            self.assertTrue(output_path.exists(), result.stdout)
            output = output_path.read_text(encoding="utf-8")
            self.assertIn("# Chi-square Test: response by group", output)
            self.assertIn("Treatment", output)
            self.assertIn("Control", output)
            self.assertIn("P-value", output)

    def test_analysis_template_linear_writes_regression_results(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            csv_path = tmp_path / "linear.csv"
            out_dir = tmp_path / "analysis"
            rows = [
                {"outcome": "3", "age": "1", "bmi": "20"},
                {"outcome": "5", "age": "2", "bmi": "21"},
                {"outcome": "7", "age": "3", "bmi": "22"},
                {"outcome": "9", "age": "4", "bmi": "23"},
                {"outcome": "11", "age": "5", "bmi": "24"},
            ]
            with csv_path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["outcome", "age", "bmi"])
                writer.writeheader()
                writer.writerows(rows)

            result = run_analysis_template([
                "--input",
                str(csv_path),
                "--analysis",
                "linear",
                "--outcome",
                "outcome",
                "--predictors",
                "age",
                "bmi",
                "--output-dir",
                str(out_dir),
            ])

            self.assertEqual(result.returncode, 0, result.stderr)
            output_path = out_dir / "linear_outcome.md"
            self.assertTrue(output_path.exists(), result.stdout)
            output = output_path.read_text(encoding="utf-8")
            self.assertIn("# Linear Regression: outcome", output)
            self.assertIn("age", output)
            self.assertIn("bmi", output)
            self.assertIn("R-squared", output)

    def test_analysis_template_correlation_writes_numeric_matrices(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            csv_path = tmp_path / "correlation.csv"
            out_dir = tmp_path / "analysis"
            rows = [
                {"age": "10", "height": "120", "weight": "30", "group": "A"},
                {"age": "11", "height": "125", "weight": "33", "group": "A"},
                {"age": "12", "height": "130", "weight": "36", "group": "B"},
                {"age": "13", "height": "135", "weight": "39", "group": "B"},
            ]
            with csv_path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["age", "height", "weight", "group"])
                writer.writeheader()
                writer.writerows(rows)

            result = run_analysis_template([
                "--input",
                str(csv_path),
                "--analysis",
                "correlation",
                "--output-dir",
                str(out_dir),
            ])

            self.assertEqual(result.returncode, 0, result.stderr)
            output_path = out_dir / "correlation_matrix.md"
            self.assertTrue(output_path.exists(), result.stdout)
            output = output_path.read_text(encoding="utf-8")
            self.assertIn("# Correlation Matrix", output)
            self.assertIn("Pearson", output)
            self.assertIn("Spearman", output)
            self.assertIn("height", output)

    def test_table1_categorical_variables_show_category_levels(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            csv_path = tmp_path / "baseline.csv"
            out_path = tmp_path / "table1.md"
            rows = [
                {"arm": "Control", "race": "Asian", "age": "42"},
                {"arm": "Control", "race": "White", "age": "44"},
                {"arm": "Treatment", "race": "Asian", "age": "45"},
                {"arm": "Treatment", "race": "Black", "age": "47"},
            ]
            with csv_path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["arm", "race", "age"])
                writer.writeheader()
                writer.writerows(rows)

            result = run_cmd([
                sys.executable,
                str(SCRIPTS / "table1.py"),
                "--input",
                str(csv_path),
                "--group",
                "arm",
                "--output",
                str(out_path),
            ])

            self.assertEqual(result.returncode, 0, result.stderr)
            table = out_path.read_text(encoding="utf-8")
            self.assertIn("Asian: 2 (50.0%)", table)
            self.assertIn("Black: 1 (25.0%)", table)
            self.assertIn("White: 1 (25.0%)", table)
            self.assertNotIn("| race | 0 (0.0%)", table)

    def test_compile_manuscript_reads_standard_sections_subdirectory(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            sections = project / "sections"
            sections.mkdir()
            (sections / "02_methods.md").write_text("# Methods\n\nMethods body.\n", encoding="utf-8")
            (sections / "03_results.md").write_text("# Results\n\nResults body.\n", encoding="utf-8")

            result = run_cmd([str(SCRIPTS / "compile-manuscript.sh"), str(project)])

            self.assertEqual(result.returncode, 0, result.stderr)
            compiled = sorted((project / "compiled").glob("*_manuscript_*.md"))
            self.assertTrue(compiled)
            content = compiled[-1].read_text(encoding="utf-8")
            self.assertIn("Methods body.", content)
            self.assertIn("Results body.", content)

    def test_compile_manuscript_allows_sections_that_only_contain_internal_notes(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            sections = project / "sections"
            sections.mkdir()
            (sections / "02_methods.md").write_text("TODO: fill methods later\n", encoding="utf-8")
            (sections / "03_results.md").write_text("# Results\n\nResults body.\n", encoding="utf-8")

            result = run_cmd([str(SCRIPTS / "compile-manuscript.sh"), str(project)])

            self.assertEqual(result.returncode, 0, result.stderr)
            compiled = sorted((project / "compiled").glob("*_manuscript_*.md"))
            self.assertTrue(compiled)
            content = compiled[-1].read_text(encoding="utf-8")
            self.assertNotIn("TODO:", content)
            self.assertIn("Results body.", content)

    def test_word_count_reads_standard_sections_subdirectory_and_keeps_link_text(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            sections = project / "sections"
            sections.mkdir()
            (sections / "04_introduction.md").write_text(
                "# Introduction\n\nThe [primary outcome](https://example.com) improved today.\n",
                encoding="utf-8",
            )

            result = run_cmd([str(SCRIPTS / "word-count.sh"), str(project)])

            self.assertEqual(result.returncode, 0, result.stderr)
            plain = re.sub(r"\x1b\[[0-9;]*m", "", result.stdout)
            intro_line = next(line for line in plain.splitlines() if "Introduction" in line)
            self.assertRegex(intro_line, r"\s5\s")


if __name__ == "__main__":
    unittest.main()
