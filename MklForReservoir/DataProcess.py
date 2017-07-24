# -*- coding: utf-8 -*-
# from matplotlib import *
# from pylab import *
import math
import numpy as np
import copy
import cv2 as cv
from CalcOperator import MyGaussianBlur
import os

seisDataDir = 'data/seismic/seismic'
seisTestDir = 'data/seismic/testdata'
wellLogDataDir = 'data/well/welllog/data.txt' #x y z shen kong bao bozukang x y z
wellTopDataDir = 'data/well/welltop.dat'
seismicMaxLength = 100  # 二维数组每行长度不等时计算出最长的那行,数据预处理的时候得到的值，当做全局变量处理，不必在程序中展现
train_well_data = []

#返回完整地震数据矩阵(data),网格排列波阻抗矩阵(dataValue)，坐标矩阵(dataCoord)
def seisData2Mat(seisDir):
    data = []
    dataCoord = []
    dataValue = []
    tempDataValue = []
    index = 0
    row = -1
    for line in open(seisDir):
        # filter the data title
        if len(line) < 40 and line[0:6] != '-99.00':
            continue
        # 第一次碰到非法数据
        if line[0:6] == '-99.00' and index == 0:
            index += 1
            continue
        # 正在非法数据循环中
        if line[0:6] == '-99.00' and index != 0:
            continue
        # 第一次结束非法数据循环
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

#x y z per por sat 解析测井数据
def getWellData(wellDir):
    wellList = []
    for line in open(wellLogDataDir):
        temp = line.replace('\r', '').replace('\n', '').replace('"', '').replace('\t', '').rstrip().split(' ')
        temp = filter(notEmpty, temp)
        wellList.append(temp)
    return wellList

#组合测井数据与16种特征 x y z per por sat 16features
def getWellTrainData(seisdataMat,wellData):
    resultList = []
    seisMatNp = np.array(seisdataMat)
    # f = open('data/well/welllog/result.txt', 'w')
    for i in wellData:
        compare = (abs(float(i[1]) - seisMatNp[:, 0]) <= 50.0) & (abs(float(i[2]) - seisMatNp[:, 1]) <= 50.0)
        # x = np.extract(compare,seisMatNp[:,0])
        # y = np.extract(compare, seisMatNp[:,1])
        # z = np.extract(compare, seisMatNp[:,2])
        wave = np.extract(compare, seisMatNp[:,3])
        if wave.size == 0:
           pass
        else:
            i.extend(wave[0])
        # resultList.append(i)
        # f.write(''.join([str(v)+' ' for v in temp])+'\n')
    # f.close()
    #组合特征数据格式
    return

#组合地震数据与16种特征
def getSeisTrainData(seisData,featureList):
    train_seis_data = copy.deepcopy(seisData)
    for i in range(0,16):
        tempList = featureList[i]
        for j, data in enumerate(seisData):
            temp = tempList[int(j / 100), j % 100]
            train_seis_data[j].append(temp)
    return np.array(train_seis_data)
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

#先得到测井数据列表
wellLogList = getWellData(wellLogDataDir)
#解析地震数据
seisDataList, waveMat, seisCoord  = seisData2Mat(seisDataDir)

#构造15种特征数据
#1：DOG R2和R1  R4和R2  R8和R6
#2：Grad R1 R2 R4
#3：Dir Y1 Y2 Y4 X1 X2 X4
#4 Smooth R1 R2 R4

r=1 #模版半径，自己自由调整
LapOpeator = np.array([[0,1,0],[1,-4,1],[0,1,0]])#laplace 算子
sobelX = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])#方向导数暂用sobel算子
sobelY = np.array([[1,2,1],[0,0,0],[-1,-2,1]])

GBlur_R1=MyGaussianBlur(radius=r, sigma=1.0)#声明高斯模糊类
GBlur_R2 = MyGaussianBlur(radius=r, sigma=2.0)
GBlur_R4 = MyGaussianBlur(radius=r, sigma=4.0)
GBlur_R6 = MyGaussianBlur(radius=r, sigma=6.0)
GBlur_R8 = MyGaussianBlur(radius=r, sigma=8.0)
R1_Template=GBlur_R1.GaussKernelMat()#得到滤波模版
R2_Template= GBlur_R2.GaussKernelMat()
R4_Template= GBlur_R2.GaussKernelMat()
R6_Template= GBlur_R2.GaussKernelMat()
R8_Template= GBlur_R2.GaussKernelMat()

Gaus_R1 = GBlur_R1.Convolute(waveMat, R1_Template)#15种特征,高斯模糊
Gaus_R2 = GBlur_R2.Convolute(waveMat,R2_Template)
Gaus_R4 = GBlur_R4.Convolute(waveMat,R4_Template)
Gaus_R6 = GBlur_R6.Convolute(waveMat,R6_Template)
Gaus_R8 = GBlur_R8.Convolute(waveMat,R8_Template)
Grad_R1  = GBlur_R1.Convolute(waveMat,LapOpeator)#梯度
Grad_R2  = GBlur_R2.Convolute(waveMat,LapOpeator)
Grad_R4  = GBlur_R4.Convolute(waveMat,LapOpeator)
Dir_X_R1 = GBlur_R1.Convolute(waveMat,sobelX)#方向倒数
Dir_X_R2 = GBlur_R2.Convolute(waveMat,sobelX)
Dir_X_R4 = GBlur_R4.Convolute(waveMat,sobelX)
Dir_Y_R1 = GBlur_R1.Convolute(waveMat,sobelY)
Dir_Y_R2 = GBlur_R2.Convolute(waveMat,sobelY)
Dir_Y_R4 = GBlur_R4.Convolute(waveMat,sobelY)
Dog_R2_R1 = GBlur_R1.diffOfGauus(Gaus_R1,Gaus_R2)#高斯差分
Dog_R4_R2 = GBlur_R1.diffOfGauus(Gaus_R2,Gaus_R4)
Dog_R8_R6 = GBlur_R1.diffOfGauus(Gaus_R6,Gaus_R8)
list = [Gaus_R1,Gaus_R2,Gaus_R4,Gaus_R6,Gaus_R8,Grad_R1,Grad_R2,Grad_R4,Dir_X_R1,Dir_X_R2,Dir_X_R4,
        Dir_Y_R1,Dir_Y_R2,Dir_Y_R4,Dog_R2_R1,Dog_R4_R2,Dog_R8_R6]
#将地震数据加入15种特征数据
train_seis_data = getSeisTrainData(seisDataList, list)
#将测井数据转换为训练数据格式，并方便加入16种特征数据
getWellTrainData(wellLogList,seisDataList)
bbb=1
#wellData2Mat(a)