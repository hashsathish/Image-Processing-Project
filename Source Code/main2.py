# Importing Required Packages
import cv2
import pygetwindow
import pyautogui
from PIL import Image
import time
import numpy as np
from PIL import ImageEnhance
# import matplotlib.pyplot as plt

path = "F:/snap_dead-main/img/pic.png"

# Getting title of windows open
titles = pygetwindow.getAllTitles()
# print(titles)

x, y = pyautogui.size()
print(f"width={x}\theight={y}")

x2, y2 = pyautogui.size()
x2, y2 = int(str(x2)), int(str(y2))

my = pygetwindow.getWindowsWithTitle('Snap dude')[0]
x3 = x2//2
y3 = y2//2
my.resizeTo(x3, y3)
my.moveTo(0, 0)
time.sleep(3)

# Capturing the selected window
pyautogui.screenshot(path)

im = Image.open(path)
im = im.crop((1, 1, x3, y3))
im.save(path)

img = cv2.imread(path, flags=cv2.IMREAD_COLOR)

# Image Sharpening - Laplacian
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])
image_sharp = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)

# Saving sharpened Image
cv2.imwrite(path, image_sharp)
im2 = Image.open(path)

# Image Enhancement - increasing brightness
curr_b = ImageEnhance.Brightness(im2)
new_b = 1.1
img_b = curr_b.enhance(new_b)
img_b.save(path)

# Display Image
img_b.show()

# Image De-noising
img = cv2.imread(path)
dst = cv2.fastNlMeansDenoisingColored(img, None, 5, 5, 3, 11)

# Show Final image after de-noising
cv2.imshow('final', dst)
cv2.waitKey()



