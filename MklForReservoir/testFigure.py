# -*- coding: utf-8 -*-
#使用Pcolor绘制二维图
# from pylab import *
# a=arange(-2.0,2.001,1.0)
# b=arange(-2.0,2.001,1.0)



# x,y=meshgrid(a,b)
# func=lambda x,y:(x**2.0+y**4.0)*exp(-x**(-2.0)-y**(-3.0))
# z=func(x,y)
# pcolor(x,y,z)
# #x和y是网格,z是(x,y)坐标处的颜色值
# colorbar()#使用颜色条

import numpy as np
# aaaaa= [[[1,2],np.array([3,4])],[[1.1,2.1],np.array([3.1,4])]]
# b =  np.array(aaaaa)
# train_data = np.array([[[1,2],3,4],[[1.1,2.1],3.1,4]],dtype=float)


a = np.array([[1,2,3],[4,4,5],[4,4,5]])
b = np.where((a[:,0]==1) * (a[:,1]==2))
c = np.array([1,2,23,4,5,6,7])
print b
print len(b)
print a[b]
print len(b[0])
print a[:,1:3]
aaaa = 1