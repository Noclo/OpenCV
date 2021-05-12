# -*- coding: utf-8 -*-
# @Time : 2020/5/24
# @Author : J
# @File : 图像的基本操作.py
# @Software: PyCharm


import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread("../image.jpg")

# px = img[100,100] #行和列坐标来访问像素值
# print(px)
#
# blue = img[100,100,0] #访问指定通道的像素值
# print(blue)
#
#
# img[100,100] = [0,0,0] #修改像素值
#
#
# img.item(10,10,2)  #  （10,10,2）是坐标 修改某一点的像素
# img.itemset((10,10,2),100)


# print(img.shape)
# print(img.size)
# print(img.dtype)


#图像感兴趣区域ROI
eyes = img[285:345,335:395]   #位置改变
img[273:333,100:160] = eyes

b,g,r = cv.split(img)
img = cv.merge((b,g,r))



cv.namedWindow("image",cv.WINDOW_NORMAL)#可调整窗口大小
cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows()


# BLUE = [255,0,0]
# img1 = cv.imread('../image.png')
# #为图像设置边框（填充）
# replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
# reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
# reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
# wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
# constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)
# plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
# plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
# plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
# plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
# plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
# plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
# plt.show()
