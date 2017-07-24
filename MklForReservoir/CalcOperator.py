# -*- coding: utf-8 -*-

import math
import numpy as np



class MyGaussianBlur():
    #gradOpeator = np.array([[0,1,0],[1,-4,1],[0,1,0]])#laplace 算子
    #sobelX = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])#方向导数暂用sobel算子
    #sobelY = np.array([[1,2,1],[0,0,0],[-1,-2,1]])

    # 初始化  ifPure 判断返回特征矩阵 还是返回整合特征矩阵的地震数据列表
    def __init__(self, radius=1, sigma=1.5):
        self.radius = radius
        self.sigma = sigma

    def CalcGauss(self, x, y):
        res1 = 1 / (2 * math.pi * self.sigma * self.sigma)
        res2 = math.exp(-(x * x + y * y) / (2 * self.sigma * self.sigma))
        return res1 * res2
        # 得到滤波模版

    def GaussKernelMat(self):
        sideLength = self.radius * 2 + 1
        result = np.zeros((sideLength, sideLength))
        for i in range(sideLength):
            for j in range(sideLength):
                result[i, j] = self.CalcGauss(i - self.radius, j - self.radius)
        all = result.sum()
        return result / all

    def Convolute(self, dataMat, template):
        arr = np.array(dataMat)
        height = arr.shape[0]
        width = arr.shape[1]
        newData = np.zeros((height, width))
        for i in range(self.radius, height - self.radius):
            for j in range(self.radius, width - self.radius):
                t = arr[i - self.radius:i + self.radius + 1, j - self.radius:j + self.radius + 1]

                a = np.multiply(t, template)
                newData[i, j] = a.sum()
        #消除边缘为0效应，用原始数据补上
        newData[:,0] = dataMat[:,0]
        newData[0,:] = dataMat[0,:]
        return newData

    # 2的sigma要比1的sigma大
    def diffOfGauus(self,dataMat1,dataMat2):
        return np.subtract(dataMat2,dataMat1)

# r=1 #模版半径，自己自由调整
# s=3 #sigema数值，自己自由调整
# GBlur=MyGaussianBlur(radius=r, sigma=4.0)#声明高斯模糊类
# temp=GBlur.GaussKernelMat()#得到滤波模版
# print temp