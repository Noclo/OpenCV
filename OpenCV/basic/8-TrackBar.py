# -*- coding: utf-8 -*-
# @Time : 2020/5/24
# @Author : J
# @File : 轨迹栏作为调色板.py
# @Software: PyCharm


import numpy as np
import cv2 as cv
def nothing(x):
    pass

img = np.zeros((300,512,3),np.uint8)
cv.namedWindow("image")
cv.createTrackbar("R","image",0,255,nothing)
cv.createTrackbar("G","image",0,255,nothing)
cv.createTrackbar("B","image",0,255,nothing)

switch = "0 : OFF\n 1 : ON"
cv.createTrackbar(switch,"image",0,1,nothing)
while(1):
    cv.imshow("image",img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    r = cv.getTrackbarPos("R","image")
    g = cv.getTrackbarPos("G","image")
    b = cv.getTrackbarPos("B","image")
    s = cv.getTrackbarPos("S","image")

    if s ==0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
cv.destroyAllWindows()









