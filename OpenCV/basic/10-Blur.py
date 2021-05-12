# -*- coding: utf-8 -*-
# @Time : 2020/5/28
# @Author : J
# @File : 图像平滑.py
# @Software: PyCharm

#2d卷积
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#图像过滤
# img = cv.imread("image4.png")
# kernel = np.ones((3,3),np.float32)/9
# dst = cv.filter2D(img,-1,kernel)
# plt.subplot(121),plt.imshow(img),plt.title("original")
# plt.xticks([]),plt.yticks([])
# plt.subplot(122),plt.imshow(dst),plt.title("Averaging")
# plt.xticks([]),plt.yticks([])
# plt.show()

#图像平滑
#平均滤波
img = cv.imread("image4.png")
blur = cv.blur(img,(5,5))#平均滤波
GaussianBlur = cv.GaussianBlur(img,(9,9),0)# 高斯模糊  0为标准偏差
medianBlur = cv.medianBlur(img,5) #中值模糊
bilateralFilter = cv.bilateralFilter(img,9,75,75)#双边滤波

plt.subplot(121),plt.imshow(img),plt.title("Original")
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(bilateralFilter),plt.title("blurred")
plt.xticks(([])),plt.yticks([])
plt.show()










