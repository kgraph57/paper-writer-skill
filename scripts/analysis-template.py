#!/usr/bin/env python3
"""
Statistical Analysis Template for Medical Research

A collection of common statistical analyses used in medical papers.
Run individual analyses or use as a template to customize.

Usage:
    python analysis-template.py --input data.csv --analysis descriptive
    python analysis-template.py --input data.csv --analysis logistic --outcome outcome_col --predictors age sex bmi
    python analysis-template.py --input data.csv --analysis survival --time time_col --event event_col --group group_col

Analyses Available:
    descriptive     Descriptive statistics for all variables
    ttest           Independent t-test / Mann-Whitney U
    chi2            Chi-square / Fisher's exact test
    correlation     Pearson / Spearman correlation matrix
    logistic        Logistic regression (univariate + multivariate)
    linear          Linear regression
    survival        Kaplan-Meier + log-rank test (requires lifelines)

Dependencies:
    Required: numpy, pandas
    Optional: scipy (p-values), statsmodels (logistic regression), lifelines (survival),
              matplotlib (figures)
"""

import argparse
import sys
import os

import numpy as np

try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False

try:
    from scipy import stats
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False

try:
    from statsmodels.formula.api import logit
    HAS_SM = True
except ImportError:
    HAS_SM = False

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    HAS_MPL = True
except ImportError:
    HAS_MPL = False


def dataframe_to_markdown(df, index=True):
    """Render a DataFrame as Markdown without requiring pandas' tabulate extra."""
    try:
        return df.to_markdown(index=index)
    except ImportError:
        pass

    display = df.copy()
    if index:
        index_name = display.index.name or ""
        display.insert(0, index_name, display.index)

    headers = [str(c) for c in display.columns]
    rows = [
        [str(v).replace("\n", "<br>").replace("|", "\\|") for v in row]
        for row in display.itertuples(index=False, name=None)
    ]
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def check_deps(analysis):
    """Check required dependencies for the chosen analysis."""
    if not HAS_PANDAS:
        print("Error: pandas is required. Install: pip install pandas", file=sys.stderr)
        sys.exit(1)
    if analysis == "logistic" and not HAS_SM:
        print("Error: statsmodels is required. Install: pip install statsmodels", file=sys.stderr)
        sys.exit(1)
    if analysis == "survival":
        try:
            import lifelines
        except ImportError:
            print("Error: lifelines is required. Install: pip install lifelines", file=sys.stderr)
            sys.exit(1)


def descriptive(df, output_dir):
    """Generate descriptive statistics."""
    print("\n=== Descriptive Statistics ===\n")

    numeric = df.select_dtypes(include=[np.number])
    categorical = df.select_dtypes(exclude=[np.number])

    if numeric.empty:
        desc = None
        print("No continuous variables detected.")
    else:
        desc = numeric.describe().T
        desc["missing"] = numeric.isnull().sum()
        desc["missing%"] = (numeric.isnull().sum() / len(df) * 100).round(1)
        print(dataframe_to_markdown(desc))

    if not categorical.empty:
        print("\n--- Categorical Variables ---\n")
        for col in categorical.columns:
            counts = df[col].value_counts(dropna=False)
            pcts = (counts / len(df) * 100).round(1)
            summary = pd.DataFrame({"n": counts, "%": pcts})
            print(f"\n{col}:")
            print(dataframe_to_markdown(summary))

    # Save
    path = os.path.join(output_dir, "descriptive_stats.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("# Descriptive Statistics\n\n")
        f.write("## Continuous Variables\n\n")
        if desc is None:
            f.write("No continuous variables detected.")
        else:
            f.write(dataframe_to_markdown(desc))
        f.write("\n\n## Categorical Variables\n\n")
        if categorical.empty:
            f.write("No categorical variables detected.\n")
        else:
            for col in categorical.columns:
                counts = df[col].value_counts(dropna=False)
                pcts = (counts / len(df) * 100).round(1)
                summary = pd.DataFrame({"n": counts, "%": pcts})
                f.write(f"\n### {col}\n\n")
                f.write(dataframe_to_markdown(summary))
                f.write("\n")
    print(f"\nSaved: {path}")


def ttest_analysis(df, outcome, group, output_dir):
    """Independent t-test or Mann-Whitney U test."""
    print(f"\n=== Comparing {outcome} by {group} ===\n")

    groups = df[group].dropna().unique()
    if len(groups) != 2:
        print(f"Error: Need exactly 2 groups, found {len(groups)}: {groups}", file=sys.stderr)
        return

    g1 = df[df[group] == groups[0]][outcome].dropna().values
    g2 = df[df[group] == groups[1]][outcome].dropna().values

    print(f"Group '{groups[0]}': N={len(g1)}, mean={np.mean(g1):.2f}, SD={np.std(g1,ddof=1):.2f}")
    print(f"Group '{groups[1]}': N={len(g2)}, mean={np.mean(g2):.2f}, SD={np.std(g2,ddof=1):.2f}")

    if HAS_SCIPY:
        # Check normality
        normal_1 = stats.shapiro(g1)[1] > 0.05 if len(g1) < 5000 else False
        normal_2 = stats.shapiro(g2)[1] > 0.05 if len(g2) < 5000 else False

        if normal_1 and normal_2:
            stat, p = stats.ttest_ind(g1, g2)
            test_name = "Independent t-test"
        else:
            stat, p = stats.mannwhitneyu(g1, g2, alternative="two-sided")
            test_name = "Mann-Whitney U test"

        print(f"\nTest: {test_name}")
        print(f"Statistic: {stat:.3f}")
        print(f"P-value: {p:.4f}")

    # Box plot
    if HAS_MPL:
        fig, ax = plt.subplots(figsize=(6, 4))
        data = [g1, g2]
        bp = ax.boxplot(data, labels=[str(groups[0]), str(groups[1])], patch_artist=True)
        bp["boxes"][0].set_facecolor("#4393c3")
        bp["boxes"][1].set_facecolor("#d6604d")
        ax.set_ylabel(outcome)
        ax.set_title(f"{outcome} by {group}")
        path = os.path.join(output_dir, f"boxplot_{outcome}_by_{group}.png")
        plt.savefig(path, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Saved: {path}")


def chi2_analysis(df, outcome, group, output_dir):
    """Chi-square or Fisher's exact test for categorical variables."""
    print(f"\n=== Categorical Association: {outcome} by {group} ===\n")

    if outcome not in df.columns:
        print(f"Error: outcome column not found: {outcome}", file=sys.stderr)
        sys.exit(1)
    if group not in df.columns:
        print(f"Error: group column not found: {group}", file=sys.stderr)
        sys.exit(1)

    data = df[[group, outcome]].dropna()
    if data.empty:
        print("Error: no complete rows for chi-square analysis", file=sys.stderr)
        sys.exit(1)

    table = pd.crosstab(data[group], data[outcome])
    print(dataframe_to_markdown(table))

    test_name = "Not computed"
    stat = None
    p = None
    dof = None
    expected = None

    if HAS_SCIPY:
        if table.shape == (2, 2):
            chi2, chi2_p, chi2_dof, chi2_expected = stats.chi2_contingency(table)
            if (chi2_expected < 5).any():
                odds_ratio, p = stats.fisher_exact(table)
                test_name = "Fisher's exact test"
                stat = odds_ratio
            else:
                test_name = "Chi-square test"
                stat, p, dof, expected = chi2, chi2_p, chi2_dof, chi2_expected
        else:
            stat, p, dof, expected = stats.chi2_contingency(table)
            test_name = "Chi-square test"

        print(f"\nTest: {test_name}")
        print(f"Statistic: {stat:.3f}")
        if dof is not None:
            print(f"Degrees of freedom: {dof}")
        print(f"P-value: {p:.4f}")
    else:
        print("\nscipy not installed; contingency table saved without a p-value.")

    path = os.path.join(output_dir, f"chi2_{outcome}_by_{group}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Chi-square Test: {outcome} by {group}\n\n")
        f.write("## Contingency Table\n\n")
        f.write(dataframe_to_markdown(table))
        f.write("\n\n## Test Result\n\n")
        f.write(f"- Test: {test_name}\n")
        if stat is not None:
            f.write(f"- Statistic: {stat:.3f}\n")
        if dof is not None:
            f.write(f"- Degrees of freedom: {dof}\n")
        if p is not None:
            f.write(f"- P-value: {p:.4f}\n")
        else:
            f.write("- P-value: not computed (scipy not installed)\n")
        if expected is not None:
            expected_df = pd.DataFrame(expected, index=table.index, columns=table.columns)
            f.write("\n## Expected Counts\n\n")
            f.write(dataframe_to_markdown(expected_df.round(2)))
            f.write("\n")
    print(f"\nSaved: {path}")


def correlation_analysis(df, output_dir):
    """Generate Pearson and Spearman correlation matrices for numeric variables."""
    print("\n=== Correlation Matrix ===\n")

    numeric = df.select_dtypes(include=[np.number])
    if numeric.shape[1] < 2:
        print("Error: at least two numeric columns are required for correlation", file=sys.stderr)
        sys.exit(1)

    pearson = numeric.corr(method="pearson")
    spearman = numeric.corr(method="spearman")

    print("--- Pearson ---\n")
    print(dataframe_to_markdown(pearson.round(3)))
    print("\n--- Spearman ---\n")
    print(dataframe_to_markdown(spearman.round(3)))

    path = os.path.join(output_dir, "correlation_matrix.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("# Correlation Matrix\n\n")
        f.write("## Pearson\n\n")
        f.write(dataframe_to_markdown(pearson.round(3)))
        f.write("\n\n## Spearman\n\n")
        f.write(dataframe_to_markdown(spearman.round(3)))
        f.write("\n")
    print(f"\nSaved: {path}")


def logistic_analysis(df, outcome, predictors, output_dir):
    """Logistic regression (univariate + multivariate)."""
    print(f"\n=== Logistic Regression: {outcome} ===\n")

    # Univariate
    print("--- Univariate ---\n")
    uni_results = []
    for pred in predictors:
        try:
            formula = f"{outcome} ~ {pred}"
            model = logit(formula, data=df.dropna(subset=[outcome, pred])).fit(disp=0)
            or_val = np.exp(model.params[pred])
            ci = np.exp(model.conf_int().loc[pred])
            p = model.pvalues[pred]
            uni_results.append({
                "Variable": pred,
                "OR": f"{or_val:.2f}",
                "95% CI": f"{ci[0]:.2f}–{ci[1]:.2f}",
                "P": f"{p:.3f}",
            })
            print(f"  {pred}: OR={or_val:.2f} (95% CI: {ci[0]:.2f}–{ci[1]:.2f}), P={p:.3f}")
        except Exception as e:
            print(f"  {pred}: Error — {e}")

    # Multivariate
    print("\n--- Multivariate ---\n")
    try:
        formula = f"{outcome} ~ {' + '.join(predictors)}"
        model = logit(formula, data=df.dropna(subset=[outcome] + predictors)).fit(disp=0)
        print(model.summary2())

        multi_results = []
        for pred in predictors:
            if pred in model.params.index:
                or_val = np.exp(model.params[pred])
                ci = np.exp(model.conf_int().loc[pred])
                p = model.pvalues[pred]
                multi_results.append({
                    "Variable": pred,
                    "aOR": f"{or_val:.2f}",
                    "95% CI": f"{ci[0]:.2f}–{ci[1]:.2f}",
                    "P": f"{p:.3f}",
                })
    except Exception as e:
        print(f"Multivariate model failed: {e}")
        multi_results = []

    # Save
    path = os.path.join(output_dir, f"logistic_{outcome}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Logistic Regression: {outcome}\n\n")
        f.write("## Univariate Analysis\n\n")
        if uni_results:
            uni_df = pd.DataFrame(uni_results)
            f.write(dataframe_to_markdown(uni_df, index=False))
        f.write("\n\n## Multivariate Analysis\n\n")
        if multi_results:
            multi_df = pd.DataFrame(multi_results)
            f.write(dataframe_to_markdown(multi_df, index=False))
        f.write("\n")
    print(f"\nSaved: {path}")


def linear_analysis(df, outcome, predictors, output_dir):
    """Linear regression using ordinary least squares."""
    print(f"\n=== Linear Regression: {outcome} ===\n")

    missing = [c for c in [outcome] + predictors if c not in df.columns]
    if missing:
        print(f"Error: column(s) not found: {', '.join(missing)}", file=sys.stderr)
        sys.exit(1)

    data = df[[outcome] + predictors].apply(pd.to_numeric, errors="coerce").dropna()
    if len(data) < len(predictors) + 2:
        print("Error: not enough complete rows for linear regression", file=sys.stderr)
        sys.exit(1)

    y = data[outcome].to_numpy(dtype=float)
    x = data[predictors].to_numpy(dtype=float)
    design = np.column_stack([np.ones(len(data)), x])
    terms = ["Intercept"] + predictors

    coef, _, rank, _ = np.linalg.lstsq(design, y, rcond=None)
    fitted = design @ coef
    residuals = y - fitted
    ss_res = float(np.sum(residuals**2))
    ss_tot = float(np.sum((y - np.mean(y))**2))
    r_squared = 1 - ss_res / ss_tot if ss_tot else 1.0
    df_resid = len(data) - rank

    if df_resid > 0:
        mse = ss_res / df_resid
        cov = mse * np.linalg.pinv(design.T @ design)
        se = np.sqrt(np.diag(cov))
    else:
        se = np.full_like(coef, np.nan, dtype=float)

    with np.errstate(divide="ignore", invalid="ignore"):
        t_values = coef / se

    if HAS_SCIPY and df_resid > 0:
        p_values = 2 * stats.t.sf(np.abs(t_values), df_resid)
    else:
        p_values = np.full_like(coef, np.nan, dtype=float)

    results = pd.DataFrame({
        "Variable": terms,
        "Estimate": coef,
        "Std. Error": se,
        "t": t_values,
        "P": p_values,
    })
    display = results.copy()
    for col in ("Estimate", "Std. Error", "t", "P"):
        display[col] = display[col].map(lambda v: "—" if pd.isna(v) else f"{v:.4f}")

    print(dataframe_to_markdown(display, index=False))
    print(f"\nN: {len(data)}")
    print(f"R-squared: {r_squared:.4f}")
    print(f"Residual df: {df_resid}")

    path = os.path.join(output_dir, f"linear_{outcome}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Linear Regression: {outcome}\n\n")
        f.write("## Model\n\n")
        f.write(f"- Outcome: `{outcome}`\n")
        f.write(f"- Predictors: {', '.join(f'`{p}`' for p in predictors)}\n")
        f.write(f"- N: {len(data)}\n")
        f.write(f"- R-squared: {r_squared:.4f}\n")
        f.write(f"- Residual df: {df_resid}\n\n")
        f.write("## Coefficients\n\n")
        f.write(dataframe_to_markdown(display, index=False))
        f.write("\n")
    print(f"\nSaved: {path}")


def survival_analysis(df, time_col, event_col, group_col, output_dir):
    """Kaplan-Meier analysis + log-rank test."""
    from lifelines import KaplanMeierFitter
    from lifelines.statistics import logrank_test

    print(f"\n=== Survival Analysis ===")
    print(f"Time: {time_col}, Event: {event_col}, Group: {group_col}\n")

    kmf = KaplanMeierFitter()
    groups = df[group_col].dropna().unique()

    if HAS_MPL:
        fig, ax = plt.subplots(figsize=(8, 5))

    colors = ["#2166ac", "#b2182b", "#4dac26", "#7b3294"]

    for i, g in enumerate(sorted(groups)):
        mask = df[group_col] == g
        T = df.loc[mask, time_col].dropna()
        E = df.loc[mask, event_col].dropna()
        idx = T.index.intersection(E.index)
        T, E = T[idx], E[idx]

        kmf.fit(T, E, label=str(g))

        median = kmf.median_survival_time_
        print(f"Group '{g}': N={len(T)}, Events={int(E.sum())}, Median survival={median:.1f}")

        if HAS_MPL:
            kmf.plot_survival_function(ax=ax, ci_show=True, color=colors[i % len(colors)])

    # Log-rank test
    if len(groups) == 2:
        mask1 = df[group_col] == sorted(groups)[0]
        mask2 = df[group_col] == sorted(groups)[1]
        result = logrank_test(
            df.loc[mask1, time_col], df.loc[mask2, time_col],
            df.loc[mask1, event_col], df.loc[mask2, event_col],
        )
        print(f"\nLog-rank test: chi2={result.test_statistic:.3f}, P={result.p_value:.4f}")

    if HAS_MPL:
        ax.set_xlabel("Time")
        ax.set_ylabel("Survival Probability")
        ax.set_title("Kaplan-Meier Survival Curves")
        ax.legend(loc="best")
        path = os.path.join(output_dir, "km_curve.png")
        plt.savefig(path, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"\nSaved: {path}")


def main():
    parser = argparse.ArgumentParser(description="Statistical analysis for medical research")
    parser.add_argument("--input", required=True, help="Input CSV file")
    parser.add_argument(
        "--analysis",
        required=True,
        choices=["descriptive", "ttest", "chi2", "correlation", "logistic", "linear", "survival"],
        help="Analysis type",
    )
    parser.add_argument("--outcome", help="Outcome variable")
    parser.add_argument("--predictors", nargs="*", help="Predictor variables")
    parser.add_argument("--group", help="Grouping variable")
    parser.add_argument("--time", help="Time variable (survival)")
    parser.add_argument("--event", help="Event variable (survival)")
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Output directory for results (default: current dir)",
    )

    args = parser.parse_args()
    check_deps(args.analysis)

    if not os.path.exists(args.input):
        print(f"Error: File not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    os.makedirs(args.output_dir, exist_ok=True)
    df = pd.read_csv(args.input)
    print(f"Loaded: {len(df)} rows, {len(df.columns)} columns")

    if args.analysis == "descriptive":
        descriptive(df, args.output_dir)
    elif args.analysis == "ttest":
        if not args.outcome or not args.group:
            print("Error: --outcome and --group required for ttest", file=sys.stderr)
            sys.exit(1)
        ttest_analysis(df, args.outcome, args.group, args.output_dir)
    elif args.analysis == "chi2":
        if not args.outcome or not args.group:
            print("Error: --outcome and --group required for chi2", file=sys.stderr)
            sys.exit(1)
        chi2_analysis(df, args.outcome, args.group, args.output_dir)
    elif args.analysis == "correlation":
        correlation_analysis(df, args.output_dir)
    elif args.analysis == "logistic":
        if not args.outcome or not args.predictors:
            print("Error: --outcome and --predictors required for logistic", file=sys.stderr)
            sys.exit(1)
        logistic_analysis(df, args.outcome, args.predictors, args.output_dir)
    elif args.analysis == "linear":
        if not args.outcome or not args.predictors:
            print("Error: --outcome and --predictors required for linear", file=sys.stderr)
            sys.exit(1)
        linear_analysis(df, args.outcome, args.predictors, args.output_dir)
    elif args.analysis == "survival":
        if not args.time or not args.event or not args.group:
            print("Error: --time, --event, --group required for survival", file=sys.stderr)
            sys.exit(1)
        survival_analysis(df, args.time, args.event, args.group, args.output_dir)
    else:
        print(f"Analysis '{args.analysis}' not yet implemented in this template.")
        print("Customize this script for your specific needs.")


if __name__ == "__main__":
    main()
