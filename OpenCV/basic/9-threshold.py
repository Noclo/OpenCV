# -*- coding: utf-8 -*-
# @Time : 2020/5/27
# @Author : J
# @File : 图像阈值.py
# @Software: PyCharm


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#全局阈值
img = cv.imread("../image2.jpg",0)
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV) #INV表示相反的图像
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
titles = ["Original Image","BINARY","BINARY_INV","TRUNC","TOZERO","TOZERO_INV"]
images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()


# img = cv.imread("../image6.jpg",0)
# ret1,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# #该函数有两个返回值，第一个retVal（得到的阈值值（在后面一个方法中会用到）），第二个就是阈值化后的图像。
#
# ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
#
# blur = cv.GaussianBlur(img,(5,5),0)
# ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
#
# images = [img,0,th1,
#           img,0,th2,
#           blur,0,th3]
# titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
#           'Original Noisy Image','Histogram',"Otsu's Thresholding",
#           'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
#
# for i in range(3):
#     plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],"gray")
#     plt.title(titles[i*3]),plt.xticks([]),plt.yticks([])
#
#     plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
#     plt.title(titles[i * 3+1]), plt.xticks([]), plt.yticks([])
#
#     plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],"gray")
#     plt.title(titles[i * 3 + 2]), plt.xticks([]), plt.yticks([])
#
# plt.show()













