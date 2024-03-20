import cv2
import os

images = os.listdir('images')
face_cascade = cv2.CascadeClassifier('faces.xml')
i = 0;
for image in images:
    inent = cv2.imread(f'images/{image}', 1)
    face = face_cascade.detectMultiScale(inent,1.1,4)
    if(len(face) != 0):
        cv2.imwrite(f'images-with-face/{image}', inent)