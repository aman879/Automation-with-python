import cv2
import os

images = os.listdir('images')
for image in images:
    gray = cv2.imread(f'images/{image}', 0)
    cv2.imwrite(f'grayImages/gray-{image}', gray)