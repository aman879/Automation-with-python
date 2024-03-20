import numpy as np
import os
import cv2

col = 3
row = 2

horizontal_margin = 40 
vertical_margin = 20

images = os.listdir('images')
image_object = [cv2.imread(f'images/{filename}') for filename in images]

shape = cv2.imread('images/1.jpeg').shape

big_image = np.zeros((shape[0] * row * horizontal_margin * (row + 1),
    shape[1] * col + vertical_margin * (col + 1),
    shape[2]), np.uint8)

big_image.fill(255)

positions = [(x, y) for x in range(col) for y in range(row)]

for (pos_x, pos_y), image in zip(positions, image_object):
    x = pos_x * (shape[1] + vertical_margin) + vertical_margin
    y = pos_y * (shape[0] + horizontal_margin) + horizontal_margin 
    big_image[y:y+shape[0], x:x+shape[1]] = image

cv2.imwrite('grid.jpeg', big_image)