import cv2
from cvzone.HandTrackingModule import HandDetector
import math
import time
import serial

# 🔵 ARDUINO CONNECTION
arduino = serial.Serial('COM14', 9600)  # <-- Check COM number
time.sleep(2)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8, maxHands=1)

cv2.namedWindow("Virtual Switches", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Virtual Switches",
                      cv2.WND_PROP_FULLSCREEN,
                      cv2.WINDOW_FULLSCREEN)

# Switch [x, y, w, h, state]
switches = [
    [250, 250, 220, 220, False],
    [550, 250, 220, 220, False],
    [850, 250, 220, 220, False]
]

click_delay = 0.6
last_click_time = 0

def draw_glass_button(img, x, y, w, h, state, text):
    overlay = img.copy()

    if state:
        color = (0, 0, 255)  # 🔴 ON = Red
    else:
        color = (200, 200, 200)  # ⚪ OFF = Light Gray

    cv2.rectangle(overlay, (x, y), (x + w, y + h), color, -1)
    img = cv2.addWeighted(overlay, 0.3, img, 0.7, 0)

    cv2.rectangle(img, (x, y), (x + w, y + h),
                  (255, 255, 255), 3)

    text_size = cv2.getTextSize(text,
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1.2, 3)[0]
    text_x = x + (w - text_size[0]) // 2
    text_y = y + (h + text_size[1]) // 2

    cv2.putText(img, text, (text_x, text_y),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.2, (255, 255, 255), 3)

    return img

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img)

    if hands:
        lmList = hands[0]['lmList']

        x1, y1 = lmList[4][:2]   # Thumb
        x2, y2 = lmList[8][:2]   # Index

        distance = math.hypot(x2 - x1, y2 - y1)

        for i, sw in enumerate(switches):
            x, y, w, h, state = sw

            if x < x2 < x + w and y < y2 < y + h:
                if distance < 35 and (time.time() - last_click_time > click_delay):
                    sw[4] = not sw[4]
                    last_click_time = time.time()

                    # 🔵 SEND SIGNAL TO ARDUINO
                    arduino.write(str(i + 1).encode())

    # Draw switches
    for i, sw in enumerate(switches):
        x, y, w, h, state = sw
        img = draw_glass_button(img, x, y, w, h, state, f"Switch {i+1}")

    cv2.imshow("Virtual Switches", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
