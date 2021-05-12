# -*- coding: utf-8 -*-
# @Time : 2020/5/24
# @Author : J
# @File : 图像上的算术运算.py
# @Software: PyCharm

import cv2 as cv
import numpy as np
img1 = cv.imread("../image2.jpg")
img2 = cv.imread("../image3.jpg")
dst = cv.addWeighted(img1,0.5,img2,0.5,0)
cv.namedWindow('dst',cv.WINDOW_NORMAL)
cv.imshow("dst",dst)
cv.waitKey(0)
cv.destroyAllWindows()

img1 = cv.imread('../image2.jpg')
img2 = cv.imread('../image3.png')
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]
# 现在创建logo的掩码，并同时创建其相反掩码
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
#src:灰度图  thresh阈值 maxval：最大值  type：阈值类型
# 第一个参数ret 为True 或者False,代表有没有读取到图片 mask：二值化的图像
# 将灰度图img2gray中灰度值小于10的点置0，灰度值大于175的点置255


mask_inv = cv.bitwise_not(mask)
# # 现在将ROI中logo的区域涂黑
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
# 仅从logo图像中提取logo区域
img2_fg = cv.bitwise_and(img2,img2,mask = mask)
# 将logo放入ROI并修改主图像
dst = cv.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv.namedWindow('dst',cv.WINDOW_NORMAL)
cv.imshow('dst',img1)
cv.waitKey(0)
cv.destroyAllWindows()





