# -*- coding: utf-8 -*-
import plotly.plotly
import plotly.graph_objs as go
import numpy as np

# trace = go.Heatmap(z=[[1, 20, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
#                        x=[1,2,3,4,5],
#                        y=[4,5,6])
# data = [trace]
# plotly.offline.plot(data)

a = [[1,2,3],[3,4,5]]
b= np.array(a)
index = np.where((b[:,0] == 4) * (b[:,1] == 4))
c = b[index]
print index == ()
print len(index)
print index[0] == np.array([])

# xMin,xMax = np.min(xData),np.max(xData)
    # yMin,yMax = np.min(yData),np.max(yData)
    # xLine = np.linspace(xMin,xMax,int(((xMax-xMin)/100)+1))
    # yLine = np.linspace(yMin, yMax, int(((yMax - yMin) / 100)+1))
    # x, y = pyl.meshgrid(xData, yData)
    # a = testData[:,0]
    # b = testData[:,1]
    # z = predictedData.reshape((a.size,b.size))
    # pyl.pcolor(x, y, z)
    # # x和y是网格,z是(x,y)坐标处的颜色值
    # pyl.colorbar()  # 使用颜色条
    # pyl.show()