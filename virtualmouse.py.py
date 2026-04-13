# Virtual Mouse: color-based tracking
# Controls:
#   - BLUE object  : moves the cursor
#   - YELLOW object: tap = left click, hold (>0.5s) = drag
#   - RED object   : right click
#     
# Press 'q' to quit.


import cv2
import numpy as np
import pyautogui
import time

# --- Setup ---
pyautogui.FAILSAFE = False  # disable corner-failsafe so cursor can visit edges

cap = cv2.VideoCapture(0)   # change to 1/2 if you use another camera
if not cap.isOpened():
    raise RuntimeError("Could not open webcam. Check camera permissions/connection.")

screen_w, screen_h = pyautogui.size()

# Minimum contour area to accept (filter noise)
MIN_AREA = 800

# Smoothing factor (0=no smoothing, 1=no movement)
SMOOTH_ALPHA = 0.35
smoothed_x = None
smoothed_y = None

# Drag states
yellow_down_since = None
dragging = False
DRAG_HOLD_SEC = 0.5
last_left_click_time = 0.0
last_right_click_time = 0.0
CLICK_DEBOUNCE = 0.25

# --- HSV color ranges (tune these!) ---
# Blue
LOW_BLUE  = np.array([100, 120,  70])
HIGH_BLUE = np.array([130, 255, 255])

# Yellow
LOW_YEL  = np.array([20, 120, 100])
HIGH_YEL = np.array([35, 255, 255])

# Red is split around the HSV hue wrap (0 and 180)
LOW_RED1, HIGH_RED1 = np.array([0, 120, 80]),  np.array([10, 255, 255])
LOW_RED2, HIGH_RED2 = np.array([170, 120, 80]), np.array([180, 255, 255])

kernel = np.ones((5, 5), np.uint8)

def preprocess(mask):
    # reduce noise and fill small holes
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=1)
    return mask

def find_center(mask, min_area=MIN_AREA):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return None, None
    largest = max(contours, key=cv2.contourArea)
    area = cv2.contourArea(largest)
    if area < min_area:
        return None, None
    M = cv2.moments(largest)
    if M["m00"] == 0:
        return None, None
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])
    return (cx, cy), largest

def map_to_screen(cx, cy, frame_w, frame_h):
    # map camera coordinates → screen coordinates
    mx = int(np.interp(cx, [0, frame_w], [0, screen_w]))
    my = int(np.interp(cy, [0, frame_h], [0, screen_h]))
    return mx, my

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # mirror for natural interaction
    h, w = frame.shape[:2]

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Masks
    blue_mask = preprocess(cv2.inRange(hsv, LOW_BLUE, HIGH_BLUE))
    yellow_mask = preprocess(cv2.inRange(hsv, LOW_YEL, HIGH_YEL))
    red_mask = preprocess(cv2.inRange(hsv, LOW_RED1, HIGH_RED1) |
                          cv2.inRange(hsv, LOW_RED2, HIGH_RED2))

    # --- BLUE: move cursor ---
    blue_center, blue_cnt = find_center(blue_mask)
    if blue_center:
        cx, cy = blue_center

        # optional smoothing (exponential moving average)
        if smoothed_x is None:
            smoothed_x, smoothed_y = cx, cy
        else:
            smoothed_x = int(SMOOTH_ALPHA * smoothed_x + (1 - SMOOTH_ALPHA) * cx)
            smoothed_y = int(SMOOTH_ALPHA * smoothed_y + (1 - SMOOTH_ALPHA) * cy)

        mouse_x, mouse_y = map_to_screen(smoothed_x, smoothed_y, w, h)
        pyautogui.moveTo(mouse_x, mouse_y)

        # draw on preview
        cv2.circle(frame, (cx, cy), 10, (255, 0, 0), -1)      # blue marker
        cv2.drawContours(frame, [blue_cnt], -1, (255, 0, 0), 2)

    # --- YELLOW: left click / drag ---
    yellow_center, yellow_cnt = find_center(yellow_mask)
    now = time.time()

    if yellow_center:
        cv2.circle(frame, yellow_center, 10, (0, 255, 255), -1)
        cv2.drawContours(frame, [yellow_cnt], -1, (0, 255, 255), 2)

        # Start/continue hold timer
        if yellow_down_since is None:
            yellow_down_since = now

        # If held long enough → drag
        if not dragging and (now - yellow_down_since) > DRAG_HOLD_SEC:
            pyautogui.mouseDown()  # start drag
            dragging = True

        # If quick tap and not dragging → left click (debounced)
        if not dragging and (now - yellow_down_since) <= DRAG_HOLD_SEC:
            # only register once per appearance
            if (now - last_left_click_time) > CLICK_DEBOUNCE:
                pyautogui.click()
                last_left_click_time = now
                # prevent multiple clicks while still visible
                yellow_down_since = now + 10  # push timer far ahead until released
    else:
        # released: end drag if active
        if dragging:
            pyautogui.mouseUp()
            dragging = False
        yellow_down_since = None

    # --- RED: right click (rising edge) ---
    red_center, red_cnt = find_center(red_mask)
    if red_center:
        cv2.circle(frame, red_center, 10, (0, 0, 255), -1)
        cv2.drawContours(frame, [red_cnt], -1, (0, 0, 255), 2)
        if (now - last_right_click_time) > CLICK_DEBOUNCE:
            pyautogui.rightClick()
            last_right_click_time = now

    # --- Preview windows ---
    cv2.putText(frame, "Blue=move | Yellow=tap=Left / hold=Drag | Red=Right", (10, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (50, 255, 50), 2, cv2.LINE_AA)

    cv2.imshow("Virtual Mouse (preview)", frame)
    cv2.imshow("Mask - Blue", blue_mask)
    cv2.imshow("Mask - Yellow", yellow_mask)
    cv2.imshow("Mask - Red", red_mask)

    # Quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# --- Cleanup ---
cap.release()
cv2.destroyAllWindows()
