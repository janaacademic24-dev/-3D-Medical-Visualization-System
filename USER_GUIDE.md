# 📚 Medical Visualization System - Complete User Guide

## Table of Contents
1. [Installation](#installation)
2. [Getting Started](#getting-started)
3. [Feature Tutorials](#feature-tutorials)
4. [Advanced Usage](#advanced-usage)
5. [File Formats](#file-formats)
6. [Troubleshooting](#troubleshooting)
7. [Tips & Tricks](#tips--tricks)

---

## Installation

### Step 1: System Requirements
- **OS**: Windows 10/11, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **Python**: 3.8 or higher
- **RAM**: Minimum 4GB, recommended 8GB+
- **Graphics**: OpenGL 3.2 compatible GPU

### Step 2: Download Repository
```bash
# Clone from GitHub
git clone https://github.com/yourusername/medical-visualization.git
cd medical-visualization

# Or download ZIP and extract
```

### Step 3: Install Python Dependencies

#### Option A: Install All Features
```bash
pip install -r requirements.txt
```

#### Option B: Minimal Install (Core Only)
```bash
pip install PyQt5 vtk numpy scipy matplotlib
```

#### Option C: Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 4: Verify Installation
```bash
python -c "import PyQt5; import vtk; print('✓ Installation successful!')"
```

---

## Getting Started

### Launch Application
```bash
python main.py
```

### First Time Setup

1. **Welcome Screen Appears**
   - Shows 4 organ system options
   - Select the system you want to visualize

2. **Feature Overview**
   - Read about available features
   - Click "Continue" when ready

3. **Main Interface Loads**
   - Left panel: Controls
   - Right panel: 3D viewport
   - Bottom: Status bar

---

## Feature Tutorials

### 1️⃣ Loading 3D Models

#### Prepare Your Data
Organize OBJ files in a folder:
```
my_models/
├── part1.obj
├── part2.obj
└── part3.obj
```

#### Load Process
1. Click **"📂 Load 3D Models (OBJ)"**
2. Select folder containing OBJ files
3. Wait for loading (progress shown in status bar)
4. Models appear with realistic colors

**Automatic Coloring:**
The system assigns colors based on filenames:
- Files with "ventricle" → Red tones
- Files with "artery" → Bright red
- Files with "vein" → Blue tones
- Files with "bone" → Beige tones

---

### 2️⃣ Surface Rendering (Basic 3D View)

#### Mouse Controls
| Action | Control |
|--------|---------|
| **Rotate** | Left mouse drag |
| **Pan** | Middle mouse drag (or Shift + Left drag) |
| **Zoom** | Mouse wheel scroll |
| **Reset view** | Press 'R' key |

#### Adjust Visibility
1. Go to **"Parts"** tab
2. Click parts in list to select
3. Use **"Show All"** / **"Hide All"** buttons

#### Adjust Transparency
1. Go to **"Parts"** tab
2. Find "Global Opacity" slider
3. Move slider (0% = transparent, 100% = opaque)

---

### 3️⃣ Multi-Planar Slicing

View your organ in three orthogonal planes simultaneously!

#### Axial Planes (Top View)
1. Go to **"Multi-Planar"** tab
2. Check ☑ **"Enable Axial Clipping"**
3. Adjust **"Number of planes"** (1-10)
4. Move **"Position"** slider to explore

#### Coronal Planes (Front View)
1. Check ☑ **"Enable Coronal Clipping"**
2. Adjust planes and position
3. See frontal cross-sections

#### Sagittal Planes (Side View)
1. Check ☑ **"Enable Sagittal Clipping"**
2. Adjust planes and position
3. See lateral cross-sections

**💡 Pro Tip:** Enable all three simultaneously for comprehensive 3D sectioning!

#### Clear All Planes
Click **"Clear All Planes"** button at bottom of tab

---

### 4️⃣ Focus Navigation

Highlight specific anatomical structures while dimming others.

#### Method 1: Click in 3D View
1. Simply click on any part in 3D viewport
2. That part highlights automatically
3. Other parts dim to 20% opacity

#### Method 2: Select from List
1. Go to **"Parts"** tab
2. Hold `Ctrl` and click multiple parts
3. Click **"Apply Focus to Selected"**
4. Adjust **"Background Opacity"** slider
5. Click **"Clear Focus"** to reset

**Use Cases:**
- Isolate specific anatomical structures
- Create educational presentations
- Focus on areas of interest

---

### 5️⃣ Virtual Endoscopy (Fly-through)

Navigate through anatomical structures like a virtual camera!

#### Define Custom Path
1. Go to **"Navigation"** tab
2. Click **"📍 Start Defining Path"**
3. Click points in 3D view to define route
   - First click: Start point
   - Subsequent clicks: Waypoints
   - Last click: End point
4. Click **"✓ Finish Path"** when done

#### Path Controls
- **↩ Undo**: Remove last point
- **🗑 Clear**: Start over
- Path info shows: Number of points defined

#### Start Endoscopy
1. Ensure you have at least 2 points
2. Adjust **"Speed"** slider (10-100)
3. Click **"▶ Start Virtual Endoscopy"**
4. Camera flies through your defined path!

#### During Animation
- Click **"⏸ Stop"** to end animation
- Camera returns to original position

**💡 Tips:**
- Place points inside hollow structures (vessels, airways)
- More points = smoother path
- Lower speed for detailed viewing

---

### 6️⃣ Standalone Curved MPR Generator

Advanced tool for curved multi-planar reconstruction!

#### Launch Window
1. Go to **"Curved MPR"** tab
2. Click **"🔬 Launch Standalone MPR Window"**
3. New window opens

#### Load Medical Data

**Option A: Load NIFTI File**
1. Click **"📂 Load NIFTI"**
2. Select `.nii` or `.nii.gz` file
3. Data loads, middle slice displays

**Option B: Load DICOM Series**
1. Click **"📂 Load DICOM"**
2. Select folder containing DICOM files
3. Series loads automatically

#### Define Curved Path
1. Navigate slices using **◄ Previous** / **Next ►**
2. Click points on the axial view to define path
3. Points show as green circles
4. Green line connects points

#### Generate CPR
1. Click **"🔄 Generate CPR"** (or press `G`)
2. Wait for processing
3. Curved reformatting appears on right

#### Adjust Window/Level
- **Window Center** slider: Adjust brightness
- **Window Width** slider: Adjust contrast
- Real-time updates

#### Save Result
1. Click **"💾 Save CPR"** (or press `S`)
2. Choose PNG or JPEG format
3. Select save location

#### Keyboard Shortcuts
- `G` = Generate CPR
- `C` = Clear path
- `S` = Save image
- `↑` = Next slice
- `↓` = Previous slice

---

### 7️⃣ Heart Animation (Heart System Only)

Realistic cardiac pumping simulation!

#### Start Animation
1. Load heart model
2. Go to **"Animation"** tab
3. Click **"▶ Start Heart Pump"**
4. Watch realistic contraction/expansion

#### Adjust Speed
- Move **"Pump Speed"** slider
- Range: 20 (slow) to 100 (fast)
- Simulates different heart rates

#### Stop Animation
- Click **"⏸ Stop Heart Pump"**
- Heart returns to normal size

**Technical Details:**
- Simulates systole and diastole
- Ventricles contract more than atria
- Based on sinusoidal function

---

## Advanced Usage

### Combining Multiple Features

#### Example 1: Focused Endoscopy
1. Apply focus to vessel system
2. Define fly-through path inside vessel
3. Start endoscopy while focused

#### Example 2: Animated Slicing
1. Enable multi-planar clipping
2. Start heart pump animation
3. Watch beating heart in cross-section

#### Example 3: Comparative MPR
1. Open standalone MPR window
2. Load first dataset
3. Define and generate CPR
4. Save result
5. Load second dataset
6. Use same path points (note positions)
7. Compare results

---

### Working with Different Organ Systems

#### Brain (Nervous System)
**Best features:**
- Multi-planar slicing to see internal structures
- Focus navigation for specific regions
- Virtual endoscopy through ventricles

**Tips:**
- Use axial slicing to see hemispheres
- Focus on cortex to see surface details
- Define paths through major vessels

#### Heart (Cardiovascular System)
**Best features:**
- Heart pumping animation
- Virtual endoscopy through vessels
- Multi-planar to see chambers

**Tips:**
- Start pump animation first
- Use coronal slicing to see all chambers
- Define path from vena cava to aorta

#### Teeth (Dental System)
**Best features:**
- Focus navigation for individual teeth
- Sagittal slicing for bite analysis
- Surface rendering shows enamel detail

**Tips:**
- Focus on specific teeth for examination
- Use sagittal planes to see roots
- High opacity for clear visualization

#### Muscle (Musculoskeletal System)
**Best features:**
- Multi-planar to see muscle layers
- Focus on specific muscle groups
- Surface rendering shows attachments

**Tips:**
- Use multiple sagittal planes for layers
- Focus on muscle groups alternately
- Adjust opacity to see internal bones

---

## File Formats

### Input Formats

#### OBJ Files (3D Models)
```
Format: Wavefront OBJ
Extension: .obj
Content: Vertices, faces, normals
Usage: Main 3D surface models
```

**Requirements:**
- Text-based format
- Must include vertices (v) and faces (f)
- Normals optional (auto-calculated)

#### NIFTI Files (Volume Data)
```
Format: Neuroimaging Informatics Technology Initiative
Extensions: .nii, .nii.gz
Content: 3D volumetric medical data
Usage: Curved MPR, slicing
```

**Requirements:**
- Requires nibabel package
- Standard medical imaging format
- Includes spatial information

#### DICOM Files (Medical Images)
```
Format: Digital Imaging and Communications in Medicine
Extension: .dcm (various)
Content: Medical image series
Usage: Curved MPR, volume reconstruction
```

**Requirements:**
- Requires pydicom package
- Load entire series (folder)
- Maintains spatial metadata

### Output Formats

#### Images
- **PNG**: Lossless, best quality
- **JPEG**: Compressed, smaller file size

#### Screenshots
- Use system screenshot tool
- Capture 3D viewport
- Save to any format

---

## Troubleshooting

### Common Issues & Solutions

#### Issue: "pydicom not installed"
**Solution:**
```bash
pip install pydicom
```

#### Issue: "nibabel not installed"
**Solution:**
```bash
pip install nibabel
```

#### Issue: VTK rendering window is black
**Solutions:**
1. Update graphics drivers
2. Try software rendering:
   ```bash
   export LIBGL_ALWAYS_SOFTWARE=1  # Linux
   set LIBGL_ALWAYS_SOFTWARE=1      # Windows
   ```
3. Reinstall VTK:
   ```bash
   pip uninstall vtk
   pip install vtk
   ```

#### Issue: Application crashes on startup
**Solutions:**
1. Check Python version: `python --version` (need 3.8+)
2. Reinstall dependencies:
   ```bash
   pip install --force-reinstall -r requirements.txt
   ```
3. Check for conflicting packages

#### Issue: Models load but appear all black
**Solutions:**
1. Check OBJ file format (must be valid)
2. Verify lighting (reset camera with 'R' key)
3. Increase ambient lighting in code

#### Issue: Slow performance
**Solutions:**
1. Reduce number of clipping planes
2. Use smaller model files
3. Close standalone MPR when not needed
4. Reduce model polygon count

#### Issue: Can't click to define path
**Solutions:**
1. Ensure "Start Defining Path" is clicked
2. Button should say "✓ Finish Path"
3. Try clicking directly on model surface

#### Issue: DICOM series loads in wrong order
**Solutions:**
1. Check instance numbers in DICOM files
2. Verify ImagePositionPatient tags
3. Try sorting by slice location

---

## Tips & Tricks

### 🎯 Visualization Tips

1. **Start Simple**
   - Load model first
   - Explore with mouse
   - Then try advanced features

2. **Use Focus Strategically**
   - Highlight target structures
   - Reduce clutter
   - Better screenshots

3. **Combine Features**
   - Multi-planar + Focus = Isolated cross-sections
   - Endoscopy + Animation = Dynamic exploration
   - Clipping + MPR = Detailed analysis

### ⌨️ Keyboard Efficiency

Main Window (3D View):
- `R` - Reset camera
- Left drag - Rotate
- Middle drag - Pan
- Scroll - Zoom

Standalone MPR:
- `G` - Quick generate
- `C` - Quick clear
- `S` - Quick save
- `↑↓` - Navigate slices

### 📊 Best Practices

**For Teaching:**
1. Start with full model
2. Apply focus to area of interest
3. Add clipping planes progressively
4. Use virtual endoscopy for inside view

**For Presentations:**
1. Prepare paths in advance
2. Test animation speeds
3. Save key MPR views
4. Use consistent opacity settings

**For Analysis:**
1. Use multi-planar slicing extensively
2. Generate MPRs from multiple angles
3. Compare focused vs. full views
4. Document settings used

### 🎨 Color Customization

Models are automatically colored by name. To customize:
1. Edit `config/organ_colors.py`
2. Add/modify color mappings
3. Colors are RGB tuples (0.0-1.0)
4. Restart application

Example color override:
```python
ORGAN_COLORS = {
    'heart': {
        'left_ventricle': (1.0, 0.0, 0.0),  # Bright red
        # ... more colors
    }
}
```

### 💾 Saving Your Work

**Screenshots:**
- Use system screenshot tool
- Capture entire window or viewport only
- Best format: PNG for quality

**MPR Images:**
- Use standalone MPR save function
- Choose PNG for analysis
- Choose JPEG for sharing

**Paths:**
- Currently no save feature for paths
- Document point coordinates if needed
- Or take screenshots of path definition

### 🔄 Workflow Examples

**Cardiac Analysis:**
1. Load heart model
2. Enable heart pump
3. Add coronal slicing
4. Focus on left ventricle
5. Capture screenshots at different phases

**Dental Examination:**
1. Load teeth model
2. Focus on specific tooth
3. Add sagittal slicing
4. Adjust transparency
5. Document findings

**Brain Mapping:**
1. Load brain model
2. Use all three clipping planes
3. Focus on specific regions
4. Define endoscopy path through ventricles
5. Generate MPR views

---

## Support & Resources

### Getting Help

1. **Check this guide first**
2. **Read error messages carefully**
3. **Try troubleshooting section**
4. **Open GitHub issue** with:
   - Error message
   - Steps to reproduce
   - System info (OS, Python version)
   - Screenshots if relevant

### Learning Resources

- **VTK Documentation**: https://vtk.org/doc/
- **PyQt5 Tutorial**: https://doc.qt.io/qtforpython/
- **Medical Imaging**: RadiologyKey.com

### Contact

- **GitHub**: [Open an Issue](https://github.com/yourusername/medical-visualization/issues)
- **Email**: your.email@example.com

---

## Appendix

### System Requirements Detailed

**Minimum:**
- CPU: Dual-core 2.0 GHz
- RAM: 4 GB
- GPU: OpenGL 3.2 compatible
- Storage: 500 MB for app + model space

**Recommended:**
- CPU: Quad-core 2.5 GHz+
- RAM: 8 GB+
- GPU: Dedicated with 2GB+ VRAM
- Storage: 5 GB+ (for medical datasets)

### Supported OS Versions

| OS | Minimum Version | Tested |
|----|----------------|--------|
| Windows | 10 (64-bit) | ✓ |
| macOS | 10.14 Mojave | ✓ |
| Ubuntu | 18.04 LTS | ✓ |
| Fedora | 30+ | ✓ |
| Arch Linux | Current | ✓ |

### File Size Limits

- **OBJ Models**: Up to 500 MB each (larger may slow down)
- **NIFTI Files**: Up to 2 GB
- **DICOM Series**: Up to 1000 slices
- **MPR Output**: Depends on defined resolution

---

**Happy Visualizing! 🏥**

If you find this guide helpful, please star the repository and share with others!
