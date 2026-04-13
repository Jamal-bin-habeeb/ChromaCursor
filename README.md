# ChromaCursor

> Control your cursor with color - no mouse required.
>
> ![Python](https://img.shields.io/badge/Python-3.x-blue) ![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green) ![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-latest-orange)
>
> **ChromaCursor** is a webcam-based virtual mouse that lets you control your computer cursor using colored objects. Blue moves the cursor, yellow left-clicks/drags, and red right-clicks - all in real-time using OpenCV and PyAutoGUI. No physical mouse needed!
>
> ---
>
> ## Color Controls
>
> | Color | Action |
> |-------|--------|
> | Blue | Move cursor |
> | Yellow | Tap = left click / Hold = drag |
> | Red | Right click |
>
> ## Features
> - Real-time HSV color detection via webcam
> - - Exponential smoothing for stable cursor movement
>   - - Morphological noise filtering for clean tracking
>     - - Drag support with configurable hold threshold
>       - - Click debouncing to prevent accidental double-clicks
>         - - Live preview windows for all color masks
>          
>           - ## Requirements
>           - ```bash
>             pip install opencv-python pyautogui numpy
>             ```
>
> ## Usage
> ```bash
> git clone https://github.com/Jamal-bin-habeeb/ChromaCursor
> cd ChromaCursor
> python virtualmouse.py
> ```
> Press 'q' to quit the preview window.
>
> ## Configuration
> | Variable | Default | Description |
> |----------|---------|-------------|
> | MIN_AREA | 800 | Min contour area to reduce noise |
> | SMOOTH_ALPHA | 0.35 | Cursor smoothing (0=none, 1=frozen) |
> | DRAG_HOLD_SEC | 0.5s | Hold duration to trigger drag |
> | CLICK_DEBOUNCE | 0.25s | Debounce window between clicks |
>
> ---
> Made with love by Jamal-bin-habeeb - MIT License
> 
