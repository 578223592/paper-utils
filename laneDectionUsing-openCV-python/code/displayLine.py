from tkinter import SOLID
import cv2
import numpy as np

''' vẽ đường lên ảnh'''
def display_line(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 15, cv2.LINE_AA)
    return line_image