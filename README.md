# CFD Investigation of Inlet Distortion Effects on a Compressor Blade Row

## Project Overview

This work investigates the aerodynamic impact of inlet total pressure distortion on a compressor blade cascade representative of modern turbomachinery applications.

The study focuses on performance degradation, flow instability, and non-uniform rotor loading under distorted inflow conditions typical of High Bypass Ratio (HBPR) turbofan engines.

<p align="center">
  <img src="axial_velocity_30_100.gif" width="600">
</p>

---

## Objectives

- Quantify erodynamic penalties induced by inlet flow distortion
- Reproduce irealistic total pressure distortion patterns at compressor inlet
- Assess impact on:
  - Total pressure ratio (TPR)
  - Isentropic efficiency
  - Mass flow rate
- Investigate unsteady flow mechanisms linked to distortion propagation
- Develop a reduced-cost CFD strategy suitable for early design phase analysis

---

## Numerical Methodology

### Solver and Numerical Framework
- ANSYS Fluent (density-based solver)
- Fully compressible formulation

### Turbulence Modelling
- k-ω standard
- k-ε with enhanced wall treatment 
- Spalart–Allmaras 

### Mesh Strategy
- Structured topology
- Near-wall resolution: y⁺ < 1
- Grid independence assessment:
  - Coarse: 38,700 cells  
  - Medium: 64,029 cells  
  - Fine: 138,447 cells  

### Boundary Conditions
- Total pressure inlet with imposed distortion sector
- Static pressure outlet

### Inlet Distortion Definition
- Sector amplitudes: 30°, 60°, 90°
- Total pressure deficit levels:
  - 10% (104 kPa)
  - 20% (100 kPa)

---

## Simulation Strategy

To ensure physical consistency and computational efficiency, three levels of fidelity were adopted:

- **Steady RANS (single passage):**
  Turbulence model selection and mesh sensitivity study

- **Steady RANS (full annulus):**
  Baseline reference solution without time dependency

- **URANS (full annulus):**
  Time-resolved simulation capturing:
  - Distortion transport
  - Unsteady rotor loading
  - Flow separation and vortex dynamics

```text
Turbolence model selection
        ↓
Mesh Sensitivity
        ↓
Steady RANS Validation
        ↓
Full-Annulus Setup
        ↓
URANS Simulations on HPC (CINECA)
        ↓
Python Automated Post-Processing
        ↓
Performance Parameters Extraction
```

---

## Post-Processing and Data Analysis

Post-processing was carried out using Paraview and custom Python automation scripts developed for batch processing and quantitative evaluation.

Extracted metrics include:
- Pressure ratio evolution across operating points
- Isentropic efficiency maps
- Mach number distributions
- Time-resolved URANS field analysis
- Distortion propagation tracking

---

## Automated Post-Processing Pipeline

Python scripts were developed to automate the extraction and visualization of performance parameters from simulation results datasets.

Main automated tasks:
- Automated generation of characteristic maps
- Total pressure ratio computation
- Efficiency trend comparison
- Multi-case data management
- Circumferential parameter evaluation 
- Time-resolved URANS data analysis
- Python-based workflow automation for multi-case simulations
- HPC data handling and post-processing

Example:

`post_processing/read_speedline_full_anulus_mappa_github.py`

---

## Computational Environment

- High Performance Computing (HPC) on CINECA infrastructure
- Linux-based workflow automation
- Batch simulation management and post-processing scripting
- Parallel execution of multi-case parametric studies

---

## Key Findings

- Inlet distortion leads to a measurable reduction in compressor mass flow rate and overall performance
- Efficiency degradation is dependent on distortion intensity and operating condition
- Significant circumferential non-uniformity in rotor loading is observed
- Unsteady simulations reveal:
  - Localised flow separation
  - Enhanced temporal fluctuations in pressure and velocity fields

---

## Selected Results

### Summary of mass flow rate, TPR, and efficiency for all the considered cases

<p align="center">
  <img src="riepilogo_unsteady_barre_cases.png" width="600">
</p>

- Reduction of the normalized mass flow rate up to 3% for the most severe distortion case.
- Smaller distortion sectors showed a stronger impact compared to wider sectors.
- Although a slight increase in the efficiency was observed in some operating conditions, the overall performace degraded compared to the associated mass flow rate in clean conditions.


### Efficiency Characteristic Map

<p align="center">
  <img src="eta_full_annulus_map.png" width="800">
</p>

- Inlet distortion progressively shifted the operating points toward near-stall conditions as the distorted sector increased.
- A reduction in normalized mass flow rate was observed for all distorted configurations.
- Operating points located below the reference curve highlighted the overall compressor performance degradation caused by the distorted inflow.


### Relative Mach number Distribution - Case 1, Sector 90°

<p align="center">
  <img src="Mach_rel_avg_100_90.png" width="600">
</p>

- Local pressure and velocity peaks developed near the interface between distorted and clean inlet regions.
- The flow progressively recovered downstream of the blade passage within the clean sector.
- Non-uniform flow structures generated circumferential aerodynamic loading variations along the cascade.


### Axial Velocity Evolution - Case 1, Sector 30°

<p align="center">
  <img src="axial_velocity_30_100.gif" width="600">
</p>

- Flow evolution highlighted alternating high- and low-velocity wake structures downstream of the blade row, Von Kármán vortex street.
- Boundary layer thickening and local flow instability contributed to increased aerodynamic losses.

---

## Core Technical Skills Demonstrated

- CFD (RANS / URANS) applied to turbomachinery flows
- Aerodynamic analysis of compressor cascades
- Mesh independence and numerical verification
- Turbulence modelling assessment and selection
- High-fidelity post-processing and data reduction
- HPC computing workflows (CINECA)
- Linux environment and automation scripting (Python-based pipeline)

---

## Tools & Technologies

- ANSYS Fluent
- ANSYS Meshing
- Python Linux
- HPC CINECA
- ParaView
- URANS RANS
- Turbomachinery CFD
- Post-processing automation

---
