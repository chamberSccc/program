# -*- coding: utf-8 -*-
# from matplotlib import *
# from pylab import *
import math
import numpy as np
import cv2 as cv
from CalcOperator import MyGaussianBlur
import os

seisDataDir = 'data/seismic/seismic'
seisTestDir = 'data/seismic/testdata'
wellLogDataDir = 'data/well/welllog/data.txt' #x y z shen kong bao bozukang x y z
wellTopDataDir = 'data/well/welltop.dat'
seismicMaxLength = 100  # 二维数组每行长度不等时计算出最长的那行,数据预处理的时候得到的值，当做全局变量处理，不必在程序中展现

#返回完整地震数据矩阵(data),网格排列波阻抗矩阵(dataValue)，坐标矩阵(dataCoord)
def seisData2Mat(dataDir):
    data = []
    dataCoord = []
    dataValue = []
    tempDataValue = []
    index = 0
    row = -1
    for line in open(dataDir):
        # filter the data title
        if len(line) < 40 and line[0:6] != '-99.00':
            continue
        # 如果是第一次碰到非法数据
        if line[0:6] == '-99.00' and index == 0:
            index += 1
            continue
        # 如果现在正在非法数据循环中
        if line[0:6] == '-99.00' and index != 0:
            continue
        # 如果第一次碰到非法数据的下一行
        if line[0:6] != '-99.00' and index == 1:
            dataValue.append(tempDataValue)
            tempDataValue = []
            index = 0;
            row += 1;

        temp = line.replace('\r','').replace('\n','').rstrip().split(' ')
        floatTemp = [round(float(x),2) for x in temp]

        tempDataValue.append(floatTemp[3])
        dataCoord.append(floatTemp[:2])
        # floatTemp.pop(2)
        data.append(floatTemp)
    #存入最后一行数据
    dataValue.append(tempDataValue)

    # 数0组中长度不等的地方补0
    map(extend0Toarray, dataValue)
    # dataDesc = dataValue[::-1]
    npDataValue= np.array(dataValue)

    return data,npDataValue, dataCoord

#返回x,y坐标   label:孔隙度
def wellData2Mat(seisdataMat):
    resultList = []
    # f = open('data/well/welllog/result.txt', 'w')
    for line in open(wellLogDataDir):
        temp = line.replace('\r', '').replace('\n', '').replace('"', '').replace('\t', '').rstrip().split(' ')
        temp = filter(notEmpty, temp)
        seisMatNp = np.array(seisdataMat)
        compare = (abs(float(temp[1]) - seisMatNp[:,0]) <= 50.0) & (abs(float(temp[2])-seisMatNp[:,1])<=50.0)
        x = np.extract(compare,seisMatNp[:,0])
        y = np.extract(compare, seisMatNp[:,1])
        z = np.extract(compare, seisMatNp[:,2])
        wave = np.extract(compare, seisMatNp[:,3])
        if x.size == 0:
           pass
        else:
            temp.extend([x[0], y[0], z[0], wave[0]])
        resultList.append(temp)
        # f.write(''.join([str(v)+' ' for v in temp])+'\n')
    # f.close()
    a=1

    #组合特征数据格式
    return
#地震数据 + 论文中提到的16种特征数据组合,写入文件
def seisDataAndFeature(seisData,featureData):
    for i, data in enumerate(seisData):
        temp = featureData[i%130,i-(i%130)]
        data.extend(temp)
        aaaaa=1
    return
def extend0Toarray(x):
    temp = [0 for i in range(0, seismicMaxLength - len(x))]
    x.extend(temp)

def notEmpty(x):
    return x != '';


# def testPil(seisdata,seisdataMat):
#     seisMatNp = np.array(seisdata)
#     x1 = seisMatNp[:,0]
#     x2 = seisMatNp[:,1]
#     z = seisdataMat
#     x, y = meshgrid(x1, x2)
#     figure(figsize=(10, 5))
#     title("Classification using MKL")
#     c=pcolor(x, y, z)
#     _=colorbar(c)
#     return


a,b,c = seisData2Mat(seisDataDir)
r=1 #模版半径，自己自由调整
LapOpeator = np.array([[0,1,0],[1,-4,1],[0,1,0]])#laplace 算子
GBlur=MyGaussianBlur(radius=r, sigma=1)#声明高斯模糊类
GBlur1 = MyGaussianBlur(radius=r,sigma=2.0)
temp=GBlur.GaussKernelMat()#得到滤波模版
temp1= GBlur1.GaussKernelMat()
sobelX = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])#方向导数暂用sobel算子
sobelY = np.array([[1,2,1],[0,0,0],[-1,-2,1]])
resultGau1 = GBlur.Convolute(b,temp)
resultGau2 = GBlur.Convolute(b,temp1)
resultGrad  = GBlur.Convolute(b,LapOpeator)
resultX = GBlur.Convolute(b,sobelX)
resultY = GBlur.Convolute(b,sobelY)
resultDog = GBlur.diffOfGauus(resultGau1,resultGau2)
seisDataAndFeature(a,resultGau1)
bbb=1
#wellData2Mat(a)