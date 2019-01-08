# -*- coding: utf-8 -*-
import CombinDataAndFeature as comb
import PreMklSingleFeature as pMkl
import numpy as np
import DataVisualize as dv
import DataProcess as dp
import utility as util
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
import modshogun as shogun


def trainMkl(kernel,mkl,trainFeature):
    kernel.init(trainFeature, trainFeature)
    mkl.train()


wellLogList = dp.getWellData(dp.wellLogDataDir)
# 地震数据转为矩阵数据
seisDataList, waveList, seisCoord  = dp.seisData2Mat(dp.seisDataDir)
# 属性矩阵 真实地形形状
waveMat= util.dataTransMat(np.array(seisCoord),np.array(waveList))
npwavemat = np.array(waveMat)
# 通过波阻抗矩阵得到
featureList =  comb.generateFeatureMat(npwavemat)
npFeature = np.array(featureList);
# 序贯高斯模拟孔隙度数据
porosity_gauList = dp.por2array()
#现在需要根据seisTrainData的坐标值,得到对应的label
seisTrainData,labelData = comb.combinDataAndFeature(seisDataList,wellLogList,featureList,porosity_gauList)

dv.visualize(seisTrainData, seisTrainData[:,9])
# 从3开始
#3:gaussion_r1  4:gaussion_r2  5:gaussion_r4
#6:grad_r1   7:grad_r2   8:grad_r4  9-14 direction_r1_r2_r4_x_y
#15:dog_r2_r1   16:dog_r4_r2   17:dog_r8_r6
# dv.visualizeFeature(seisTrainData,featureList[2])
aaa =  1

