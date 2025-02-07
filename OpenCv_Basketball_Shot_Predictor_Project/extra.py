from typing import Any
import cv2
import numpy as np
import math
from numpy import ndarray, dtype

cap = cv2.VideoCapture("Files/Videos/6.mp4")
posListX = []
posListY = []

XList = [item for item in range(0, 1300)]

def get_contours(mask, original_copy, minarea=700):
    center_points = []
    contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    print("Length of Contours:", len(contours))

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > minarea:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            cx, cy = x + (w // 2), y + (h // 2)

            cv2.circle(original_copy, (cx, cy), 5, (0, 0, 255), cv2.FILLED)
            center_points.append({"area": area, "center": [cx, cy]})

    center_points = sorted(center_points, key=lambda x: x["area"], reverse=True)
    return original_copy, center_points

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_copy = frame.copy()
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Ball Detection
    lower_range = (7, 153, 29)
    upper_range = (162, 255, 255)
    mask = cv2.inRange(frameHSV, lower_range, upper_range)

    frame_copy, center_points = get_contours(mask, frame_copy, minarea=700)

    if center_points:
        posListX.append(center_points[0]["center"][0])
        posListY.append(center_points[0]["center"][1])

    if len(posListX) >= 3:  # Ensure at least 3 points for polynomial fitting
        A, B, C = np.polyfit(posListX, posListY, 2)

        # Draw Ball Trace
        for posX, posY in zip(posListX, posListY):
            cv2.circle(frame_copy, (posX, posY), 8, (0, 255, 0), cv2.FILLED)

        # Draw Predicted Parabola
        for x in XList:
            y = int(A * x ** 2 + B * x + C)
            cv2.circle(frame_copy, (x, y), 2, (0, 0, 0), cv2.FILLED)

        # Check if the ball will enter the basket
        a = A
        b = B
        c = C - 590  # Adjust basket height

        # Quadratic formula: x = (-b ± sqrt(b^2 - 4ac)) / 2a
        discriminant = b ** 2 - (4 * a * c)
        if discriminant >= 0:  # Valid quadratic solution
            x1 = (-b - math.sqrt(discriminant)) / (2 * a)
            x2 = (-b + math.sqrt(discriminant)) / (2 * a)

            # Choose the larger x-value (more realistic for basketball trajectory)
            x_pred = max(x1, x2)
            prediction = 330 < x_pred < 430  # Basket range

            if prediction:
                IN = "BASKET"
            else:
                IN = "NO BASKET"

            # Display Prediction Result
            pos = (50, 150)
            offset = 10
            (w, h), _ = cv2.getTextSize(IN, cv2.FONT_HERSHEY_PLAIN, 3, thickness=3)
            x1, y1, x2, y2 = pos[0] - offset, pos[1] + offset, pos[0] + w + offset, pos[1] - h - offset
            cv2.rectangle(frame_copy, (x1, y1), (x2, y2), (255, 0, 255), -1)
            cv2.putText(frame_copy, IN, (pos[0], pos[1]), cv2.FONT_HERSHEY_PLAIN, 3, [255, 255, 255], thickness=3)

    frame_copy = cv2.resize(frame_copy, (0, 0), None, 0.6, 0.6)
    cv2.imshow("Video", frame_copy)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
