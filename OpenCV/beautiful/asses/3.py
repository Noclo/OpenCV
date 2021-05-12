# -*- coding: utf-8 -*-
# @Time : 2021/3/18
# @Author : J
# @File : 3.py
# @Software: PyCharm
import cv2 as cv

if __name__ == '__main__':
    img1 = cv.imread('Li2.PNG')
    img2 = cv.imread('YN4.jpg')

    # 热图变成和原图大小相同
    heatmap = cv.resize(src=img2, dsize=(img1.shape[1], img1.shape[0]))

    # 把热图处理成CV中的密度热力图样式
    # heatmap = cv.applyColorMap(heatmap, cv.COLORMAP_JET)

    # 叠加
    # src1不透明。src2透明度0.9
    img_add = cv.addWeighted(src1=img1, alpha=1, src2=heatmap, beta=0.5, gamma=0)

    # 显示图
    cv.namedWindow("Li", cv.WINDOW_NORMAL)
    cv.imshow('Li', img_add)
    cv.waitKey(0)
    #
    # # 保存图
    # save_path = 'heatmap2.jpg'
    # cv.imwrite(save_path, img_add)
