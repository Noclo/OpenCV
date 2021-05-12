# -*- coding: utf-8 -*-
# @Time : 2020/5/29
# @Author : J
# @File : 形态学转换.py
# @Software: PyCharm



import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("erosion.png",0)
kernel = np.ones((25,25),np.uint8) #uint8是用0-255表示所有颜色。

erosion = cv.erode(img,kernel,iterations = 1)#侵蚀
dilation = cv.dilate(img,kernel,iterations = 1) #扩张

opening = cv.morphologyEx(img,cv.MORPH_OPEN,kernel) #开运算 侵蚀后扩张 消除噪音
closing = cv.morphologyEx(img,cv.MORPH_CLOSE,kernel) #闭运算 扩张后侵蚀 对内部的小孔小黑点

gradient = cv.morphologyEx(img,cv.MORPH_GRADIENT,kernel) #形态学梯度  镂空 轮廓

tophat = cv.morphologyEx(img,cv.MORPH_TOPHAT,kernel)
#顶帽 输入图像和图像开运算之差 暗背景上的亮物体 得到的效果图突出了比原图轮廓周围的区域更明亮的区域
blackhat = cv.morphologyEx(img,cv.MORPH_BLACKHAT,kernel)
#黑帽 进行闭运算以后得到的图像与原图像的差,所以黑帽运算用来分离比邻近点暗一些的斑块。

plt.subplot(1,2,1),plt.imshow(img),plt.title("Original") #121 1代表行 2代表列  1代表第一个图
plt.xticks([]),plt.yticks([])
plt.subplot(1,2,2),plt.imshow(blackhat),plt.title(" ")
plt.xticks(([])),plt.yticks([])
plt.show()















