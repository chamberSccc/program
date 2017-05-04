# -*- coding: utf-8 -*-
import  numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from sklearn import svm

train_data_path = 'file/Porosity_Training.dat'
test_data_path = 'file/Porosity_Validation.dat'

#解析孔隙度数据为矩阵
def dataProcess(dataPath):
    dataMat = []
    x= []
    y= []
    dataValue = []
    index = 0
    for line in open(dataPath):
        if len(line) < 50:
            pass
        else:
            temp = line.strip(' \n').split(" ")
            dataValue.append(temp[3])#孔隙度值
            dataMat.append(temp[0:2])
            x.append(temp[0])#X坐标值
            y.append(temp[1])#Y坐标值
            index = index + 1
    return dataMat,dataValue,x,y

#创建SVR模型
def creatSVR(dataMat,dataValue):
    clf = svm.SVR(kernel='rbf')
    clf.fit(dataMat,dataValue)
    return clf

#展示SVR模型
def showData(trainX,trainY,testX,preY,support_vector=None):
    support_X = []
    support_Y = []
    plt.figure()
    plt.axis([0, 1, 0, 1])
    plt.scatter(trainX, trainY, color='darkorange', label='train')
    plt.grid()
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(0.1))
    ax.yaxis.set_major_locator(MultipleLocator(0.1))
    if support_vector is not None:
        for x,y in support_vector:
            support_X.append(x)
            support_Y.append(y)
    lw = 2
    plt.scatter(support_X, support_Y, color='navy', label='support_vector')
    plt.plot(testX, preY, color='r', lw=lw, label='super plane')
    #plt.legend()
    plt.show()
    return


if __name__ == '__main__':
    trainMat,trainValue,trainX,trainY = dataProcess(train_data_path)
    testMat, testValue, testX, testY = dataProcess(test_data_path)
    clf = creatSVR(trainMat,trainValue)
    preY = clf.predict(testMat)
    showData(trainX,trainY,testX,preY,clf.support_vectors_)