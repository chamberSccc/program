# -*- coding: utf-8 -*-
import math
import numpy as np
import copy
import DataVisualize as dv

seisDataDir = 'data/seismic/seismic'
seisTestDir = 'data/seismic/testdata'
wellLogDataDir = 'data/well/welllog/data.txt' #x y z shen kong bao bozukang x y z
wellTopDataDir = 'data/well/welltop.dat'

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
    tempDataValue = []
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
    return
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
    for i in wellData:
        temp = np.array(i)
        compareIndex = np.where(abs(float(temp[1]) - seisMatNp[:, 0]) <= 50.0 * (abs(float(temp[2]) - seisMatNp[:, 1]) <=50.0))
        templist = seisMatNp[compareIndex]

        if len(compareIndex[0]) != 0:
            i.extend(templist[0,:])
        else:
            pass
    npWellData = np.array(wellData)
    temp1 = npWellData[:,7]
    zeroIndex = np.where(temp1=='0.0')

    #特征计算过程中会出现0,暂且认为是脏数据
    for x in zeroIndex:
        npWellData = np.delete(npWellData,x,axis=0)
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
    for i in range(0,15):
        tempList = featureMatList[i]
        for j, data in enumerate(seisData):
            temp = tempList[int(j / 100), j % 100]
            test_seis_data[j].append(temp)
    test_seis_data = np.array(test_seis_data)
    return test_seis_data

def delZeroData(data, index):
    """
    delete the nonsense value from data(always 0 in feature data)
    Parameter
    ---------
    data: array_like   data
    index: int    column which first appear 0
    """
    temp1 = data[:, 4]
    zeroIndex = np.where(temp1 == 0.0)
    for x in zeroIndex:
        data = np.delete(data, x, axis=0)
    return data

#delete '' in a list,associate with the filter function
def notEmpty(x):
    return x != '';

