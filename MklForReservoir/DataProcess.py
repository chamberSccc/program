# -*- coding: utf-8 -*-
import math
import numpy as np
import copy
import DataVisualize as dv

seisDataDir = 'data/seismic/seismic'
seisTestDir = 'data/seismic/testdata'
wellLogDataDir = 'data/well/welllog/data.txt' #data format:x y z per por sat wave x y z
wellTopDataDir = 'data/well/welltop.dat'
porosityGauDir = 'data/well/porosity.txt' #sequential gaussian simulation

#the longest row in irregular 2D array,which in order to entend 0 to each row
#transform |1|2| | |  to|1|2|0|0|
#          |3|4| | |    |3|4|0|0|
#the seismicMaxLenth is 4
seismicMaxLength = 100
train_well_data = []


#transform seismic data to attribute matrix
def seisData2Mat(seisDir):
    """
    Parameter
    ---------
    seisDir: seismic data path

    Returns
    -------
    data :  list_like         seis data list
    dataValue : list_like     seis attribute list
    dataCoord : list_like     seismic data's coordinate list
    """
    data = []
    dataCoord = []
    dataValue = []
    index = 0
    row = -1
    for line in open(seisDir):
        # filter the data title
        if len(line) < 40 and line[0:6] != '-99.00':
            continue
        # first meet the invalid data
        if line[0:6] == '-99.00' and index == 0:
            index += 1
            continue
        # looping in the invalid data
        if line[0:6] == '-99.00' and index != 0:
            continue
        # first end the invalid data loop
        if line[0:6] != '-99.00' and index == 1:
            index = 0;
            row += 1;
        temp = line.replace('\r','').replace('\n','').rstrip().split(' ')
        temp = filter(notEmpty, temp)
        floatTemp = [float(x) for x in temp]

        dataCoord.append(floatTemp[:2])
        dataValue.append(floatTemp[3])
        data.append(floatTemp)
    # dataDesc = dataValue[::-1]
    return data,dataValue, dataCoord

def por2array():
    porosityGaussian = []  # initial porosity label

    index = 0
    row = -1
    for line in open(porosityGauDir):
        # filter the data title
        if len(line) < 40 and line[0:6] != '-99.00':
            continue
        # first meet the invalid data
        if line[0:6] == '-99.00' and index == 0:
            index += 1
            continue
        # looping in the invalid data
        if line[0:6] == '-99.00' and index != 0:
            continue
        # first end the invalid data loop
        if line[0:6] != '-99.00' and index == 1:
            index = 0;
            row += 1;
        temp = line.replace('\r','').replace('\n','').rstrip().split(' ')
        temp = filter(notEmpty, temp)
        floatTemp = [float(x) for x in temp]
        porosityGaussian.append(floatTemp)
    # dataDesc = dataValue[::-1]
    return porosityGaussian

def attrToMat(coordList,attList):
    """
    Parameter
    ---------
    coordList: list_like coordinate list data
    attList: list_like attribute list data

    Returns
    -------
    attMat: attribute matrix according to the coordinate data range
    """
    xList,yList = dv.getXYrange(coordList)
    return xList,yList
#get well data list
def getWellData(wellDir):
    """
    Parameter
    ---------
    wellDir: well data path

    Returns
    -------
    wellList :  list_like     well data list
                dataformat is x y z permeability porosity stauration
    """
    wellList = []
    for line in open(wellLogDataDir):
        temp = line.replace('\r', '').replace('\n', '').replace('\t', ' ').rstrip().split(' ')
        temp = filter(notEmpty, temp)
        wellList.append(temp)
    return wellList

#combine well data and 15 feature
def getWellTrainData(seisMatNp,wellData):
    """
    Parameter
    ---------
    seisMatNp: array_like   seismic attribute matrix(wave impedance)
    wellData:  list_like    well data list

    Returns
    -------
    npWellData :  array_like   seis data list combined with feature
                      dataformat is x y z permeability porosity saturation 15feature
    """
    newWellData = []
    for value in wellData:
        temp = np.array(value)
        compareIndex = np.where((abs(round(float(temp[1]),6) - seisMatNp[:, 0]) <= 50.0) *
                                (abs(round(float(temp[2]),6) - seisMatNp[:, 1]) <= 50.0))
        templist = seisMatNp[compareIndex]
        # aaa = templist.size
        if templist[:,4] ==0 or templist.size ==0:
            # zeroIndex.append(wellData.index(value))
            continue
        else:
            value.extend(templist[0,4:])
            newWellData.append(value)
    npWellData = np.array(newWellData)
    return npWellData

#combine seismic data and features
def getSeisTrainData(seisData, featureMatList):
    """
    Parameter
    ---------
    seisData: list_like  seismic data list
    featureMatList:list_like   list include all feature's object(each feature is a matrix)

    Returns
    -------
    test_seis_data :  array_like    test seismic data combined with features
                dataformat is x y z permeability porosity stauration
    """
    test_seis_data = copy.deepcopy(seisData)
    xList, yList = getXYrange(np.array(seisData))
    for i in range(0,15):
        tempList = featureMatList[i]
        for j, data in enumerate(seisData):
            column = xList.index(round(seisData[j][0],6))
            row = yList.index(round(seisData[j][1],6))
            temp = tempList[row,column]
            test_seis_data[j].append(temp)
    test_seis_data = np.array(test_seis_data)
    return test_seis_data

def delZeroData(data,index):
    """
    delete the nonsense value from data(always 0 in feature data)
    Parameter
    ---------
    data: array_like   data
    index: 出现0的列数
    """
    temp1 = data[:, index]
    zeroIndex = np.where(temp1 == 0.0)
    # for x in zeroIndex:
    #     data = np.delete(data, x, axis=0)
    return data,zeroIndex

#delete '' in a list,associate with the filter function
def notEmpty(x):
    return x != '';
def getXYrange(testData):
    xData = testData[:, 0]
    yData = testData[:, 1]
    xList,yList = [],[]
    # 根据xy最小最大坐标得到网格范围
    xyList = np.array(map(roundSix, testData[:,0:2]))
    xMin, xMax = np.min(xData)-1, np.max(xData)+1
    yMin, yMax = np.min(yData)-1, np.max(yData)+1
    for i in xyList:
        if i[0] >= xMin and i[0] <= xMax and (i[0] in xList) == False:
            xList.append(i[0])
        if i[1] >= yMin and i[1] <= yMax and (i[1] in yList) == False:
            yList.append(i[1])
    xList.sort()
    yList.sort()
    return xList,yList
def roundSix(x):
    result = [round(i,6) for i in x]
    return result

