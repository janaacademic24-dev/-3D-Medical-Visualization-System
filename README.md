# -3D-Medical-Visualization-System
A 3D medical visualization tool showing the nervous, musculoskeletal, dental, and cardiovascular systems using clipping planes, surface rendering, and curved MPR. Includes focus navigation, flying camera, and heart-pumping animation with curved path control.
# 🧠 3D Medical Visualization System

### Multi-System Anatomical Visualization with Advanced Rendering & Navigation

This project provides an **interactive 3D visualization tool** for exploring four major human anatomical systems:
- **Nervous System**
- **Musculoskeletal System**
- **Dental System**
- **Cardiovascular System**

It integrates **three visualization methods** and **dynamic navigation features**, making it an ideal educational and research-oriented platform.

---

## 🌟 Key Features

### 🩺 Anatomical Systems
- **Nervous System** – explore brain structures.  
- **Musculoskeletal System** – visualize bones, muscles, and joints.  
- **Dental System** – view detailed oral and jaw anatomy.  
- **Cardiovascular System** – includes **animated heart pumping** and vessel dynamics.  

---

### 🎨 Visualization Techniques
1. **Clipping Planes** – slice through models to view internal layers.  
2. **Surface Rendering** – realistic anatomical surfaces and textures.  
3. **Curved MPR (Multi-Planar Reconstruction)** – follow curved paths through anatomical volumes with full control.

---

### 🧭 Navigation & Interaction
- **Focus Navigation** – quickly zoom to target organs or systems.  
- **Flying Camera** – smooth cinematic transitions through anatomy.  
- **Curved Path Control** – interactively adjust MPR trajectory.  
- **Heart Animation** – dynamic real-time cardiac cycle simulation.  

---

## ⚙️ Technical Highlights

| Feature | Description |
|----------|-------------|
| **Visualization Engine** | VTK / PyVista |
| **3D Rendering** | Real-time shaders & transparency control |
| **Camera System** | Focus, fly-through & orbit modes |
| **Animation Control** | Heartbeat, camera flight, and curved MPR |
| **UI Controller** | Centralized interface for rendering modes & systems |

### 🖼️ Screenshots  
Showcase different anatomical systems and visualization modes:

| System | Example |
|---------|----------|
| Nervous System | ![Nervous System](https://github.com/user-attachments/assets/c81034a2-86dd-49d1-a29f-ff2b7c57e57b) |
| Musculoskeletal System | ![Musculoskeletal System](https://github.com/user-attachments/assets/a50b7731-0d54-4cd6-a577-a80979070679) |
| Dental System | ![Dental System](https://github.com/user-attachments/assets/e0e0df15-c9e3-4398-9d54-f3be288a075e) |
| Cardiovascular System | ![Cardiovascular System](https://github.com/user-attachments/assets/cbcbd9fd-1e44-4268-b30f-30e684c83d6b) |
| Curved MPR | ![Curved MPR](https://github.com/user-attachments/assets/652e0c03-179a-4ff0-9ddf-d6148df7cbe2) |


## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/medical-visualization.git
cd medical-visualization
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python main.py
```

---

## 📦 Dependencies

### Required Packages
```txt
PyQt5>=5.15.0
vtk>=9.0.0
numpy>=1.19.0
scipy>=1.5.0
matplotlib>=3.3.0
```

### Optional Packages (for enhanced features)
```txt
pydicom>=2.0.0          # For DICOM support
nibabel>=3.2.0          # For NIFTI support
Pillow>=8.0.0           # For image saving
```

Install all dependencies:
```bash
# Core dependencies only
pip install PyQt5 vtk numpy scipy matplotlib

# With optional features
pip install PyQt5 vtk numpy scipy matplotlib pydicom nibabel Pillow
```

---
### Basic Usage (5 Minutes)

1. **Launch Application**
   ```bash
   python main.py
   ```

2. **Select Organ System**
   - Choose from Brain 🧠, Heart ❤️, Teeth 🦷, or Muscle 💪
   - Read feature overview and click Continue

3. **Load Your 3D Models**
   - Click **"📂 Load 3D Models (OBJ)"**
   - Select folder containing `.obj` files
   - Models appear with realistic anatomical colors

4. **Explore with Mouse**
   - **Rotate**: Left drag
   - **Pan**: Middle drag (or Shift + Left)
   - **Zoom**: Scroll wheel

## 🗂️ File Organization

### Preparing Your Models

Organize `.obj` files by organ system:
```
data/
├── brain/
│   ├── cortex.obj
│   ├── cerebellum.obj
│   └── white_matter.obj
├── heart/
│   ├── left_ventricle.obj
│   ├── right_ventricle.obj
│   └── aorta.obj
├── teeth/
│   ├── tooth_01.obj
│   ├── tooth_02.obj
│   └── jaw.obj
└── muscle/
    ├── bicep.obj
    ├── tricep.obj
    └── bone.obj

## 🎓 Educational Usage
This system is ideal for:
- Medical education and training
- Anatomical visualization
- Surgical planning demonstrations
- Research presentations
- Medical imaging workshops

## 👨‍💻 Author
Jana Hazem Mohamed -(mailto:jana.taha06@eng-st.cu.edu.eg)
