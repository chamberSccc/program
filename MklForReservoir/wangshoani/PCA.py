# -*- coding: utf-8 -*-
import numpy as np
# 均值化
def zeroMean(x):
    meanVal = np.mean(x,axis=0)     #按列求均值，即求各个特征的均值
    newData = x - meanVal
    return newData, meanVal

# PCA
def pca(x,n):
    newData,meanVal = zeroMean(x)
    covMat = np.cov(newData, rowvar = 0)    #求协方差矩阵,return ndarray；若rowvar非0，一列代表一个样本，为0，一行代表一个样本

    eigVals,eigVects = np.linalg.eig(np.mat(covMat))#求特征值和特征向量,特征向量是按列放的，即一列代表一个特征向量
    eigValIndice = np.argsort(eigVals)            #对特征值从小到大排序
    n_eigValIndice = eigValIndice[-1:-(n + 1):-1]   #最大的n个特征值的下标
    n_eigVect = eigVects[:,n_eigValIndice]        #最大的n个特征值对应的特征向量
    lowDDataMat = newData*n_eigVect               #低维特征空间的数据
    reconMat = (lowDDataMat*n_eigVect.T) + meanVal  #重构数据
    return lowDDataMat, reconMat


temparray = np.array([[1,2,3],[4,5,6],[7,8,9]])
zeroMean(temparray)