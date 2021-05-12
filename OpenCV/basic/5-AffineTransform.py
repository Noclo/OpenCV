# -*- coding: utf-8 -*-
# @Time : 2020/5/26
# @Author : J
# @File : 图像的几何变换.py
# @Software: PyCharm


import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


#缩放
# img = cv.imread("../image2.jpg")
# res = cv.resize(img,None,fx=2,fy=2,interpolation = cv.INTER_CUBIC)#缩放
# # height,width = img.shape[:2]
# # res = cv.resize(img,(2*width,2*height),interpolation = cv.INTER_CUBIC)#缩放
# cv.imshow("image",img)
# cv.waitKey(0)
# cv.destroyAllWindows()
#平移
# img = cv.imread("../image5.jpg")
# rows,cols,ch = img.shape
# M = np.float32([[1,0,100],[0,1,50]])#偏移(100,50)
# dst = cv.warpAffine(img,M,(cols,rows))#偏移
# cv.imshow("image",dst)
# cv.waitKey(0)
# cv.destroyAllWindows()
#旋转
# img = cv.imread("../image5.jpg")
# rows,cols,ch = img.shape
# M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
# dst = cv.warpAffine(img,M,(cols,rows))
# cv.imshow("image",dst)
# cv.waitKey(0)
# cv.destroyAllWindows()


#仿射变换 坐标装换
# img = cv.imread("../image5.jpg")
# rows,cols,ch = img.shape
# pst1 = np.float32([[50,50],[200,50],[50,200]])
# pst2 = np.float32([[10,100],[200,50],[100,250]])
# M = cv.getAffineTransform(pst1,pst2) #创建2*3矩阵
# dst = cv.warpAffine(img,M,(cols,rows))
# # plt.subplot(121),plt.imshow(img),plt.title("Input")
# # plt.subplot(122),plt.imshow(dst),plt.title("Output")
# cv.imshow("image",dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

#透视变换  试卷扫描
img = cv.imread("../image5.jpg")
rows,cols,ch = img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,300))
# plt.subplot(121),plt.imshow(img),plt.title("Input")
# plt.subplot(122),plt.imshow(dst),plt.title("Output")
# plt.show()
cv.imshow("image",dst)
cv.waitKey(0)
cv.destroyAllWindows()










