# -*- coding: utf-8 -*-
# @Time : 2020/5/23 18:45
# @Author : J
# @File : 图像入门.py
# @Software: PyCharm

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 读取图像
img = cv.imread("../image.jpg",0) # 1是彩色图像 0是灰度图 -1是原始图像
cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows()

# 显示图像
# cv.namedWindow("image",cv.WINDOW_NORMAL)#   可调整窗口大小
# cv.imshow("image",img)
# cv.waitKey(0)   #持续存在知道有按键发生
# cv.destroyAllWindows()

# 保存图像为 png格式
# cv.imwrite("image.png",img)

# 总结
# cv.imshow("image",img)
# k = cv.waitKey(0)
# if k == 27 & 0xFF:      #Esc的ASCII码为27,即判断是否按下esc键
#     cv.destroyAllWindows()
# elif k == ord("s"):
#     cv.imwrite("image.png",img)
#     cv.destroyAllWindows()

# 使用Matplotlib
# OpenCV加载的彩色图像处于BGR模式。
# 但是Matplotlib以RGB模式显示。
# 因此，如果使用OpenCV读取彩色图像，
# 则Matplotlib中将无法正确显示彩色图像
# plt.imshow(img,cmap = "gray",interpolation = "bicubic")
# plt.xticks([]),plt.yticks([])
# plt.show()




