import cv2
import numpy as np
import matplotlib.pyplot as plt
#--------------------lọc ra vùng có làn đường-----------------------# 
def region_of_interest(image):
    dim = (1280, 720)
    image = cv2.resize(image, dim, interpolation= cv2.INTER_AREA)

    height = image.shape[0]
    pollygons = np.array([[(128, height),(220, height),(380, int(height*2/3)), (330, int(height*2/3))],[(520, height),(600, height), (516,int(height*2/3) ), (470, int(height*2/3))] ])
    pollygons = np.array([[(250, height), (1100, height), (800, int(height*2/3)),(450, int(height*2/3))]]) # lọc theo hình thang
    mask = np.zeros_like(image)
    
    cv2.fillPoly(mask, pollygons, 255)
    # cv2.imshow('mask',mask)
    # plt.imshow(image)
    # plt.show()
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image