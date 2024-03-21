import cv2

video = cv2.VideoCapture('smile.mp4')
success, frame = video.read()

height = frame.shape[0]
widht = frame.shape[1]

face_cascade = cv2.CascadeClassifier('faces.xml')

output = cv2.VideoWriter('blurred_smile.avi', cv2.VideoWriter_fourcc(*"DIVX"), 30, (widht, height))

while success:
    face = face_cascade.detectMultiScale(frame, 1.1, 4)
    for (x, y, w, h) in face:
        frame[y:y+h, x:x+w] = cv2.blur(frame[y:y+h, x:x+h], (50, 50))
    output.write(frame)
    success, frame = video.read()

output.release()