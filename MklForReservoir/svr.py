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
# 序贯高斯模拟孔隙度数据
porosity_gauList = dp.por2array()
#现在需要根据seisTrainData的坐标值,得到对应的label
seisTrainData,labelData = comb.combinDataAndFeature(seisDataList,wellLogList,featureList,porosity_gauList)

##########  9.11测试
# 把地震数据中 特征值为0的值剔除出来
##########
# zeroData = seisTrainData[:,4]
# test = seisTrainData[:,3]
# zeroIndex = np.where(zeroData == 0)
# zeroList = []
# zeroLabel = []
# for i in zeroIndex:
#     zeroList.append(seisTrainData[i, :])
#     zeroLabel.append(labelData[i])
#     seisTrainData = np.delete(seisTrainData, i, axis=0)
#     labelData = np.delete(labelData, i, axis=0)

# predit_porosity = np.concatenate(predit_porosity,zeroLabel);
# dv.visualize(seisTrainData, predit_porosity)

# skf = KFold(n_splits=2)
##############
# #数据交叉验证区分训练数据和测试数据
##############
# skf = StratifiedKFold(n_splits=2)
# for train_index, test_index in skf.split(seisTrainData,labelData):
#     seis_train, seis_test = seisTrainData[train_index], seisTrainData[test_index]
#     label_train, label_test = labelData[train_index], labelData[test_index]
#

# data (全部数据)   labels(全部目标值)     X_train 训练集(全部特征)  Y_train 训练集的目标值
seis_train, seis_test, label_train, label_test = train_test_split(seisTrainData,labelData, test_size=0.25, random_state=0) #这里训练集75%:测试集25%

#交叉验证完之后,要区分训练特征和测试特征
train_feature = comb.detailFeature(seis_train)
test_feature = comb.detailFeature(seis_test)
all_feature = comb.detailFeature(seisTrainData)
labels_train = shogun.RegressionLabels(label_train)

# 得到单个mkl特征
# -----------------
# combined_Train_sgFeature = pMkl.getShogunFeature(train_feature[0:2])
# combined_Test_sgFeature = pMkl.getShogunFeature(test_feature[0:2])
# combined_all_feature = pMkl.getShogunFeature(all_feature[0:2])
temp_train = np.array(train_feature[0:20])
temp_test = np.array(test_feature[0:20])
temp_all = np.array(all_feature[0:20])
combined_Train_sgFeature = shogun.RealFeatures(temp_train)
combined_Test_sgFeature = shogun.RealFeatures(temp_test)
combined_all_feature = shogun.RealFeatures(temp_all)
width = 5.0
kernel = shogun.GaussianKernel(width)
svm_c = 2.0
svr_param = 0.1
svr = shogun.LibSVR(svm_c, svr_param, kernel, labels_train, shogun.LIBSVR_EPSILON_SVR)
svr.train(combined_Train_sgFeature)
labels_predict = svr.apply_regression(combined_all_feature)
predit_porosity = labels_predict.get_labels()
dv.visualize(seisTrainData, predit_porosity)
# dv.visualize(seisTrainData, seisTrainData[:,3])
#0:gaussion_r1  1:gaussion_r2  2:gaussion_r4
#3:grad_r1   4:grad_r2   5:grad_r4  6-11 direction_r1_r2_r4_x_y
#12:dog_r2_r1   13:dog_r4_r2   14:dog_r8_r6
# dv.visualizeFeature(seisTrainData,featureList[2])
aaa =  1

