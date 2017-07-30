# -*- coding: utf-8 -*-
import numpy as np
import plotly.plotly
import plotly.graph_objs as go
#plotly 画图软件
def visualize(testData, predictedData):
    xList,yList,zList = dataTransMat(testData,predictedData)
    layout = dict(width=600, height=800)
    trace = go.Heatmap(z= zList,
                       x= xList,
                       y= yList)
    # data = [trace]
    figure = dict(data=[trace],layout=layout)
    plotly.offline.plot(figure)

#（二维）将预测数据与坐标鼠标转为 plotly所需要的网格数据 x一维 y一维 z二维
def dataTransMat(testData,predictedData):
    xData = testData[:, 0]
    yData = testData[:, 1]
    zData = predictedData
    xyzList = []
    xyzList.append(xData)
    xyzList.append(yData)
    xyzList.append(zData)
    npXyzList = np.transpose(np.array(xyzList))
    npXyzList= np.array(map(roundSix,npXyzList))
    if np.size(xData) != np.size(yData):
        return
    xMin,xMax = np.min(xData),np.max(xData)
    yMin,yMax = np.min(yData),np.max(yData)
    tempXList,tempYList = [],[]
    #根据xy最小最大坐标得到网格范围
    for i in npXyzList:
        if i[0]>=xMin and i[0]<=xMax and (i[0] in tempXList) == False:
            tempXList.append(i[0])
        if i[1]>=yMin and i[1]<=yMax and (i[1] in tempYList) == False:
            tempYList.append(i[1])
    tempXList.sort()
    tempYList.sort()
    #网格中填充Z值
    gridList = np.zeros((len(tempYList),len(tempXList)),dtype=float)
    for xIndex,xValues in enumerate(tempXList):
        for yIndex,yValues in enumerate(tempYList):
            index = np.where((npXyzList[:,0] == xValues) * (npXyzList[:,1] == yValues))
            temp = npXyzList[index]
            if temp.size == 3:
                gridList[yIndex, xIndex] = zData[index[0]]
    return tempXList,tempYList,gridList.tolist()

def roundSix(x):
    result = [round(i,6) for i in x]
    return result
