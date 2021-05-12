# -*- coding: utf-8 -*-
# @Time : 2020/5/23 21:21
# @Author : J
# @File : 绘图功能.py
# @Software: PyCharm

import numpy as np
import cv2 as cv

img = np.zeros((512,512,3),np.uint8)
# np.zeros()有两个参数，一个是创建的图片矩阵大小，另一个是数据类型
# 512,512是像素(第一个512像素高，第二个是512像素宽)，3指BGR三种颜色
# uint8是用0-255表示所有颜色。

cv.line(img,(0,0),(511,511),(0,255,0),5)
#这个函数有5个参数，img是图像名称，起点坐标，终点坐标，（255,0,0）是蓝色，5是线的宽度

cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv.circle(img,(447,63),63,(0,0,255),-1)
#这个函数有5个参数，图像名称，圆心坐标，半径63，（0,0,255）红色，线宽为-1，当线宽-1时表示封闭图形的颜色填充。

cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
#椭圆 这个函数有8个参数：图像名称，中心点坐标，长轴长度，短轴长度，旋转角度，
#图像出现的部分（长轴顺时针方向起始的角度和结束角度）0,180是下半个椭圆，颜色数组这里255是蓝色，线宽

pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)  #多边形
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255)) #True表示闭合，（0,255,255）是黄色，3是线宽

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,"OpenCV",(10,500),font,4,(255,255,255),2,cv.LINE_AA)
#这个函数有八个参数，图像名称，字符串，坐标，字体，字号，（255,255,255）白色、线宽2
cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows()









