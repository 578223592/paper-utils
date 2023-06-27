# import cv2
#
# # 读取图像
# img = cv2.imread('../assets/road.png')
#
# # 将图像转换为灰度图像
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype('int16')
#
# # 对灰度图像进行Laplacian算子增强
# laplacian = cv2.Laplacian(gray, cv2.CV_16S, ksize=3)
#
# # 将边界增强后的图像转化为8位无符号整型
# laplacian = cv2.convertScaleAbs(laplacian)
#
# # 自适应阈值二值化
# binary = cv2.adaptiveThreshold(laplacian, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
#
# # 显示结果
# cv2.imshow('binary', binary)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# import cv2
#
#
# # 读取图像
# img = cv2.imread('../assets/road.png')
#
# # 将图像分离为三个通道
# b, g, r = cv2.split(img)
#
# # 分别对RGB三个通道进行Laplacian增强
# laplacian_b = cv2.Laplacian(b, cv2.CV_16S, ksize=3)
# laplacian_g = cv2.Laplacian(g, cv2.CV_16S, ksize=3)
# laplacian_r = cv2.Laplacian(r, cv2.CV_16S, ksize=3)
#
# # 将边界增强后的图像转化为8位无符号整型
# laplacian_b = cv2.convertScaleAbs(laplacian_b)
# laplacian_g = cv2.convertScaleAbs(laplacian_g)
# laplacian_r = cv2.convertScaleAbs(laplacian_r)
#
# # 将三个通道的边界增强后的图像合并
# laplacian = cv2.merge([laplacian_b, laplacian_g, laplacian_r])
#
# # 将图像转换为灰度图像
# gray = cv2.cvtColor(laplacian, cv2.COLOR_BGR2GRAY)
#
# # 自适应阈值二值化
# binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
#
# # 显示结果
# cv2.imshow('lap',laplacian)
# cv2.imshow('binary', binary)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import cv2
#
# # 读取彩色图像
# img = cv2.imread('../assets/man.png')
#
# # 将图像分离为BGR三个通道
# b, g, r = cv2.split(img)
#
# # 对每个通道进行Laplacian算子增强
# lap_b = cv2.Laplacian(b, cv2.CV_16S, ksize=3)
# lap_g = cv2.Laplacian(g, cv2.CV_16S, ksize=3)
# lap_r = cv2.Laplacian(r, cv2.CV_16S, ksize=3)
#
# # 将每个通道处理后的图像转化为8位无符号整型
# lap_b = cv2.convertScaleAbs(lap_b)
# lap_g = cv2.convertScaleAbs(lap_g)
# lap_r = cv2.convertScaleAbs(lap_r)
#
# # 将三个通道合并为一张图像
# laplacian = cv2.merge([lap_b, lap_g, lap_r])
#
# # 显示结果
# cv2.imshow('laplacian', laplacian)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import numpy as np
# 读取图像
img = cv2.imread('../assets/man.png')

# 检查图像是否成功读取
if img is None:
    print("打开图片失败,请检查")
    exit(0)

# 显示原图像
cv2.imshow("原图像", img)

# 构造卷积核
kernel = [[0, -1, 0], [0, 5, 0], [0, -1, 0]]
kernel = np.array(kernel, dtype='float32')

# 进行滤波操作
dst = cv2.filter2D(img, -1, kernel)

# 显示处理后的图像
cv2.imshow("拉普拉斯算子图像增强效果", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
