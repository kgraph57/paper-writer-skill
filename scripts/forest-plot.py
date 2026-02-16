#!/usr/bin/env python3
"""
Forest Plot Generator for Meta-Analysis

Generates publication-quality forest plots using matplotlib and numpy.
No special meta-analysis packages required.

Usage:
    python forest-plot.py                          # Run with example data
    python forest-plot.py --input data.csv         # Read from CSV file
    python forest-plot.py --input data.csv --output my_forest_plot

CSV format (header required):
    study,effect_size,ci_lower,ci_upper,weight
    Smith 2020,1.25,0.85,1.84,15.3
    Jones 2021,1.52,1.10,2.10,18.7
    ...

Options:
    --input FILE       CSV file with study data (default: uses built-in example)
    --output NAME      Output filename without extension (default: forest_plot)
    --measure NAME     Effect measure label: OR, RR, HR, MD, SMD (default: OR)
    --model TYPE       Model type: random or fixed (default: random)
    --null-line VALUE  Null effect line position (default: 1.0 for ratios, 0.0 for differences)
    --log-scale        Use log scale for x-axis (recommended for OR/RR/HR)
    --title TEXT       Plot title (default: "Forest Plot")
    --dpi INT          Output DPI for PNG (default: 300)

Examples:
    # Odds ratios on log scale
    python forest-plot.py --input studies.csv --measure OR --log-scale

    # Mean differences
    python forest-plot.py --input studies.csv --measure MD --null-line 0

    # Hazard ratios with custom title
    python forest-plot.py --input studies.csv --measure HR --log-scale --title "Overall Survival"
"""

import argparse
import csv
import sys
import os
from typing import NamedTuple

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class StudyData(NamedTuple):
    name: str
    effect_size: float
    ci_lower: float
    ci_upper: float
    weight: float


def load_example_data():
    """Return example study data for demonstration."""
    return [
        StudyData("Smith 2020", 1.25, 0.85, 1.84, 12.3),
        StudyData("Jones 2021", 1.52, 1.10, 2.10, 15.7),
        StudyData("Wang 2021", 0.98, 0.62, 1.55, 10.2),
        StudyData("Garcia 2022", 1.78, 1.22, 2.60, 14.5),
        StudyData("Kim 2022", 1.35, 0.95, 1.92, 13.8),
        StudyData("Patel 2023", 1.15, 0.78, 1.70, 11.9),
        StudyData("Mueller 2023", 1.62, 1.18, 2.22, 16.1),
        StudyData("Tanaka 2024", 1.08, 0.71, 1.64, 5.5),
    ]


def load_csv_data(filepath):
    """Load study data from a CSV file."""
    studies = []
    with open(filepath, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            studies.append(
                StudyData(
                    name=row["study"].strip(),
                    effect_size=float(row["effect_size"]),
                    ci_lower=float(row["ci_lower"]),
                    ci_upper=float(row["ci_upper"]),
                    weight=float(row["weight"]),
                )
            )
    return studies


def calculate_pooled_fixed(studies):
    """
    Calculate fixed-effects pooled estimate using inverse-variance method.
    Assumes effect sizes are on log scale for ratios (OR, RR, HR).
    For simplicity, this uses the provided weights directly.
    """
    total_weight = sum(s.weight for s in studies)
    pooled = sum(s.effect_size * s.weight for s in studies) / total_weight

    # Approximate pooled SE from weights
    pooled_var = 1.0 / total_weight
    pooled_se = np.sqrt(pooled_var)

    # For display purposes, compute CI from the weighted average
    # This is approximate; real meta-analysis should use proper variance
    ci_lower = pooled - 1.96 * pooled_se
    ci_upper = pooled + 1.96 * pooled_se

    return pooled, ci_lower, ci_upper


def calculate_pooled_random(studies):
    """
    Calculate random-effects pooled estimate (DerSimonian-Laird method).
    This is a simplified version using provided weights.
    For a real meta-analysis, use proper software (R metafor, RevMan, etc.).
    """
    n = len(studies)
    if n < 2:
        return calculate_pooled_fixed(studies)

    # Use inverse-variance weights
    weights = np.array([s.weight for s in studies])
    effects = np.array([s.effect_size for s in studies])

    # Fixed-effects pooled estimate
    w_total = np.sum(weights)
    pooled_fixed = np.sum(effects * weights) / w_total

    # Cochran's Q
    q_stat = np.sum(weights * (effects - pooled_fixed) ** 2)

    # DerSimonian-Laird tau-squared
    c = w_total - np.sum(weights**2) / w_total
    tau_sq = max(0, (q_stat - (n - 1)) / c)

    # Random-effects weights
    # Approximate study variances from provided weights
    study_vars = 1.0 / weights
    re_weights = 1.0 / (study_vars + tau_sq)

    re_total = np.sum(re_weights)
    pooled_re = np.sum(effects * re_weights) / re_total
    pooled_se = np.sqrt(1.0 / re_total)

    ci_lower = pooled_re - 1.96 * pooled_se
    ci_upper = pooled_re + 1.96 * pooled_se

    return pooled_re, ci_lower, ci_upper


def create_forest_plot(
    studies,
    pooled_effect,
    pooled_ci_lower,
    pooled_ci_upper,
    measure_label="OR",
    model_label="Random",
    null_value=1.0,
    use_log_scale=False,
    title="Forest Plot",
    output_name="forest_plot",
    dpi=300,
):
    """Generate a publication-quality forest plot."""

    n_studies = len(studies)
    fig_height = max(4, 1.0 + n_studies * 0.55 + 1.5)
    fig, ax = plt.subplots(figsize=(10, fig_height))

    # Normalize weights for marker sizing
    weights = [s.weight for s in studies]
    max_weight = max(weights) if weights else 1
    min_marker = 6
    max_marker = 15

    # Y positions (top to bottom)
    y_positions = list(range(n_studies + 1, 1, -1))  # studies
    y_pooled = 0.5  # pooled estimate at bottom

    # Draw null effect line
    ax.axvline(x=null_value, color="black", linestyle="-", linewidth=0.8, zorder=1)

    # Plot each study
    for i, study in enumerate(studies):
        y = y_positions[i]
        marker_size = min_marker + (study.weight / max_weight) * (max_marker - min_marker)

        # CI line
        ax.plot(
            [study.ci_lower, study.ci_upper],
            [y, y],
            color="black",
            linewidth=1.0,
            zorder=2,
        )

        # Square marker (size proportional to weight)
        ax.plot(
            study.effect_size,
            y,
            marker="s",
            color="#2166ac",
            markersize=marker_size,
            zorder=3,
        )

        # Study label (left side)
        ax.text(
            -0.02,
            y,
            study.name,
            transform=ax.get_yaxis_transform(),
            ha="right",
            va="center",
            fontsize=9,
        )

        # Effect size and CI text (right side)
        ci_text = f"{study.effect_size:.2f} [{study.ci_lower:.2f}, {study.ci_upper:.2f}]"
        ax.text(
            1.02,
            y,
            ci_text,
            transform=ax.get_yaxis_transform(),
            ha="left",
            va="center",
            fontsize=9,
            family="monospace",
        )

        # Weight text (far right)
        ax.text(
            1.22,
            y,
            f"{study.weight:.1f}%",
            transform=ax.get_yaxis_transform(),
            ha="left",
            va="center",
            fontsize=9,
        )

    # Draw pooled estimate diamond
    diamond_height = 0.35
    diamond_x = [pooled_ci_lower, pooled_effect, pooled_ci_upper, pooled_effect]
    diamond_y = [
        y_pooled,
        y_pooled + diamond_height,
        y_pooled,
        y_pooled - diamond_height,
    ]
    diamond = patches.Polygon(
        list(zip(diamond_x, diamond_y)),
        closed=True,
        facecolor="#b2182b",
        edgecolor="black",
        linewidth=1.0,
        zorder=4,
    )
    ax.add_patch(diamond)

    # Pooled estimate label
    ax.text(
        -0.02,
        y_pooled,
        f"Pooled ({model_label}-effects)",
        transform=ax.get_yaxis_transform(),
        ha="right",
        va="center",
        fontsize=9,
        fontweight="bold",
    )

    # Pooled CI text
    pooled_text = f"{pooled_effect:.2f} [{pooled_ci_lower:.2f}, {pooled_ci_upper:.2f}]"
    ax.text(
        1.02,
        y_pooled,
        pooled_text,
        transform=ax.get_yaxis_transform(),
        ha="left",
        va="center",
        fontsize=9,
        fontweight="bold",
        family="monospace",
    )

    # Separator line above pooled estimate
    separator_y = 1.5
    all_effects = [s.effect_size for s in studies] + [pooled_ci_lower, pooled_ci_upper]
    ax.axhline(y=separator_y, color="gray", linestyle="-", linewidth=0.5, zorder=1)

    # Column headers
    header_y = n_studies + 2.2
    ax.text(
        -0.02,
        header_y,
        "Study",
        transform=ax.get_yaxis_transform(),
        ha="right",
        va="center",
        fontsize=9,
        fontweight="bold",
    )
    ax.text(
        1.02,
        header_y,
        f"{measure_label} [95% CI]",
        transform=ax.get_yaxis_transform(),
        ha="left",
        va="center",
        fontsize=9,
        fontweight="bold",
    )
    ax.text(
        1.22,
        header_y,
        "Weight",
        transform=ax.get_yaxis_transform(),
        ha="left",
        va="center",
        fontsize=9,
        fontweight="bold",
    )

    # Axis formatting
    if use_log_scale:
        ax.set_xscale("log")
        # Set sensible tick marks for log scale
        ax.set_xticks([0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0])
        ax.get_xaxis().set_major_formatter(plt.ScalarFormatter())

    # Favors labels
    if null_value == 1.0:
        favors_left = f"Favors control"
        favors_right = f"Favors intervention"
    elif null_value == 0.0:
        favors_left = f"Favors control"
        favors_right = f"Favors intervention"
    else:
        favors_left = ""
        favors_right = ""

    ax.text(
        0.35,
        -0.06,
        favors_left,
        transform=ax.transAxes,
        ha="center",
        va="top",
        fontsize=8,
        fontstyle="italic",
    )
    ax.text(
        0.65,
        -0.06,
        favors_right,
        transform=ax.transAxes,
        ha="center",
        va="top",
        fontsize=8,
        fontstyle="italic",
    )

    ax.set_xlabel(f"{measure_label}", fontsize=10)
    ax.set_ylim(-0.5, n_studies + 2.8)
    ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    if title:
        ax.set_title(title, fontsize=12, fontweight="bold", pad=15)

    plt.tight_layout()
    plt.subplots_adjust(left=0.25, right=0.72, top=0.92, bottom=0.12)

    # Save outputs
    png_path = f"{output_name}.png"
    svg_path = f"{output_name}.svg"
    plt.savefig(png_path, dpi=dpi, bbox_inches="tight", facecolor="white")
    plt.savefig(svg_path, bbox_inches="tight", facecolor="white")
    plt.close()

    return png_path, svg_path


def main():
    parser = argparse.ArgumentParser(
        description="Generate a forest plot for meta-analysis"
    )
    parser.add_argument("--input", type=str, help="CSV file with study data")
    parser.add_argument(
        "--output",
        type=str,
        default="forest_plot",
        help="Output filename (without extension)",
    )
    parser.add_argument(
        "--measure",
        type=str,
        default="OR",
        choices=["OR", "RR", "HR", "MD", "SMD"],
        help="Effect measure label",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="random",
        choices=["random", "fixed"],
        help="Model type",
    )
    parser.add_argument(
        "--null-line",
        type=float,
        default=None,
        help="Null effect line position (default: 1.0 for ratios, 0.0 for differences)",
    )
    parser.add_argument(
        "--log-scale",
        action="store_true",
        help="Use log scale for x-axis",
    )
    parser.add_argument(
        "--title",
        type=str,
        default="Forest Plot",
        help="Plot title",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=300,
        help="Output DPI for PNG",
    )

    args = parser.parse_args()

    # Load data
    if args.input:
        if not os.path.exists(args.input):
            print(f"Error: File not found: {args.input}", file=sys.stderr)
            sys.exit(1)
        studies = load_csv_data(args.input)
    else:
        print("No input file specified. Using example data for demonstration.")
        studies = load_example_data()

    if not studies:
        print("Error: No studies loaded.", file=sys.stderr)
        sys.exit(1)

    # Determine null value
    if args.null_line is not None:
        null_value = args.null_line
    elif args.measure in ("MD", "SMD"):
        null_value = 0.0
    else:
        null_value = 1.0

    # Calculate pooled estimate
    if args.model == "random":
        pooled, ci_low, ci_high = calculate_pooled_random(studies)
        model_label = "Random"
    else:
        pooled, ci_low, ci_high = calculate_pooled_fixed(studies)
        model_label = "Fixed"

    print(f"Model: {model_label}-effects")
    print(f"Pooled {args.measure}: {pooled:.3f} (95% CI: {ci_low:.3f} to {ci_high:.3f})")
    print(f"Number of studies: {len(studies)}")

    # Generate plot
    png_path, svg_path = create_forest_plot(
        studies=studies,
        pooled_effect=pooled,
        pooled_ci_lower=ci_low,
        pooled_ci_upper=ci_high,
        measure_label=args.measure,
        model_label=model_label,
        null_value=null_value,
        use_log_scale=args.log_scale,
        title=args.title,
        output_name=args.output,
        dpi=args.dpi,
    )

    print(f"Saved: {png_path}")
    print(f"Saved: {svg_path}")


if __name__ == "__main__":
    main()


# =============================================================================
# R VERSION (using metafor package)
# =============================================================================
#
# Save the code below as forest_plot.R and run with:
#   Rscript forest_plot.R
#
# Requires: install.packages("metafor")
#
# ---- R CODE START ----
#
# library(metafor)
#
# # Example data: log odds ratios and standard errors
# # For OR/RR/HR, use log-transformed values
# study_data <- data.frame(
#   study = c("Smith 2020", "Jones 2021", "Wang 2021", "Garcia 2022",
#             "Kim 2022", "Patel 2023", "Mueller 2023", "Tanaka 2024"),
#   yi = log(c(1.25, 1.52, 0.98, 1.78, 1.35, 1.15, 1.62, 1.08)),  # log(OR)
#   sei = c(0.20, 0.17, 0.23, 0.19, 0.18, 0.20, 0.16, 0.21)       # SE of log(OR)
# )
#
# # --- Random-effects meta-analysis (DerSimonian-Laird) ---
# res <- rma(yi = yi, sei = sei, data = study_data, method = "DL")
#
# # Print summary
# summary(res)
#
# # --- Forest plot ---
# png("forest_plot_R.png", width = 10, height = 7, units = "in", res = 300)
# forest(res,
#        slab = study_data$study,
#        atransf = exp,           # back-transform to OR scale
#        xlab = "Odds Ratio",
#        header = c("Study", "OR [95% CI]"),
#        refline = 1,             # null effect line at OR = 1
#        cex = 0.9,
#        col = "blue4",
#        border = "blue4",
#        mlab = paste0("RE Model (I\u00B2 = ",
#                      formatC(res$I2, digits = 1, format = "f"), "%, ",
#                      "p = ", formatC(res$QEp, digits = 3, format = "f"), ")"))
# dev.off()
# cat("Saved: forest_plot_R.png\n")
#
# # --- SVG version ---
# svg("forest_plot_R.svg", width = 10, height = 7)
# forest(res,
#        slab = study_data$study,
#        atransf = exp,
#        xlab = "Odds Ratio",
#        header = c("Study", "OR [95% CI]"),
#        refline = 1,
#        cex = 0.9,
#        col = "blue4",
#        border = "blue4",
#        mlab = paste0("RE Model (I\u00B2 = ",
#                      formatC(res$I2, digits = 1, format = "f"), "%, ",
#                      "p = ", formatC(res$QEp, digits = 3, format = "f"), ")"))
# dev.off()
# cat("Saved: forest_plot_R.svg\n")
#
# # --- Funnel plot for publication bias ---
# png("funnel_plot_R.png", width = 7, height = 6, units = "in", res = 300)
# funnel(res, main = "Funnel Plot", xlab = "Log Odds Ratio")
# dev.off()
# cat("Saved: funnel_plot_R.png\n")
#
# # --- Egger's regression test ---
# regtest(res, model = "lm")
#
# # --- Leave-one-out sensitivity analysis ---
# loo <- leave1out(res)
# print(loo)
#
# # --- Subgroup analysis example ---
# # study_data$subgroup <- c("RCT","RCT","Obs","RCT","Obs","RCT","Obs","RCT")
# # res_sub <- rma(yi = yi, sei = sei, data = study_data, method = "DL",
# #                mods = ~ subgroup)
# # summary(res_sub)
#
# # ---- R CODE END ----
