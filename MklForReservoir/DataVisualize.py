# -*- coding: utf-8 -*-
import numpy as np
import plotly.plotly
import plotly.graph_objs as go

def visualize(testData, predictedData):
    xList,yList,zList = dataTransMat(testData,predictedData)
    layout = dict(width=600, height=800)
    trace = go.Heatmap(z= zList,
                       x= xList,
                       y= yList)
    # data = [trace]
    figure = dict(data=[trace],layout=layout)
    plotly.offline.plot(figure)

def dataTransMat(testData, zValue):
    """
    trasfrom test data and z value to a spectific format,which plotly needs
    Parameter
    --------
    testData:array_like     test data
    zValue  :array_like     attribute data

    Returns
    -------
    xList: transform x value to a range(no-repeat) between xMin and xMax.
    yList: transform y value to a range(no-repeat) between yMin and yMax.
    gridList: go.Heatmap() functions param  z
    """
    xData = testData[:, 0]
    yData = testData[:, 1]
    if np.size(xData) != np.size(yData):
        return
    zData = zValue
    xyzList = [xData,yData]
    xyzList.append(zData)
    npXyzList = np.transpose(np.array(xyzList))
    npXyzList= np.array(map(roundSix,npXyzList))
    xList,yList = getXYrange(testData)
    gridList = np.zeros((len(yList),len(xList)),dtype=float)
    for xIndex,xValues in enumerate(xList):
        for yIndex,yValues in enumerate(yList):
            index = np.where((npXyzList[:,0] == xValues) * (npXyzList[:,1] == yValues))
            temp = npXyzList[index]
            if temp.size == 3:
                gridList[yIndex, xIndex] = zData[index[0]]
    return xList,yList,gridList.tolist()

def getXYrange(testData):
    """
     transform x value to a range between(no-repeat) xMin and xMax.
     transform y value to a range between(no-repeat) yMin and yMax.
    """
    xData = testData[:, 0]
    yData = testData[:, 1]
    xList,yList = [],[]
    # 根据xy最小最大坐标得到网格范围
    xyList = np.array(map(roundSix, testData[:,0:2]))
    xMin, xMax = np.min(xData), np.max(xData)
    yMin, yMax = np.min(yData), np.max(yData)
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
