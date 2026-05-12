"""
URANS Distorted Inflow Study
Post-processing script for compressor characteristic maps.

This script:
- reads steady and unsteady CFD simulation output files
- computes corrected mass flow rate
- evaluates Total Pressure Ratio (TPR) and efficiency
- compares distorted inflow configurations
- generates compressor characteristic maps

Simulation data were processed directly from solver-generated files
within the HPC workflow.

Author: Simone Pompeo
"""

# =============================================================================
# Imports
# =============================================================================

import os
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.lines as mlines

import readData as rd


# =============================================================================
# Plot Configuration
# =============================================================================

FONT_SIZE = 18

plt.style.use("seaborn-v0_8-notebook")

mpl.rcParams["xtick.labelsize"] = FONT_SIZE
mpl.rcParams["ytick.labelsize"] = FONT_SIZE
mpl.rcParams["axes.labelsize"] = FONT_SIZE
mpl.rcParams["legend.fontsize"] = FONT_SIZE * 0.9

plt.rcParams["figure.figsize"] = [10, 6.5]


# =============================================================================
# Reference Parameters
# =============================================================================

OMEGA = -1511.9          # [rad/s]
R_TIP = 0.202            # [m]
U_REF = R_TIP * OMEGA


# =============================================================================
# Paths
# =============================================================================

BASE_DIR = Path("data")

STEADY_DIR = BASE_DIR / "steady"
UNSTEADY_DIR = BASE_DIR / "unsteady"

OUTPUT_DIR = Path("generated_figures")
OUTPUT_DIR.mkdir(exist_ok=True)


# =============================================================================
# Simulation Cases
# =============================================================================

steady_cases = ["RESULTS"]

steady_outlet_pressure = np.array(
    [100, 101, 102, 103, 104, 105, 106, 107]
) * 1e3


unsteady_cases = [
    "100/cascade_med_30",
    "100/cascade_med_60",
    "100/cascade_med_90",
    "104/cascade_med_30",
    "104/cascade_med_60",
    "104/cascade_med_90",
]

unsteady_outlet_pressure = np.array([103]) * 1e3


# =============================================================================
# Plot Styling
# =============================================================================

steady_markers = ["v", "^", ">", "<"]
unsteady_markers = ["<", "d", "P", "<", "d", "P"]

unsteady_labels = [
    "Case 1 - Sector 30°",
    "Case 1 - Sector 60°",
    "Case 1 - Sector 90°",
    "Case 2 - Sector 30°",
    "Case 2 - Sector 60°",
    "Case 2 - Sector 90°",
]


# =============================================================================
# Utility Functions
# =============================================================================

def compute_performance(p0_in, p0_out, T0_in, T0_out):
    """
    Compute Total Pressure Ratio, Total Temperature Ratio and efficiency.
    """

    TTR = np.array(T0_out) / np.array(T0_in)
    TPR = np.array(p0_out) / np.array(p0_in)

    eta = (TPR ** (0.4 / 1.4) - 1.0) / (TTR - 1.0)

    return TPR, TTR, eta


def compute_corrected_massflow(mf_in, mf_out, p0_in, T0_in):
    """
    Compute corrected mass flow rate.
    """

    mflow = 0.5 * (np.abs(mf_in) + np.abs(mf_out))

    correction_factor = np.sqrt(T0_in / 288.15) / (p0_in / 101325)

    return mflow * correction_factor


def read_case_data(base_path, outlet_pressure):
    """
    Read ParaView-exported performance files.
    """

    mf_in = []
    mf_out = []

    p0_in = []
    p0_out = []

    T0_in = []
    T0_out = []

    for pressure in outlet_pressure:

        # Mass flow
        filename = base_path / f"massflow_{pressure:.1f}.frp"
        file_data = rd.readData(filename)

        mf_in.append(float(file_data[0][1]))
        mf_out.append(float(file_data[1][1]))

        # Total pressure
        filename = base_path / f"mflowavg_TotPress_{pressure:.1f}.srp"
        file_data = rd.readData(filename)

        p0_in.append(float(file_data[0][1]))
        p0_out.append(float(file_data[1][1]))

        # Total temperature
        filename = base_path / f"mflowavg_TotTemp_{pressure:.1f}.srp"
        file_data = rd.readData(filename)

        T0_in.append(float(file_data[0][1]))
        T0_out.append(float(file_data[1][1]))

    return (
        np.array(mf_in),
        np.array(mf_out),
        np.array(p0_in),
        np.array(p0_out),
        np.array(T0_in),
        np.array(T0_out),
    )


# =============================================================================
# Steady Data Processing
# =============================================================================

steady_data = {}

for case in steady_cases:

    case_path = STEADY_DIR / case

    (
        mf_in,
        mf_out,
        p0_in,
        p0_out,
        T0_in,
        T0_out,
    ) = read_case_data(case_path, steady_outlet_pressure)

    TPR, TTR, eta = compute_performance(
        p0_in,
        p0_out,
        T0_in,
        T0_out,
    )

    mflow_corr = compute_corrected_massflow(
        mf_in,
        mf_out,
        p0_in,
        T0_in,
    )

    # Reference point at peak efficiency
    mflow_ref = mflow_corr[6]

    mflow_norm = mflow_corr / mflow_ref

    steady_data[case] = {
        "TPR": TPR,
        "TTR": TTR,
        "eta": eta,
        "mflow_norm": mflow_norm,
    }

    print(f"Processed steady case: {case}")


# =============================================================================
# Unsteady Data Processing
# =============================================================================

unsteady_data = {}

for case in unsteady_cases:

    case_path = UNSTEADY_DIR / case

    (
        mf_in,
        mf_out,
        p0_in,
        p0_out,
        T0_in,
        T0_out,
    ) = read_case_data(case_path, unsteady_outlet_pressure)

    TPR, TTR, eta = compute_performance(
        p0_in,
        p0_out,
        T0_in,
        T0_out,
    )

    mflow_corr = compute_corrected_massflow(
        mf_in,
        mf_out,
        p0_in,
        T0_in,
    )

    mflow_norm = mflow_corr / mflow_ref

    unsteady_data[case] = {
        "TPR": TPR,
        "TTR": TTR,
        "eta": eta,
        "mflow_norm": mflow_norm,
    }

    print(f"Processed unsteady case: {case}")


# =============================================================================
# Characteristic Map Plot Function
# =============================================================================

def plot_characteristic_map(y_variable, ylabel, filename):
    """
    Generate compressor characteristic maps.
    """

    fig, ax = plt.subplots(constrained_layout=True)

    # -------------------------------------------------------------------------
    # Steady curve
    # -------------------------------------------------------------------------

    for i, case in enumerate(steady_cases):

        marker = steady_markers[i]

        ax.plot(
            steady_data[case]["mflow_norm"],
            steady_data[case][y_variable],
            linewidth=1.5,
            linestyle="-",
            marker=marker,
            color="b",
            markersize=10,
        )

        # Highlight reference points
        ax.scatter(
            steady_data[case]["mflow_norm"][0],
            steady_data[case][y_variable][0],
            color="g",
            s=120,
            marker="v",
            zorder=5,
        )

        ax.scatter(
            steady_data[case]["mflow_norm"][4],
            steady_data[case][y_variable][4],
            color="r",
            s=120,
            marker="v",
            zorder=5,
        )

    # -------------------------------------------------------------------------
    # Unsteady points
    # -------------------------------------------------------------------------

    for i, case in enumerate(unsteady_cases):

        marker = unsteady_markers[i]

        color = "g" if i < 3 else "r"

        ax.plot(
            unsteady_data[case]["mflow_norm"],
            unsteady_data[case][y_variable],
            linewidth=1.5,
            linestyle="-",
            marker=marker,
            color=color,
            markersize=12,
        )

    # -------------------------------------------------------------------------
    # Legends
    # -------------------------------------------------------------------------

    color_legend = [
        mlines.Line2D(
            [],
            [],
            color="g",
            marker="o",
            linestyle="None",
            label="Case 1",
        ),
        mlines.Line2D(
            [],
            [],
            color="r",
            marker="o",
            linestyle="None",
            label="Case 2",
        ),
    ]

    marker_legend = [
        mlines.Line2D(
            [],
            [],
            color="k",
            marker="<",
            linestyle="None",
            label="30°",
        ),
        mlines.Line2D(
            [],
            [],
            color="k",
            marker="d",
            linestyle="None",
            label="60°",
        ),
        mlines.Line2D(
            [],
            [],
            color="k",
            marker="P",
            linestyle="None",
            label="90°",
        ),
    ]

    legend_1 = ax.legend(
        handles=color_legend,
        title="Pressure Condition",
        loc="lower left",
        fontsize=16,
    )

    ax.add_artist(legend_1)

    legend_2 = ax.legend(
        handles=marker_legend,
        title="Sector Amplitude",
        loc="upper right",
        fontsize=16,
    )

    # -------------------------------------------------------------------------
    # Axes
    # -------------------------------------------------------------------------

    ax.set_xlabel(
        r"$\dot{m}_{corr}~/~\dot{m}_{corr,ref}$",
        fontsize=18,
    )

    ax.set_ylabel(ylabel, fontsize=18)

    ax.tick_params(axis="both", which="major", labelsize=16)

    # -------------------------------------------------------------------------
    # Save Figure
    # -------------------------------------------------------------------------

    plt.savefig(
        OUTPUT_DIR / filename,
        format="pdf",
        bbox_inches="tight",
    )

    print(f"Saved figure: {filename}")


# =============================================================================
# Generate Characteristic Maps
# =============================================================================

plot_characteristic_map(
    y_variable="TPR",
    ylabel=r"$TPR$",
    filename="TPR_full_annulus_map.pdf",
)

plot_characteristic_map(
    y_variable="eta",
    ylabel=r"$\eta$",
    filename="eta_full_annulus_map.pdf",
)

print("\nPost-processing completed successfully.")
