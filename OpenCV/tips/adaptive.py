# -*- coding: utf-8 -*-
# @Time : 2020/11/18
# @Author : J
# @File : Practise-1.py
# @Software: PyCharm


import numpy as np
import cv2


img = cv2.imread("../adaptive.jpg")
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval,threshold = cv2.threshold(grayscaled,10,255,cv2.THRESH_BINARY)
TH = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow("orginal",img)
cv2.imshow("threshold",TH)
cv2.waitKey(0)
cv2.destroyAllWindows()








