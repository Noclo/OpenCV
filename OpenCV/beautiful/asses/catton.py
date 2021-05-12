# -*- coding: utf-8 -*-
# @Time : 2020/9/14
# @Author : J
# @File : catton.py
# @Software: PyCharm
import cv2

img = cv2.imread("Li.jpg")
img_copy = img

# 灰度处理
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 平滑操作，去除噪声
img_blur = cv2.GaussianBlur(img_gray,(5,5),0.8)#中值滤波
# 通过阈值提取轮廓
img_edge = cv2.adaptiveThreshold(img_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, blockSize=11,C=3)
# 将灰度图片变成 3 通道，用于后续合并
img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2BGR)


for _ in range(2):
	# 降低分辨率
    img_copy = cv2.pyrDown(img_copy)
for _ in range(5):
	# 图像平滑，保留边缘
    img_copy = cv2.bilateralFilter(img_copy, d=9, sigmaColor=3, sigmaSpace=2)
img_copy = cv2.resize(img_copy, (img.shape[1], img.shape[0]),
                       interpolation=cv2.INTER_CUBIC)


img_cartoon = cv2.bitwise_and(img_copy, img_edge)

cv2.namedWindow("Li",cv2.WINDOW_NORMAL)
cv2.imshow("Li",img_cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()






