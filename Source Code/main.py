# Importing the required packages
from cv2 import cv2
import cvzone
import numpy as np

cap = cv2.VideoCapture(0)

print(cap)
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Displaying the available filters
print("SNAP-FILTERS\n"
      "1. gl\n"
      "2. star\n"
      "3. sun glass\n"
      "4. specs\n"
      "5. star\n"
      "20. gray_scale\n"
      )

# Getting INPUT of filter
x = int(input())
if x != 20:
    overlay = cv2.imread(f'{x}.png', cv2.IMREAD_UNCHANGED)

# Capturing the face and applying the specific filter
while True:
    _, frame = cap.read()
    print(frame)
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if x == 20:
        cv2.imshow('Snap Dude', gray_scale)
        if cv2.waitKey(10) == ord('q'):
            break
    else:
        faces = cascade.detectMultiScale(gray_scale)
        for (x, y, w, h) in faces:
            # cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 2) Shows rectangle over the face
            overlay_resize = cv2.resize(overlay, (w, h))
            frame = cvzone.overlayPNG(frame, overlay_resize, [x + 4, y - 4])
        cv2.imshow('Snap dude', frame)
        if cv2.waitKey(10) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()

