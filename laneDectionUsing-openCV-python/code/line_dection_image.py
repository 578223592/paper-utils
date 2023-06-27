import cv2
import numpy as np

img = cv2.imread("./assets/1.png")
cv2.imshow("origin picture", img)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
edges = cv2.Canny(gray, 0, 200)

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap= 250)

# print(lines)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 255), 3)

cv2.imshow("Edges", edges)
# cv2.imshow("Line dection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()