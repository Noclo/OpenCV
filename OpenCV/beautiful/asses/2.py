# -*- coding: utf-8 -*-
# @Time : 2021/3/18
# @Author : J
# @File : 2.py
# @Software: PyCharm

import cv2

img = cv2.imread("li2.png")
img_copy = img

# 灰度处理
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 平滑操作，去除噪声
img_blur = cv2.medianBlur(img_gray, 7)
# 通过阈值提取轮廓
img_edge = cv2.adaptiveThreshold(img_blur,
                                 255,
                                 cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY,
                                 blockSize=9,
                                 C=3)
# 将灰度图片变成 3 通道，用于后续合并
img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2BGR)
cv2.namedWindow("Li",cv2.WINDOW_NORMAL)
cv2.imshow("Li", img_edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
