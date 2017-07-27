# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 14:30:30 2017

@author: xiaonizi
"""

# 利用matplotlib画直方图

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.cross_validation import cross_val_score

line = pd.read_csv(os.getcwd() + "//sung15-16.csv")
#line = pd.read_csv('F:\Practeam\Pteam\TrainingData\sung15-16.csv')
#line.plot.density(figsize=(6, 49), subplots=True, yticks=[])

lines = pd.DataFrame(line)
x = lines.ix[0: , 3: ]
#x = lines[['x1','x2']]
#y = lines["y"]
y = lines.ix[0: ,[2,]]

x = x.fillna(0)
y = y.fillna(0)

x = x.values[:, :]
y = y.values[:, :]


plt.bar(range(len(x)), y)
plt.xlabel('x')
plt.ylabel('y')
##plt.xticks(range(len(x)), y )
##plt.yticks(range(len(x)), y)
plt.show() 

from sklearn.decomposition import PCA
#print(x.shape)

pca = PCA()#  创建PCA实例
x = pd.DataFrame(x) #创建dataFrame ->交叉检验
x_scaled_pca = pd.DataFrame(pca.fit_transform(x), columns = x.columns)#x降维 转为dataframe对象

v = pca.explained_variance_ratio_
vc = v.cumsum()
# DataFrame(list(zip(it.count)))


n_comps = 1 + np.argmax(vc > 0.95)

x_scaled_pca = x_scaled_pca.ix[:, :n_comps]


y = pd.DataFrame(y)
x_pca = pd.concat([x_scaled_pca, y], axis = 1)
x = x_pca
#print(x)



x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size = 0.3, random_state = 0)
    
    
dtr = DecisionTreeRegressor()

cross_val_score(dtr, x_train, y_train, cv = 10).mean()

dtr = dtr.fit(x_train, y_train)
y_predict = dtr.predict(x_test)
y_test = y_test.values[:, :]

sum1 = 0

for i in range(len(y_predict)):
    sum1 = sum1 + abs(y_predict[i]-y_test[i])
    print(y_test[i],'   ',y_predict[i]) 

print("The totol error is", sum1)
print("The average error is", sum1/len(y_test))
print(len(y_test),len(y_train))    


plt.title("The Error of the Model----DecisionTreeRegressor")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(y_test, 'r')
plt.plot(y_predict, 'g')
plt.show()








