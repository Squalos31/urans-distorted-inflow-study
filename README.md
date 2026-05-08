# CFD Analysis of Turbomachinery Flow (Master Thesis)

## Overview

This project investigates the aerodynamic impact of distorted inflow on a circular section of a compressor blade cascade using CFD simulations.

The study focuses on performance degradation, flow instability, and non-uniform rotor loading under distorted inflow conditions typical of modern turbofan engines.

---

## Objectives
- Analyse the effects of flows non-uniformities on a blade row
- Reproduce inlet distortion using total pressure deficit
- Evaluate impact on efficiency and total pressure ratio (TPR)
- Analyze flow instability and unsteady behavior
- Develop a quasi-2D reduced-cost CFD approach for a preliminary study

---

## Numerical Setup
- **Solver:** Density-based CFD solver with ANSYS Fluent
- **Models:**
  - RANS (steady, single passage) for choice of turbulence model and mesh sensitivity
  - RANS (steady, full annulus) for refernce simulations
  - URANS (unsteady, full annulus) to better capture the introduction of the distortion
- **Turbulence model:** k-ω standard | k-epsilon con enhanced wall treatment | Spalart-Allmaras
- **Mesh:**
  - Structured
  - y+ ≈< 1
  - Coarse (38700 Cells) | Medium (64029 Cells) | Fine (138447 Cells)
- **Boundary conditions:** Total pressure inlet / Static pressure outlet
- **Distortion cases:**
  - Sector: 30°, 60°, 90°
  - Total pressure deficit: 10% for case 2 (104 kPa) and 20% for case 1 (100 kPa)

---
## Results

- Inlet distortion reduces mass flow rate and alters compressor performance
- Efficiency variation strongly depends on operating conditions
- Significant non-uniform rotor loading observed
- Shock waves shift upstream with increased intensity
- High distortion cases show vortex shedding and increased unsteadiness

---

## Post-Processing
Post-processing was performed using:
- ANSYS CFD-Post
- Python scripts for data analysis and visualization

Main outputs:
- Pressure ratio evolution
- Efficiency trends
- Mach number distributions
- Time-averaged flow fields

---

## Key skills

- CFD (RANS / URANS)
- Turbomachinery aerodynamics
- Mesh sensitivity analysis
- Turbulence model selection
- Post-processing and data analysis
- HPC usage (CINECA)
- Linux-based workflow automation


<p align="center">
  <img src="axial_velocity_30_100.gif" width="600">
</p>

