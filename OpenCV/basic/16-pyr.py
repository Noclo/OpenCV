# -*- coding: utf-8 -*-
# @Time : 2020/5/31
# @Author : J
# @File : 图像金字塔.py
# @Software: PyCharm


import cv2 as cv

import numpy as np,sys

A = cv.imread("../apple.png")
B = cv.imread("../li.png")
#生成A的高斯金字塔
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpA.append(G)

#生成B的高斯金字塔
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpB.append(G)
#生成A的拉普拉斯金字塔
lpA = [gpA[5]]
for i in range(5,0,-1):
    GE = cv.pyrUp(gpA[i])
    L = cv.subtract(gpA[i-1],GE)
    lpA.append(L)
#生成B的拉普拉斯金字塔
lpB = [gpB[5]]
for i in range(5,0,-1):
    GE = cv.pyrUp(gpB[i])
    L = cv.subtract(gpB[i-1],GE)
    lpB.append(L)
#现在在每个级别中添加左右两个图像
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    ls = np.hstack(la[:,0:cols/2],lb[:,cols/2:])
    LS.append(ls)

ls_ = LS[0]
for i in range(1,6):
    ls_ = cv.pyrUp(ls_)
    ls_ = cv.add(ls_,LS[i])

real = np.hstack((A[:,:cols/2],B[:,cols/2:]))
cv.imwrite("1.jpg",ls_)
cv.imwrite("2.jpg",real)




