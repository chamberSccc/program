# -*- coding: utf-8 -*-
import math
import numpy as np
import copy

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
        temp = filter(notEmpty, temp)
        floatTemp = [float(x) for x in temp]

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
        temp = line.replace('\r', '').replace('\n', '').replace('\t', ' ').rstrip().split(' ')
        temp = filter(notEmpty, temp)
        wellList.append(temp)
    return wellList

#组合测井数据与15种特征 x y z per por sat 15features
def getWellTrainData(seisMatNp,wellData):
    # f = open('data/well/welllog/result.txt', 'w')
    for i in wellData:
        temp = np.array(i)
        compareIndex = np.where(abs(float(temp[1]) - seisMatNp[:, 0]) <= 50.0 * (abs(float(temp[2]) - seisMatNp[:, 1]) <=50.0))
        templist = seisMatNp[compareIndex]

        if len(compareIndex[0]) != 0:
            i.extend(templist[0,:])
        else:
            pass
        # f.write(''.join([str(v)+' ' for v in temp])+'\n')
    # f.close()
    npWellData = np.array(wellData)
    temp1 = npWellData[:,7]
    zeroIndex = np.where(temp1=='0.0')
    #特征计算过程中会出现0,暂且认为是脏数据
    for x in zeroIndex:
        npWellData = np.delete(npWellData,x,axis=0)
    return npWellData

#组合地震数据与15种特征
def getSeisTrainData(seisData, featureMatList):
    train_seis_data = copy.deepcopy(seisData)
    for i in range(0,15):
        tempList = featureMatList[i]
        for j, data in enumerate(seisData):
            temp = tempList[int(j / 100), j % 100]
            train_seis_data[j].append(temp)

    return np.array(train_seis_data)
#组合矩阵中每行数据不足的地方补0,每行最多为seismicMaxlength
def extend0Toarray(x):
    temp = [0 for i in range(0, seismicMaxLength - len(x))]
    x.extend(temp)
#删除地震训练数据中特征为0的行
def delZeroFromSeisTrain(seisTrainData):
    temp1 = seisTrainData[:,4]
    zeroIndex = np.where(temp1 == 0.0)
    for x in zeroIndex:
        seisTrainData = np.delete(seisTrainData,x,axis=0)
    return seisTrainData
#消除数组中'',配合filter使用
def notEmpty(x):
    return x != '';

