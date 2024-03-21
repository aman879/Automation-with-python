import cv2

video = cv2.VideoCapture("video.mp4")
success, frame = video.read()

height = frame.shape[0]
width = frame.shape[1]
face_cascade = cv2.CascadeClassifier('faces.xml')
output = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

while success:
    face = face_cascade.detectMultiScale(frame, 1.1, 4)
    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 4)
    output.write(frame)
    success, frame = video.read()

output.release()