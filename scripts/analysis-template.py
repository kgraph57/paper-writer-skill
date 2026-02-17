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
    Optional: scipy (p-values), statsmodels (regression), lifelines (survival),
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
    import statsmodels.api as sm
    from statsmodels.formula.api import logit, ols
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


def check_deps(analysis):
    """Check required dependencies for the chosen analysis."""
    if not HAS_PANDAS:
        print("Error: pandas is required. Install: pip install pandas", file=sys.stderr)
        sys.exit(1)
    if analysis in ("logistic", "linear") and not HAS_SM:
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

    desc = numeric.describe().T
    desc["missing"] = numeric.isnull().sum()
    desc["missing%"] = (numeric.isnull().sum() / len(df) * 100).round(1)
    print(desc.to_markdown())

    if not categorical.empty:
        print("\n--- Categorical Variables ---\n")
        for col in categorical.columns:
            counts = df[col].value_counts(dropna=False)
            pcts = (counts / len(df) * 100).round(1)
            summary = pd.DataFrame({"n": counts, "%": pcts})
            print(f"\n{col}:")
            print(summary.to_markdown())

    # Save
    path = os.path.join(output_dir, "descriptive_stats.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("# Descriptive Statistics\n\n")
        f.write("## Continuous Variables\n\n")
        f.write(desc.to_markdown())
        f.write("\n\n## Categorical Variables\n\n")
        for col in categorical.columns:
            counts = df[col].value_counts(dropna=False)
            pcts = (counts / len(df) * 100).round(1)
            summary = pd.DataFrame({"n": counts, "%": pcts})
            f.write(f"\n### {col}\n\n")
            f.write(summary.to_markdown())
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
            f.write(uni_df.to_markdown(index=False))
        f.write("\n\n## Multivariate Analysis\n\n")
        if multi_results:
            multi_df = pd.DataFrame(multi_results)
            f.write(multi_df.to_markdown(index=False))
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
        choices=["descriptive", "ttest", "chi2", "logistic", "linear", "survival"],
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
    elif args.analysis == "logistic":
        if not args.outcome or not args.predictors:
            print("Error: --outcome and --predictors required for logistic", file=sys.stderr)
            sys.exit(1)
        logistic_analysis(df, args.outcome, args.predictors, args.output_dir)
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
