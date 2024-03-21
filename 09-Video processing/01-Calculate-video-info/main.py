import cv2

video = cv2.VideoCapture("video.mp4")

width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
nr_framse = video.get(cv2.CAP_PROP_POS_FRAMES)
fps = video.get(cv2.CAP_PROP_FPS)

print(width, height, nr_framse, fps)