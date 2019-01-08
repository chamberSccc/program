# -*- coding: utf-8 -*-
import CombinDataAndFeature as comb
import PreMklProcess as pMkl
import numpy as np
import DataVisualize as dv
import DataProcess as dp
import utility as util
from sklearn.model_selection import KFold
import modshogun as shogun
from sklearn.model_selection import StratifiedKFold

wellLogList = dp.getWellData(dp.wellLogDataDir)
# 地震数据转为矩阵数据
seisDataList, waveList, seisCoord  = dp.seisData2Mat(dp.seisDataDir)
# 属性矩阵 真实地形形状
waveMat= util.dataTransMat(np.array(seisCoord),np.array(waveList))
npwavemat = np.array(waveMat)
featureList =  comb.generateFeatureMat(npwavemat)
# 序贯高斯模拟孔隙度数据
porosity_gauList = dp.por2array()
#到此为止,过滤掉了所有的脏数据 17820行数据只剩下5240行数据,
#现在需要根据seisTrainData的坐标值,得到对应的label
seisTrainData,labelData = comb.combinDataAndFeature(seisDataList,wellLogList,featureList,porosity_gauList)
# skf = KFold(n_splits=2)
skf = StratifiedKFold(n_splits=2)
#数据交叉验证区分训练数据和测试数据
for train_index, test_index in skf.split(seisTrainData,labelData):
    seis_train, seis_test = seisTrainData[train_index], seisTrainData[test_index]
    label_train, label_test = labelData[train_index], labelData[test_index]

#交叉验证完之后,要区分训练特征和测试特征
train_feature = comb.detailFeature(seis_train)
test_feature = comb.detailFeature(seis_test)
all_feature = comb.detailFeature(seisTrainData)

# 得到多个mkl特征
# -----------------
# combined_Train_sgFeature = pMkl.getShogunFeature(train_feature)
# combined_Test_sgFeature = pMkl.getShogunFeature(test_feature)
# combined_all_feature = pMkl.getShogunFeature(all_feature)
temp_train = np.array(train_feature[0:15])
temp_test = np.array(test_feature[0:15])
temp_all = np.array(all_feature[0:15])
combined_Train_sgFeature = shogun.RealFeatures(temp_train)
combined_Test_sgFeature = shogun.RealFeatures(temp_test)
combined_all_feature = shogun.RealFeatures(temp_all)
kernelWidthList = [1.0,2.1,1.1,1.2,1.5,0.8,2.2,2.1,
                   1.5,2.0,1.8,2.4,1.3,1.6,1.4,1.6]#kernel width param list
combined_kernel = pMkl.getCombinKernel(kernelWidthList,combined_Train_sgFeature,combined_Train_sgFeature)
# -----------------

# 得到用于训练的MKL实例
mkl = pMkl.getMkl(combined_kernel, label_train)
combined_kernel.init(combined_Train_sgFeature, combined_Train_sgFeature)
mkl.train()
beta = combined_kernel.get_subkernel_weights()
alpha = mkl.get_alphas()
print(beta)

# mkl训练完之后,预测值
combined_kernel_t = pMkl.getCombinKernel(kernelWidthList,combined_Train_sgFeature,combined_all_feature)
combined_kernel_t.init(combined_Train_sgFeature,combined_all_feature)
# 训练完之后重新传入核函数映射
mkl.set_kernel(combined_kernel_t)
labels_predict = mkl.apply()
predit_porosity = labels_predict.get_labels()
# temp = np.array(porosity_gauList)[:,3]
dv.visualize(seisTrainData, predit_porosity)
# dv.visualize(seisTrainData, seisTrainData[:,3])
#0:gaussion_r1  1:gaussion_r2  2:gaussion_r4
#3:grad_r1   4:grad_r2   5:grad_r4  6-11 direction_r1_r2_r4_x_y
#12:dog_r2_r1   13:dog_r4_r2   14:dog_r8_r6
# dv.visualizeFeature(seisTrainData,featureList[2])
aaa =  1

