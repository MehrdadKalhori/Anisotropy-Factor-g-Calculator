# Anisotropy-Factor-g-Calculator
A Python GUI tool for calculating the optical anisotropy factor (g) from forward scattering goniometric data.
# Forward Scattering Anisotropy Factor ($g$) Estimation from Goniometric Measurements

A professional Python-based Graphical User Interface (GUI) application designed for biomedical optics, photonics, and tissue characterization research. This tool automates the process of extracting, cleaning, and calculating the optical asymmetry parameter (anisotropy factor, $g$) from experimental angular scattering intensity profiles acquired via goniometric setups.

---

## 1. Theoretical & Physical Background

### 1.1. The Anisotropy Factor ($g$)
In tissue optics and radiative transport theory, the scattering properties of a turbid medium (such as biological tissue) are fundamentally characterized by the **Scattering Phase Function**, $p(\theta)$, which describes the angular probability distribution of a photon after a single scattering event.

The **Anisotropy Factor** ($g$), also known as the asymmetry parameter, is mathematically defined as the expected value (first moment) of the cosine of the scattering angle $\theta$:

$$g = \langle \cos\theta \rangle = \int_{4\pi} p(\theta) \cos\theta \, d\omega$$

Where $d\omega = 2\pi \sin\theta \, d\theta$ is the differential solid angle for an azimuthally symmetric system. 

### 1.2. Physical Interpretation
The value of $g$ boundedly ranges between $-1$ and $+1$:
* **$g \to 1$ (Highly Forward Scattering):** Light is scattered primarily in the forward direction. Biological tissues typically exhibit strong forward scattering ($0.6 \le g \le 0.99$) due to large structural components like mitochondria, nuclei, and collagen fibers relative to the wavelength of light.
* **$g = 0$ (Isotropic Scattering):** Light is scattered equally in all directions (e.g., pure Rayleigh scattering from particles much smaller than the wavelength).
* **$g \to -1$ (Highly Backward Scattering):** Light is predominantly reflected back toward the source.

---

## 2. Mathematical Formulation in the Code

### 2.1. Discrete Numerical Integration
In experimental goniometry, continuous angular distribution functions are represented by discrete measurements of scattering intensity $I(\theta_i)$ at specific angles $\theta_i$. This application evaluates the continuous integral using a discrete, intensity-weighted average formulation:

$$g = \frac{\sum_{i} I(\theta_i) \cos(\theta_i)}{\sum_{i} I(\theta_i)}$$

This approach effectively treats the measured intensity $I(\theta_i)$ as the relative probability weight for each experimental angle.

### 2.2. Dual-Direction Asymmetry Compensation
Real-world experimental setups often introduce minor systemic alignment errors, beam decentration, or localized sample heterogeneities. To provide a robust and scientifically rigorous estimation, the script implements a **Dual-Direction Averaging Logic**:

1. **Positive Profile Calculation ($g_{\text{pos}}$):** Evaluates $g$ strictly for angles $\theta \ge 0^\circ$.
2. **Negative Profile Calculation ($g_{\text{neg}}$):** Evaluates $g$ strictly for angles $\theta \le 0^\circ$.
3. **Compensated Average ($g_{\text{avg}}$):** $$g_{\text{avg}} = \frac{g_{\text{pos}} + g_{\text{neg}}}{2}$$

This mathematical compensation minimizes the influence of zero-angle alignment offsets, a common artifact in goniometric tissue characterization.

---

## 3. Core Software Features

* **Interactive GUI Interface:** Eliminates the need for hardcoded paths. Built using standard `tkinter`, allowing seamless Excel file selection (`.xlsx`, `.xls`).
* **Dynamic Column Mapping:** Automatically parses sheet structures and offers dropdown-style selection boxes to let the user map the precise columns corresponding to $\theta$ and $I(\theta)$.
* **Robust Data Validation:** Implements automated data cleaning pipelines using `pandas` and `numpy`:
  * Eliminates non-finite entries (`NaN`, `inf`).
  * Constraints spatial data to physical boundaries ($-180^\circ \le \theta \le 180^\circ$).
  * Prevents critical mathematical failures (e.g., checks for `ZeroDivisionError` if net intensity sums to zero).
* **Comprehensive Analytical Export:** Automatically writes a detailed breakdown file containing:
  * Calculated $\cos(\theta)$ arrays.
  * Weighted products ($I_{\text{raw}} \cdot \cos\theta$).
  * A dedicated `summary` sheet containing isolated values for $g_{\text{pos}}$, $g_{\text{neg}}$, and $g_{\text{avg}}$.
* **Publication-Grade Visualization:** Generates clean, high-resolution plots ($200$ DPI) mapping $I(\theta)$ against $\theta$, complete with the calculated $g$-factor embedded in the title.

---

## 4. Execution Environments

This script is highly flexible and can be executed across multiple modern development setups:

* **VS Code (Visual Studio Code):** Fully compatible with VS Code. You can execute it as a traditional `.py` script or break it into logical blocks using **Jupyter Notebook interactive cells** (by adding `#%%` markers) within VS Code to visualize data steps dynamically.
* **Jupyter Notebook Environment:** Can be integrated into `.ipynb` notebooks for step-by-step data analysis workflows. *(Note: When running Tkinter GUI elements within Jupyter, ensure your local environment allows interactive pop-up windows).*
* **Standalone Python Script:** Can be run directly from any standard terminal or command prompt.

---
## 📖 Related Publication
The mathematical logic and physical principles behind this calculator were utilized and validated in our recent publication regarding soft tissue biomaterials. If you use this tool in your research, please consider referring to our paper:

**"Modulation of Optical Anisotropy in Soft Tissue Biomaterials Using Optical Clearing Agents: Implications for Structural Characterization and Biomedical Applications."**
*Progress in Biomaterials (2024)*.
* **Focus:** Investigating the optical properties of tissue using clearing agents (e.g., Sorbitol, Glycerol) and their effect on the scattering anisotropy factor at 532 nm.
* **DOI:** [10.57647/pibm.2024.132412](https://doi.org/10.57647/pibm.2024.132412)


## 5. Environment Setup & Installation

To run this application, you must install the required scientific computing and data analysis libraries. You can install all dependencies with a single command using `pip`:

Crafted by Mehrdad Y. Kalhori, straight out of the Wild West of Lorestan, Iran 🤠

```bash
pip install numpy pandas matplotlib openpyxl

python anisotropy_calculator.py
