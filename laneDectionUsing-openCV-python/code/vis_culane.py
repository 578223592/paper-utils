
import cv2
import numpy as np




print("start")
# 读取图像
img = cv2.imread('../assets/00180.jpg')
# 显示图像
cv2.imshow("原图", img)
# 检查图像是否成功读取
if img is None:
    print("打开图片失败,请检查")
    exit(0)
# 从文件中读取坐标点
with open('../assets/00180.lines.txt', 'r') as f:
    points_str = f.read().strip().split('\n')


# 构造蒙版
mask = np.zeros_like(img, dtype=np.uint8)


points = []
for oneLane in points_str:
    laneStr = oneLane.split()
    lane = np.array(laneStr, dtype=np.float32).reshape(-1, 2).astype(int)
    cv2.polylines(mask, [lane], False, color=(255, 255, 255), thickness=10)  # 第一组坐标点用红色标记

points = np.array(points, dtype=np.float32).reshape(-1, 2).astype(int)


# 构造卷积核
# kernel = [[0, -1, 0], [0, 3, 0], [0, -1, 0]]
kernel = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
kernel = np.array(kernel, dtype='float32')

# 进行滤波操作
dst = cv2.filter2D(img, -1, kernel)
cv2.imshow("dst",dst)

# for point in points:
#     cv2.circle(mask, tuple(point), radius=15, color=(255, 255, 255), thickness=-1)


# 在目标图像上替换指定区域
img[np.where(mask != 0)] = dst[np.where(mask != 0)]

# 显示图像
cv2.imshow("标记坐标点", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

