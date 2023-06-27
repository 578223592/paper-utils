import cv2
import numpy as np
import matplotlib.pyplot as plt

video = cv2.VideoCapture("./assets/test2.mp4")

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    
    edges = cv2.Canny(gray, 75, 100)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap= 250)

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 255), 3)

    if not ret:
        video = cv2.VideoCapture("roadTrip1.mp4")
        continue
    # plt.imshow(edges)
    # plt.show()
    # cv2.imshow("frame", frame)
    cv2.imshow("line", edges)
    key = cv2.waitKey(25)
    if key == 27: 
        # nhấn esc để thoát 
        break
video.release()
cv2.destroyAllWindows()