# CFD Analysis of Turbomachinery Flow (Master Thesis)

## Overview
CFD analysis of turbomachinery using URANS simulations and Python post-processing

This repository contains the work developed for my Master’s Thesis in Aerospace Engineering, focused on the numerical analysis of internal flows in turbomachinery using Computational Fluid Dynamics (CFD).

The main objective of the study is to analyze the aerodynamic performance of a turbomachinery stage and evaluate key performance parameters such as pressure ratio, efficiency, and flow behavior under different operating conditions.

---

## Objectives
- Perform CFD simulations of turbomachinery flow
- Analyze velocity, pressure, and Mach number distributions
- Evaluate global performance parameters (efficiency, pressure ratio, work coefficient)
- Investigate flow structures and losses

---

## Numerical Setup
- **Solver:** ANSYS Fluent
- **Approach:** URANS (Unsteady Reynolds-Averaged Navier-Stokes)
- **Turbulence model:** k-ω standard | k-epsilon con enhanced wall treatment | Spallart Almaras
- **Mesh:** Structured | Coarse () | Medium () | Fine ()
- **Boundary conditions:** Total pressure inlet / Static pressure outlet

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

## Repository Structure
