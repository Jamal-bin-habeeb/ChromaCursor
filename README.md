<div align="center">

# 🖱️ ChromaCursor

### *Control your cursor with color — no mouse required.*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-latest-FF6B6B?style=for-the-badge&logoColor=white)](https://pyautogui.readthedocs.io/)
[![NumPy](https://img.shields.io/badge/NumPy-latest-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)

<br/>

> **ChromaCursor** is a real-time, webcam-based virtual mouse that lets you control your entire computer — cursor movement, left-click, drag, and right-click — using nothing but **colored objects** and your webcam.  
> No physical mouse. No special hardware. Just color.

</div>

---

## 📖 Table of Contents

- [How It Works](#-how-it-works)
- [Features](#-features)
- [Color Controls](#-color-controls)
- [Requirements](#-requirements)
- [Quick Start](#-quick-start)
- [Configuration](#️-configuration)
- [HSV Tuning Guide](#-hsv-tuning-guide)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Tips for Best Results](#-tips-for-best-results)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)

---

## ⚙️ How It Works

ChromaCursor processes your webcam feed frame-by-frame using **OpenCV** in the HSV color space, which is far more robust to lighting variation than RGB. Here's the pipeline:

```
Webcam Frame
     │
     ▼
 Flip (mirror)  ──►  HSV Conversion
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
          Blue Mask    Yellow Mask   Red Mask
              │            │            │
         Morphological Filtering (noise removal)
              │            │            │
         Contour Detection & Area Filtering
              │            │            │
         Centroid Calculation (moments)
              │            │            │
       Move Cursor   Left Click/Drag  Right Click
              │
     Exponential Smoothing
              │
     PyAutoGUI → Screen
```

The cursor coordinates from the camera frame are **linearly interpolated** to match your full screen resolution, and **exponential moving average smoothing** eliminates jitter for a fluid, stable experience.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎨 **HSV Color Detection** | Detects colors in real-time using OpenCV's HSV color space — more reliable than RGB under varying light |
| 🏃 **Real-time Performance** | Processes each webcam frame in milliseconds with no perceptible lag |
| 🖱️ **Full Mouse Emulation** | Move, left-click, right-click, and drag — complete mouse functionality, hands-free |
| 🧲 **Drag Support** | Hold the yellow object for a configurable duration to enter drag mode; release to drop |
| 🔇 **Click Debouncing** | Prevents accidental repeated clicks with a configurable debounce window |
| 🧹 **Morphological Noise Filtering** | Applies opening + dilation to color masks to remove false positives |
| 📐 **Exponential Smoothing** | Eliminates cursor jitter for natural, fluid pointer movement |
| 🪟 **Live Mask Preview** | Shows overlay windows for each color mask (Blue, Yellow, Red) so you can debug detection in real time |
| 🔄 **Mirrored Input** | Frame is flipped horizontally so controls feel natural and intuitive |
| 💰 **Zero Hardware Cost** | Works with any standard USB or built-in webcam |

---

## 🎨 Color Controls

Pick up a colored object and hold it in front of your webcam:

| Color | Object Example | Action |
|:---:|---|---|
| 🔵 **Blue** | Blue tape, blue marker cap, blue cloth | **Move the cursor** |
| 🟡 **Yellow** | Yellow sticky note, highlighter, banana | **Tap** → Left-click · **Hold (>0.5s)** → Drag |
| 🔴 **Red** | Red cap, red object, red sticker | **Right-click** |

> **How tap vs drag works for Yellow:**  
> - **Quick flash** of yellow → single left-click (debounced to prevent doubles)  
> - **Hold yellow** for more than `DRAG_HOLD_SEC` (default: 0.5s) → `mouseDown()` engages, cursor drags  
> - **Remove yellow** from view → `mouseUp()` releases the drag

---

## 📦 Requirements

- **Python 3.8+**
- A working **webcam** (built-in or USB)
- The following Python packages:

```bash
pip install opencv-python pyautogui numpy
```

### Full `requirements.txt`

```
opencv-python>=4.5.0
pyautogui>=0.9.54
numpy>=1.21.0
```

---

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/Jamal-bin-habeeb/ChromaCursor.git
cd ChromaCursor

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install opencv-python pyautogui numpy

# 4. Run ChromaCursor
python virtualmouse.py
```

Four windows will open:
- **Virtual Mouse (preview)** — your webcam feed with detected object overlays
- **Mask - Blue** — binary mask of detected blue regions
- **Mask - Yellow** — binary mask of detected yellow regions
- **Mask - Red** — binary mask of detected red regions

> Press **`q`** in any preview window to quit.

---

## 🛠️ Configuration

All tunable parameters live at the top of `virtualmouse.py`. Edit them to match your environment:

```python
MIN_AREA       = 800    # Minimum contour area (pixels²) — raise to reduce noise
SMOOTH_ALPHA   = 0.35   # Exponential smoothing factor (0 = no smooth, 1 = frozen)
DRAG_HOLD_SEC  = 0.5    # Seconds to hold yellow before drag activates
CLICK_DEBOUNCE = 0.25   # Min seconds between consecutive clicks
```

| Variable | Default | Effect |
|---|---|---|
| `MIN_AREA` | `800` | Increase if small colored patches cause false detections |
| `SMOOTH_ALPHA` | `0.35` | Lower = more responsive but jittery · Higher = smoother but laggy |
| `DRAG_HOLD_SEC` | `0.5` | Lower = faster drag activation · Higher = less accidental drags |
| `CLICK_DEBOUNCE` | `0.25` | Lower = faster repeated clicks · Higher = fewer accidental double-clicks |

---

## 🌈 HSV Tuning Guide

If your colored object isn't being detected reliably, you may need to adjust the HSV color range constants in `virtualmouse.py`.

**HSV ranges used by default:**

| Color | Lower Bound (H, S, V) | Upper Bound (H, S, V) |
|---|---|---|
| Blue | `[100, 120, 70]` | `[130, 255, 255]` |
| Yellow | `[20, 120, 100]` | `[35, 255, 255]` |
| Red (range 1) | `[0, 120, 80]` | `[10, 255, 255]` |
| Red (range 2) | `[170, 120, 80]` | `[180, 255, 255]` |

> **Why two ranges for Red?** Hue wraps around at 180° in OpenCV's HSV — red straddles the 0/180 boundary, so two separate `inRange()` calls are OR'd together.

**Tips for tuning:**
1. Run the script and observe the mask windows.
2. If the mask is **sparse** (missing parts of your object) → widen the S and V bounds downward.
3. If the mask has **too much noise** → narrow the H bounds or increase `MIN_AREA`.
4. Use OpenCV's `cv2.cvtColor` on a screenshot of your object to find its exact HSV value.

---

## 🔬 Tech Stack

| Technology | Version | Role |
|---|---|---|
| [Python](https://python.org) | 3.8+ | Core language |
| [OpenCV](https://opencv.org) | 4.x | Webcam capture, HSV processing, contour detection |
| [PyAutoGUI](https://pyautogui.readthedocs.io) | latest | Cross-platform mouse simulation |
| [NumPy](https://numpy.org) | latest | Array math, mask operations, interpolation |

---

## 📁 Project Structure

```
ChromaCursor/
├── virtualmouse.py     # Main script — run this to start ChromaCursor
└── README.md           # Project documentation
```

**Inside `virtualmouse.py`:**

| Section | Description |
|---|---|
| Setup & Config | Camera init, screen size detection, tunable constants |
| HSV Color Ranges | `LOW_*/HIGH_*` arrays for Blue, Yellow, Red |
| `preprocess(mask)` | Morphological open + dilate to clean color masks |
| `find_center(mask)` | Finds largest contour above `MIN_AREA`, returns centroid |
| `map_to_screen(cx, cy, ...)` | Interpolates camera coords → screen resolution |
| Main loop | Frame capture → masking → control logic → preview rendering |

---

## 💡 Tips for Best Results

- **Use bright, saturated objects** — bold primary/secondary colors work best (e.g., blue tape, yellow sticky note, red cap)
- **Consistent lighting matters** — avoid strong backlighting or shadows falling on your object
- **Keep objects away from your face** — skin tones can overlap with yellow/red HSV ranges
- **Solid colors only** — patterned or multi-colored objects confuse the detector
- **Increase `MIN_AREA`** if background objects keep triggering false detections
- **Adjust `SMOOTH_ALPHA`** to your preference: lower for gaming precision, higher for steady clicking
- **Place webcam at eye level** facing you for the most natural interaction geometry
- **Start with Blue** to get a feel for cursor control before using Yellow and Red

---

## 🔧 Troubleshooting

| Problem | Likely Cause | Fix |
|---|---|---|
| `RuntimeError: Could not open webcam` | Wrong camera index | Change `VideoCapture(0)` to `VideoCapture(1)` or `2` |
| Cursor jumps erratically | `SMOOTH_ALPHA` too low or `MIN_AREA` too small | Increase `SMOOTH_ALPHA` to `0.5`; increase `MIN_AREA` to `1500` |
| Object not detected | HSV range doesn't match your object's color | Widen HSV bounds or retune using a color picker |
| Double-clicking unintentionally | `CLICK_DEBOUNCE` too low | Increase `CLICK_DEBOUNCE` to `0.5` |
| Drag activates too easily | `DRAG_HOLD_SEC` too short | Increase `DRAG_HOLD_SEC` to `0.8` or `1.0` |
| Red detects skin | Skin-tone overlapping red HSV range | Narrow `LOW_RED1`/`HIGH_RED1` S and V limits |
| `ModuleNotFoundError` | Package not installed | Run `pip install opencv-python pyautogui numpy` |

---

## 📄 License

This project is licensed under the **MIT License** — you are free to use, modify, and distribute it for any purpose.

---

<div align="center">

Built with ❤️ by [Jamal-bin-habeeb](https://github.com/Jamal-bin-habeeb)

*If you find ChromaCursor useful, consider giving it a ⭐ on GitHub!*

</div>
