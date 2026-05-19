# 🌟 Interactive 3D Tissue Scattering Visualizer

Welcome to the **3D Visualization Module** of the Forward Scattering Anisotropy Factor project. While the main analytical calculator focuses on extracting the $g$-factor from raw goniometric data, this interactive computational tool is designed to bring the complex physics of light-tissue interaction to life.

---

## 🔬 1. Theoretical Background: The Optical Clearing Effect

Biological tissues, such as skin or muscle, are highly turbid media. When a laser beam passes through native tissue, photons undergo severe multiple scattering events primarily due to the refractive index mismatch between structural collagen fibers and the interstitial fluid.

This simulation dynamically models the **Tissue Optical Clearing** process. By applying Optical Clearing Agents (OCAs) like Sorbitol or Glycerol, the refractive index is matched, and the tissue becomes temporally transparent. This tool visualizes the direct consequence of this process on the scattering phase function:

* **Before Tissue (Native State):** Light is highly scattered, forming a wide geometric cone ($g \approx 0.78$).
* **After Tissue (Cleared State):** The scattering cone narrows significantly. Light becomes strongly forward-directed ($g \approx 0.96 - 0.97$), allowing for deeper penetration which is critical for optical diagnostics (e.g., OCT) and laser therapies.

---

## 💻 2. Advanced Software Features

This module is not just a static plot; it is a fully functional, event-driven Graphical User Interface (GUI) built entirely in Python using advanced `matplotlib.widgets` and 3D rendering capabilities.

### 🎛️ Interactive Geometric Manipulation
* **Real-Time Sliders:** Users can dynamically adjust the physical properties of the environment without rewriting code. Modify the tissue block thickness, shift the center of the sample, or change the lengths and base radii of the pre- and post-scattering light cones.
* **Instant Re-rendering:** The 3D multi-planar projection updates instantaneously as parameters are tuned, providing an intuitive understanding of spatial optics.

### 🖱️ Dynamic Annotation Engine
* **Draggable Captions:** The interface includes a custom event-handling engine (`button_press_event`, `motion_notify_event`). You can click and drag the main title across the 3D canvas to perfectly position it for your specific presentation layout.
* **Live Text Editing:** A built-in TextBox allows you to rewrite the plot caption on the fly.
* **Styling Widgets:** Integrated RadioButtons and Sliders let you instantly change the font color and size of the annotations directly from the UI.

### 💾 One-Click Publication Export
* **Clean Capture:** A dedicated `Save` button automatically clones the current 3D perspective and annotations into a clean, UI-free background.
* **High-Resolution Output:** Automatically exports the final frame as a 300 DPI image (`forward_scattering_cones.png`), perfectly tailored for inclusion in academic papers, slide decks, and posters.

---

## 🚀 3. How to Run the Visualizer

Ensure you have a modern Python environment with `matplotlib` and `numpy` installed. To launch the interactive GUI, run the following command in your terminal:

```bash
python 3d_scattering_visualizer.py

Note: The application uses the TkAgg backend to ensure smooth, interactive window rendering across different operating systems.

📚 4. Academic Validation
The geometric models, transition parameters, and theoretical physics visualized in this computational tool are directly derived from and validated by our peer-reviewed laboratory research:

"Modulation of Optical Anisotropy in Soft Tissue Biomaterials Using Optical Clearing Agents: Implications for Structural Characterization and Biomedical Applications." > Progress in Biomaterials (2024).

Authors: Saeed Ziaee, Mohammad Ali Ansari, Mehrdad Kalhori, Kamyab Hassani, Mohammad Hossein Naddaf, Valery V. Tuchin.

DOI: 10.57647/pibm.2024.132412

Crafted by Mehrdad Y. Kalhori, straight out of the Wild West of Lorestan, Iran 🤠
