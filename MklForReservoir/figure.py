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
