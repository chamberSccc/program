# -*- coding: utf-8 -*-

import math
import numpy as np


class MyGaussianBlur():
    # init
    def __init__(self, radius=1, sigma=1.5):
        self.radius = radius
        self.sigma = sigma

    def CalcGauss(self, x, y):
        """
        Calcaulate  Gaussion distribution number at each matrix index
        Parameter
        ---------
        x: row index
        y: column index
        """
        res1 = 1 / (2 * math.pi * self.sigma * self.sigma)
        res2 = math.exp(-(x * x + y * y) / (2 * self.sigma * self.sigma))
        return res1 * res2

    def GaussKernelMat(self):
        """
        Get the Gaussion blur template
        """
        sideLength = self.radius * 2 + 1
        result = np.zeros((sideLength, sideLength))
        for i in range(sideLength):
            for j in range(sideLength):
                result[i, j] = self.CalcGauss(i - self.radius, j - self.radius)
        all = result.sum()
        return result / all

    def Convolute(self, dataMat, template):
        """
        Data matrix convolute with the data matrix
        Parameter
        ---------
        dataMat:  array_like convoluted array data
        template: array_like convolute template

        Returns
        -------
        newData: result
        """
        # 先把属性矩阵进行扩充
        radius = (template.shape[0] - 1) / 2
        arr = np.array(dataMat)
        height = arr.shape[0]
        width = arr.shape[1]
        first_row = arr[0, :]
        last_row = arr[-1, :]
        # 扩充矩阵元素
        for i in range(0, radius):
            arr = np.insert(arr, 0, values=first_row, axis=0)
            arr = np.insert(arr, -1, values=last_row, axis=0)
        first_col = arr[:, 0]
        last_col = arr[:, -1]
        for i in range(0, radius):
            arr = np.insert(arr, 0, values=first_col, axis=1)
            arr = np.insert(arr, -1, values=last_col, axis=1)
        newData = np.zeros((height, width))
        height1 = arr.shape[0]
        width1 = arr.shape[1]
        # 处理矩阵中左边和下边是0的点
        for i in range(0, height1):
            for j in range(0, width1):
                temp = arr[i, j]
                if j < width1 - 1:
                    right = arr[i, j + 1]
                    if temp == 0 and right != 0:
                        arr[i, j] = right
                if i < height1 - 1:
                    up = arr[i + 1, j]
                    if temp == 0 and up != 0:
                        arr[i, j] = up
        # 处理矩阵中右边和上边是0的点
        for i in range(height1 - 1, -1, -1):
            for j in range(width1 - 1, -1, -1):
                temp = arr[i, j]
                if i > 0:
                    below = arr[i - 1, j]
                    if temp == 0 and below != 0:
                        arr[i, j] = below;
                if j > 0:
                    left = arr[i, j - 1]
                    if temp == 0 and left != 0:
                        arr[i, j] = left
        for i in range(radius, height1 - radius):
            for j in range(radius, width1 - radius):
                t = arr[i - radius:i + radius + 1, j - radius:j + radius + 1]

                a = np.multiply(t, template)
                newData[i - radius, j - radius] = a.sum()

        height1 = newData.shape[0]
        width1 = newData.shape[1]
        # 处理矩阵中右边和上边是0的点
        for i in range(0, height1):
            for j in range(0, width1):
                temp = newData[i, j]
                if j < width1 - 1:
                    right = newData[i, j + 1]
                    if temp != 0 and right == 0:
                        newData[i, j]=0
        return newData

    # Difference of Gaussion
    # Data format: dataMat2's sigma > dataMat1's sigma
    def diffOfGauus(self, dataMat1, dataMat2):
        return np.subtract(dataMat2, dataMat1)
