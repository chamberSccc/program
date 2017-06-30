# -*- coding: utf-8 -*-
import math
import numpy as np
import cv2 as cv

dataDir = 'data/wave impedance'
testDir = 'data/testdata'


def data2Mat(dataDir):
    data = []
    dataCoord = []
    dataValue = []
    tempDataValue = []
    index = 0
    row = 0
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

        temp = line.strip('\r\n').rstrip().split(' ')
        floatTemp = [float(x) for x in temp]
        tempDataValue.append(floatTemp[3])
        dataCoord.append(floatTemp[:2])
        floatTemp.pop(2)
        data.append(floatTemp)

    dataValue.append(tempDataValue)
    dataDesc = np.array(dataValue)[::-1]
    img_kernel1 = cv.GaussianBlur(dataDesc, (5,5), 1)
    a = 1
    return data, dataValue, dataCoord


def GaussionFormula(x, sigma=1):
    return


def GaussianSmooth(data):
    return


data2Mat(dataDir)
