#!/usr/bin/env python3
"""
Table 1 Generator — Baseline Characteristics

Generates a publication-ready Table 1 (baseline characteristics) from CSV data.
Automatically detects variable types and applies appropriate statistics.

Usage:
    python table1.py --input data.csv
    python table1.py --input data.csv --group group_col --output table1.md

Output: Markdown table ready for manuscript insertion.

CSV Requirements:
    - First row: column headers (variable names)
    - One row per subject
    - Optional: a grouping column for group comparisons

Variable Detection:
    - Binary (0/1 or Yes/No): n (%)
    - Categorical (2-10 unique values): n (%) per level
    - Continuous (numeric): mean ± SD or median [IQR]
    - Normality tested with Shapiro-Wilk (N<5000) to choose mean vs median
"""

import argparse
import csv
import sys
import os
from collections import Counter

import numpy as np

try:
    from scipy import stats
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False


def load_csv(filepath):
    """Load CSV into list of dicts."""
    rows = []
    with open(filepath, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        for row in reader:
            rows.append(row)
    return headers, rows


def detect_type(values):
    """Detect variable type: binary, categorical, or continuous."""
    clean = [v for v in values if v not in ("", "NA", "NP", "nan", "None", None)]
    if not clean:
        return "empty", clean

    # Try numeric
    numeric = []
    non_numeric = 0
    for v in clean:
        try:
            numeric.append(float(v))
        except (ValueError, TypeError):
            non_numeric += 1

    if non_numeric == 0 and numeric:
        unique = set(numeric)
        if unique <= {0, 1, 0.0, 1.0}:
            return "binary", numeric
        if len(unique) <= 10:
            return "categorical", clean
        return "continuous", numeric

    # Non-numeric
    unique = set(clean)
    if unique <= {"Yes", "No", "yes", "no", "Y", "N", "TRUE", "FALSE", "True", "False"}:
        return "binary", clean
    if len(unique) <= 10:
        return "categorical", clean

    return "text", clean


def is_normal(values, alpha=0.05):
    """Test normality with Shapiro-Wilk."""
    if not HAS_SCIPY:
        return True  # Default to mean±SD if scipy unavailable
    if len(values) < 3:
        return True
    if len(values) > 5000:
        # Shapiro-Wilk unreliable for large N; use visual or default to median
        return False
    try:
        _, p = stats.shapiro(values)
        return p > alpha
    except Exception:
        return True


def format_continuous(values):
    """Format continuous variable as mean±SD or median[IQR]."""
    arr = np.array(values, dtype=float)
    arr = arr[~np.isnan(arr)]
    if len(arr) == 0:
        return "—"

    if is_normal(arr):
        return f"{np.mean(arr):.1f} ± {np.std(arr, ddof=1):.1f}"
    else:
        q25, q50, q75 = np.percentile(arr, [25, 50, 75])
        return f"{q50:.1f} [{q25:.1f}–{q75:.1f}]"


def format_binary(values):
    """Format binary variable as n (%)."""
    total = len(values)
    if not total:
        return "—"

    # Normalize to 1/True/Yes
    positives = sum(
        1
        for v in values
        if str(v).lower() in ("1", "1.0", "yes", "y", "true")
    )
    pct = positives / total * 100
    return f"{positives} ({pct:.1f}%)"


def format_categorical(values):
    """Format categorical variable as n (%) per level."""
    total = len(values)
    if not total:
        return "—"
    counts = Counter(values)
    lines = []
    for level, n in sorted(counts.items()):
        pct = n / total * 100
        lines.append(f"  {level}: {n} ({pct:.1f}%)")
    return "\n".join(lines)


def compute_p_value(var_type, group_values):
    """Compute p-value for between-group comparison."""
    if not HAS_SCIPY or len(group_values) < 2:
        return "—"

    if var_type == "continuous":
        groups = []
        for gv in group_values.values():
            arr = np.array(gv, dtype=float)
            arr = arr[~np.isnan(arr)]
            if len(arr) > 0:
                groups.append(arr)
        if len(groups) < 2:
            return "—"
        if len(groups) == 2:
            # Check normality of both
            if all(is_normal(g) for g in groups):
                _, p = stats.ttest_ind(groups[0], groups[1])
                return f"{p:.3f}"
            else:
                _, p = stats.mannwhitneyu(groups[0], groups[1], alternative="two-sided")
                return f"{p:.3f}"
        else:
            # 3+ groups: Kruskal-Wallis
            _, p = stats.kruskal(*groups)
            return f"{p:.3f}"

    elif var_type in ("binary", "categorical"):
        # Chi-square or Fisher's exact
        labels = sorted(group_values.keys())
        if len(labels) < 2:
            return "—"
        # Build contingency table
        all_categories = set()
        for gv in group_values.values():
            all_categories.update(gv)
        all_categories = sorted(all_categories)

        table = []
        for label in labels:
            counts = Counter(group_values[label])
            row = [counts.get(cat, 0) for cat in all_categories]
            table.append(row)
        table = np.array(table)

        if table.shape[0] == 2 and table.shape[1] == 2:
            # 2x2: Fisher's exact if any cell < 5
            if np.any(table < 5):
                _, p = stats.fisher_exact(table)
                return f"{p:.3f}"
        _, p, _, _ = stats.chi2_contingency(table)
        return f"{p:.3f}"

    return "—"


def generate_table1(headers, rows, group_col=None, exclude_cols=None):
    """Generate Table 1 as Markdown."""
    if exclude_cols is None:
        exclude_cols = set()

    # Determine variables to analyze
    var_cols = [h for h in headers if h != group_col and h not in exclude_cols]

    # Get groups
    if group_col:
        groups = sorted(set(r.get(group_col, "") for r in rows))
        groups = [g for g in groups if g not in ("", "NA")]
    else:
        groups = ["All"]

    # Header row
    if group_col:
        header = f"| Variable | {'All (N=' + str(len(rows)) + ')' } | "
        header += " | ".join(
            f"{g} (N={sum(1 for r in rows if r.get(group_col) == g)})"
            for g in groups
        )
        header += " | P value |"
        sep = "|" + "---|" * (3 + len(groups))
    else:
        header = f"| Variable | All (N={len(rows)}) |"
        sep = "|---|---|"

    lines = [header, sep]

    for col in var_cols:
        all_values = [r.get(col, "") for r in rows]
        var_type, clean_all = detect_type(all_values)

        if var_type == "empty" or var_type == "text":
            continue

        # All column
        if var_type == "continuous":
            all_formatted = format_continuous(clean_all)
        elif var_type == "binary":
            all_formatted = format_binary(clean_all)
        elif var_type == "categorical":
            all_formatted = format_binary(clean_all)  # Simplified for table row
        else:
            continue

        if group_col:
            group_formatted = []
            group_values = {}
            for g in groups:
                gv = [r.get(col, "") for r in rows if r.get(group_col) == g]
                gtype, gclean = detect_type(gv)
                group_values[g] = gclean
                if var_type == "continuous":
                    group_formatted.append(format_continuous(gclean))
                elif var_type == "binary":
                    group_formatted.append(format_binary(gclean))
                else:
                    group_formatted.append(format_binary(gclean))

            p_val = compute_p_value(var_type, group_values)
            row_line = f"| {col} | {all_formatted} | "
            row_line += " | ".join(group_formatted)
            row_line += f" | {p_val} |"
        else:
            row_line = f"| {col} | {all_formatted} |"

        lines.append(row_line)

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate Table 1 from CSV data")
    parser.add_argument("--input", required=True, help="Input CSV file")
    parser.add_argument("--group", default=None, help="Grouping column name")
    parser.add_argument("--output", default="table1.md", help="Output filename")
    parser.add_argument(
        "--exclude",
        nargs="*",
        default=[],
        help="Columns to exclude (e.g., patient_id)",
    )

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: File not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    headers, rows = load_csv(args.input)
    print(f"Loaded {len(rows)} rows, {len(headers)} columns from {args.input}")

    if args.group and args.group not in headers:
        print(f"Error: Group column '{args.group}' not found in CSV", file=sys.stderr)
        print(f"Available columns: {', '.join(headers)}", file=sys.stderr)
        sys.exit(1)

    exclude = set(args.exclude)
    table = generate_table1(headers, rows, group_col=args.group, exclude_cols=exclude)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(f"# Table 1. Baseline Characteristics\n\n")
        if args.group:
            f.write(
                f"Values are mean ± SD, median [IQR], or n (%). "
                f"P values: t-test or Mann-Whitney U for continuous, "
                f"chi-square or Fisher's exact for categorical.\n\n"
            )
        else:
            f.write(f"Values are mean ± SD, median [IQR], or n (%).\n\n")
        f.write(table)
        f.write("\n")

    print(f"Table 1 saved to {args.output}")
    print()
    print(table)


if __name__ == "__main__":
    main()
