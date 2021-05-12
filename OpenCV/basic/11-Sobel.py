# -*- coding: utf-8 -*-
# @Time : 2020/5/30
# @Author : J
# @File : 图像梯度.py
# @Software: PyCharm

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread("datika.png",0)

laplacian = cv.Laplacian(img,cv.CV_64F) #拉普拉斯算子
sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize = 5)# sobel 算子
sobely= cv.Sobel(img,cv.CV_64F,0,1,ksize = 5)
plt.subplot(221),plt.imshow(img,cmap = "gray")
plt.title("original"),plt.xticks([]),plt.yticks([])
plt.subplot(222),plt.imshow(laplacian,cmap = "gray")
plt.title("Laplacian"),plt.xticks([]),plt.yticks([])
plt.subplot(223),plt.imshow(sobelx,cmap = "gray")
plt.title("Sobel X"),plt.xticks([]),plt.yticks([])
plt.subplot(224),plt.imshow(sobely,cmap = "gray")
plt.title("Sobel Y"),plt.xticks([]),plt.yticks([])
plt.show()















