# -*- coding: utf-8 -*-
#使用Pcolor绘制二维图
from pylab import *  
a=arange(-2.0,2.001,1.0)  
b=arange(-2.0,2.001,1.0)  
x,y=meshgrid(a,b)  
func=lambda x,y:(x**2.0+y**4.0)*exp(-x**(-2.0)-y**(-3.0))  
z=func(x,y)  
pcolor(x,y,z)  
#x和y是网格,z是(x,y)坐标处的颜色值  
colorbar()#使用颜色条  