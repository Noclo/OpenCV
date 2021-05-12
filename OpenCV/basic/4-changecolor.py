# -*- coding: utf-8 -*-
# @Time : 2020/5/25
# @Author : J
# @File : 改变颜色空间.py
# @Software: PyCharm



# import cv2 as cv
# flags = [i for i in dir(cv) if i.startswith("COLOR")]
# print(flags)

import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(1):
    _,frame = cap.read()
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    mask = cv.inRange(hsv,lower_blue,upper_blue)
    res = cv.bitwise_and(frame,frame,mask = mask)
    # cv.imshow("frame",frame)
    # cv.imshow("mask",res)
    cv.imshow("res",res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()














