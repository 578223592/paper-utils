from canny import *
from region import *
from displayLine import *
from makeCoordinates import *
from averageSlopeIntercept import *

cap = cv2.VideoCapture("../assets/test2.mp4")

while(cap.isOpened()):
    _, frame = cap.read()
    canny_image = canny(frame)
    cropped_image = region_of_interest(canny_image)
    
    lines = cv2.HoughLinesP(cropped_image, 1, np.pi/180, 30, np.array([]), minLineLength=40, maxLineGap=200)
    averaged_lines = average_slope_intercept(frame, lines)
    line_image = display_line(frame, averaged_lines)
    # line_image = display_line(frame, lines)

    combine_image= cv2.addWeighted(frame, 0.8, line_image, 1, 1)
    
    cv2.imshow("Result", combine_image)
    
    if cv2.waitKey(25) == ord('q'): # press q or esc tro eit pro
        break

cap.release()
cv2.destroyAllWindows()