# -*- coding: utf-8 -*-

import math
import numpy as np



class MyGaussianBlur():
    #init
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
        arr = np.array(dataMat)
        height = arr.shape[0]
        width = arr.shape[1]
        newData = np.zeros((height, width))
        for i in range(self.radius, height - self.radius):
            for j in range(self.radius, width - self.radius):
                t = arr[i - self.radius:i + self.radius + 1, j - self.radius:j + self.radius + 1]

                a = np.multiply(t, template)
                newData[i, j] = a.sum()
        return newData

    # Difference of Gaussion
    # Data format: dataMat2's sigma > dataMat1's sigma
    def diffOfGauus(self,dataMat1,dataMat2):
        return np.subtract(dataMat2,dataMat1)
