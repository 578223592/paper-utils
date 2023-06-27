import cv2
import numpy as np
def canny(image):

    lower = np.uint8([190, 190,   0])
    upper = np.uint8([255, 255, 255])
    yellow_mask = cv2.inRange(image, lower, upper)

    gray_mask = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) # chuyển về kênh màu sám
    mask = cv2.bitwise_or(gray_mask, yellow_mask)
    masked = cv2.bitwise_and(image, image, mask = mask)

    blur = cv2.GaussianBlur(masked, (5,5), 0) # làm mịn theo ô 5-5 
    canny = cv2.Canny(blur, 0, 200) # canny làm tách biệt 2 khoảng màu nhạt và đậm  
    # cv2.imshow("canny", canny) 
    return canny