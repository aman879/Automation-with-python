import cv2

image = cv2.imread('elfs.jpeg')
watermark = cv2.imread('watermark.png')

x = image.shape[1] - watermark.shape[1]
y = image.shape[0] - watermark.shape[0]

watermark_place = image[y:, x:]
blend = cv2.addWeighted(watermark_place, 0.5, watermark, 0.7, 0)

image[y:, x:] = blend
cv2.imwrite('elfs-watermark.jpeg', image)