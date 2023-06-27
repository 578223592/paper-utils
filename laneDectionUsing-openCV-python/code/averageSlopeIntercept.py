import numpy as np
from makeCoordinates import *

global_left_fit_average = []
global_right_fit_average = []
global_counter = 0 
''' tìm ra đường đi trung bình '''

def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []  
    global global_left_fit_average
    global global_right_fit_average
    global global_counter

    
    if global_counter < 3 :
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line.reshape(4)
                if x2 != x1 :

                    slope = (y2-y1) / (x2-x1)
                    intercept = y1 - slope* x1
                    
                    # length = np.sqrt((y2-y1)**2 + (x2-x1)**2)
                    # parameters = np.polyfit((x1, x2), (y1,y2), 1)
                    # print('polyfit' ,parameters)
                    # slope = parameters[0]
                    # intercept = parameters[1]
                    if (slope < -0.5 ):
                        left_fit.append((slope, intercept))
                        # left_weigth.append((length))
                    # elif (slope > 1 and slope < 2.8):
                    else:
                        right_fit.append((slope, intercept))
                        # right_weight.append((length))
                
    elif global_counter > 5:
        global_counter = 0
    global_counter += 1
            
            
    if (len(left_fit) == 0):
        left_fit_average = global_left_fit_average
    else:
        left_fit_average = np.average(left_fit, axis=0)
        global_left_fit_average = left_fit_average 
        # trong trường hợp nếu ko tìm đc thì sẽ lấy giá trị cũ để đưa vào 
    if (len(right_fit) == 0):
        right_fit_average = global_right_fit_average
    else: 
        right_fit_average = np.average(right_fit, axis=0)
        global_right_fit_average = right_fit_average
    left_line = make_coordinates(image, left_fit_average)
    right_line = make_coordinates(image, right_fit_average)
    
    return np.array([left_line, right_line])