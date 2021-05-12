# -*- coding: utf-8 -*-
# @Time : 2020/5/23 19:49
# @Author : J
# @File : 视频入门.py
# @Software: PyCharm

#打开摄像头
import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("cannot not open camera")
    exit()
while True:
    ret,frame = cap.read() #第一个参数ret 为True 或者False,代表有没有读取到图片 第二个参数frame表示截取到一帧的图片
    frame = cv.flip(frame,1) #镜像处理
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)#灰度处理
    cv.imshow("打开摄像头",frame)
    if cv.waitKey(1) == ord("q"):
        break
cap.release()
cv.destroyAllWindows()


#播放视频
cap = cv.VideoCapture("wing.mp4")
while cap.isOpened():
    ret,frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow("shame",gray)
    # cv.waitKey(30);
    if cv.waitKey(1) == ord("q"):
        break
cap.release()
cv.destroyAllWindows()


#保存视频
cap = cv.VideoCapture(0)
# FourCC是用于指定视频编解码器的4字节代码，在Fedora中：DIVX，XVID，MJPG，X264，WMV1，WMV2。
# 最好使用XVID。MJPG会生成大尺寸的视频。X264会生成非常小的尺寸的视频

fourcc = cv.VideoWriter_fourcc(*"XVID")
out = cv.VideoWriter("output.avi",fourcc,20.0,(640,480))  #输出视频 解码器  帧率 大小
while cap.isOpened():
    ret,frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    frame = cv.flip(frame,1)
    out.write(frame)
    cv.imshow("frame",frame)
    if cv.waitKey(1) == ord("q"):
        break

cap.release()
out.release()
cv.destroyAllWindows()





