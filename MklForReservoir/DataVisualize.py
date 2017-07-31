# -*- coding: utf-8 -*-
import plotly.plotly
import plotly.graph_objs as go
import utility as util

def visualize(xyData, predictedData):
    xList,yList = util.getXYrange(xyData)
    zList = util.dataTransMat(xyData, predictedData)
    layout = dict(width=600, height=800)
    trace = go.Heatmap(z= zList,
                       x= xList,
                       y= yList)
    # data = [trace]
    figure = dict(data=[trace],layout=layout)
    plotly.offline.plot(figure)

