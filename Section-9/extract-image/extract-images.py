import cv2

video = cv2.VideoCapture("Section-9/extract-image/video.mp4")
success, frame = video.read()

count = 1
while success:
    cv2.imwrite(f'Section-9/extract-image/images/{count}.jpg', frame)
    success, frame = video.read()
    count += 1
