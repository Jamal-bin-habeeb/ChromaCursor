# ChromaCursor

_Control your cursor with color - no mouse required._

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-latest-FF6B6B?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**ChromaCursor** is a real-time, webcam-based virtual mouse that lets you control your computer cursor using **colored objects** - no physical mouse needed. Simply hold a colored object in front of your webcam and let ChromaCursor do the rest.

***

## How It Works

ChromaCursor uses your webcam to detect specific colors in real-time using HSV color space detection via OpenCV. Each color triggers a different mouse action:

| Color | Action |
|-------|--------|
| Blue | Move cursor |
| Yellow | Tap to left-click, Hold to drag |
| Red | Right-click |

The cursor movement is stabilized using exponential smoothing and noise is eliminated using morphological filtering - giving you a smooth, responsive virtual mouse experience.

***

## Features


***

## Requirements

Python 3.8+ and the following packages:

```bash
pip install opencv-python pyautogui numpy
```

***

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/Jamal-bin-habeeb/ChromaCursor
cd ChromaCursor

# 2. Install dependencies
pip install opencv-python pyautogui numpy

# 3. Run ChromaCursor
python virtualmouse.py
```

_Press q to quit the preview window._

***

## Configuration

Fine-tune ChromaCursor's behavior by editing these variables at the top of virtualmouse.py:

| Variable | Default | Description |
|----------|---------|-------------|
| MIN_AREA | 800 | Minimum contour area - increase to reduce noise sensitivity |
| SMOOTH_ALPHA | 0.35 | Cursor smoothing factor (0 = no smoothing, 1 = frozen) |
| DRAG_HOLD_SEC | 0.5 | Seconds to hold yellow before triggering drag mode |
| CLICK_DEBOUNCE | 0.25 | Minimum time (seconds) between consecutive clicks |

***

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core language |
| OpenCV | Webcam capture & color detection |
| PyAutoGUI | Mouse control & simulation |
| NumPy | Array operations & mask processing |

***

## Project Structure

```
ChromaCursor/
|-- virtualmouse.py    # Main script - run this to start ChromaCursor
|-- README.md          # Project documentation
```

***

## Tips for Best Results

<ul>
  <li>Use bright, solid-colored objects (e.g., blue tape, yellow sticky note, red cap)</li>li>
<li>Ensure good, consistent lighting - avoid shadows on the objects</li>li>
<li>Keep the colored object at a distance from your face to avoid skin-tone interference</li>li>
<li>Adjust MIN_AREA if detecting too much background noise</li>li>
</ul>ul>

***

## License

This project is licensed under the MIT License - free to use, modify, and distribute.

***

Made with passion by [Jamal-bin-habeeb](https://github.com/Jamal-bin-habeeb)</li></li><ul>
| Variable | Default | Description |
|----------|---------|-------------|
| MIN_AREA | 800 | Minimum contour area - increase to reduce noise sensitivity |
| SMOOTH_ALPHA | 0.35 | Cursor smoothing factor (0 = no smoothing, 1 = frozen) |
| DRAG_HOLD_SEC | 0.5 | Seconds to hold yellow before triggering drag mode |
| CLICK_DEBOUNCE | 0.25 | Minimum time (seconds) between consecutive clicks |

***

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core language |
| OpenCV | Webcam capture & color detection |
| PyAutoGUI | Mouse control & simulation |
| NumPy | Array operations & mask processing |

***

## Project Structure

```
ChromaCursor/
|-- virtualmouse.py    # Main script - run this to start ChromaCursor
|-- README.md          # Project documentation
```

***

## Tips for Best Results

<ul>
  <li>Use bright, solid-colored objects (e.g., blue tape, yellow sticky note, red cap)</li>li>
  <li>Ensure good, consistent lighting - avoid shadows on the objects</li>li>
  <li>Keep the colored object at a distance from your face to avoid skin-tone interference</li>li>
  <li>Adjust MIN_AREA if detecting too much background noise</li>li>
</ul>ul>


***

## License

This project is licensed under the MIT License - free to use, modify, and distribute.

***

Made with passion by [Jamal-bin-habeeb](https://github.com/Jamal-bin-habeeb)
  <li>Real-time HSV Color Detection - Detects colors from your webcam feed at high speed</li>li>
<li>Exponential Smoothing - Eliminates jitter for stable, fluid cursor movement</li>li>
<li>Morphological Noise Filtering - Cleans up color masks to reduce false positives</li>li>
<li>Drag Support - Hold the yellow object for configurable duration to trigger drag mode</li>li>
<li>Click Debouncing - Prevents accidental double-clicks with a configurable debounce window</li>li>
<li>Live Mask Preview - Shows real-time preview windows for each color mask (Blue, Yellow, Red)</li>li>
<li>Zero Hardware Cost - Works with any standard webcam, no special equipment needed</li>li>
</ul>ul>

***

## Requirements

Python 3.8+ and the following packages:

```bash
pip install opencv-python pyautogui numpy
```

***

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/Jamal-bin-habeeb/ChromaCursor
cd ChromaCursor

# 2. Install dependencies
pip install opencv-python pyautogui numpy

# 3. Run ChromaCursor
python virtualmouse.py
```

_Press q to quit the preview window._

***

## Configuration

Fine-tune ChromaCursor's behavior by editing these variables at the top of virtualmouse.py:

| Variable | Default | Description |
|----------|---------|-------------|
| MIN_AREA | 800 | Minimum contour area - increase to reduce noise sensitivity |
| SMOOTH_ALPHA | 0.35 | Cursor smoothing factor (0 = no smoothing, 1 = frozen) |
| DRAG_HOLD_SEC | 0.5 | Seconds to hold yellow before triggering drag mode |
| CLICK_DEBOUNCE | 0.25 | Minimum time (seconds) between consecutive clicks |

***

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core language |
| OpenCV | Webcam capture & color detection |
| PyAutoGUI | Mouse control & simulation |
| NumPy | Array operations & mask processing |

***

## Project Structure

```
ChromaCursor/
|-- virtualmouse.py    # Main script - run this to start ChromaCursor
|-- README.md          # Project documentation
```

***

## Tips for Best Results

<ul>
  <li>Use bright, solid-colored objects (e.g., blue tape, yellow sticky note, red cap)</li>li>
  <li>Ensure good, consistent lighting - avoid shadows on the objects</li>li>
  <li>Keep the colored object at a distance from your face to avoid skin-tone interference</li>li>
  <li>Adjust MIN_AREA if detecting too much background noise</li>li>
</ul>ul>

***

## License

This project is licensed under the MIT License - free to use, modify, and distribute.

***

Made with passion by [Jamal-bin-habeeb](https://github.com/Jamal-bin-habeeb)
</li></li>
</ul>
