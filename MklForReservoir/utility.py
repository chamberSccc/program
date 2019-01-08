# -*- coding: utf-8 -*-
import numpy as np
#（二维）将预测数据与坐标鼠标转为 plotly所需要的网格数据 x一维 y一维 z对应值
def dataTransMat(coordData, zValue):
    xData = coordData[:, 0]
    yData = coordData[:, 1]
    if np.size(xData) != np.size(yData):
        return
    zData = zValue
    xyzList = [xData,yData]
    xyzList.append(zData)
    npXyzList = np.transpose(np.array(xyzList))
    npXyzList= np.array(map(roundSix,npXyzList))
    xList,yList = getXYrange(coordData)
    gridList = np.zeros((len(yList),len(xList)),dtype=float)
    for xIndex,xValues in enumerate(xList):
        for yIndex,yValues in enumerate(yList):
            index = np.where((npXyzList[:,0] == xValues) * (npXyzList[:,1] == yValues))
            temp = npXyzList[index]
            if temp.size == 3:
                gridList[yIndex, xIndex] = zData[index[0]]
    return gridList.tolist()
#得到x y坐标不重复排列
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