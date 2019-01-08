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
seis_train, seis_test, label_train, label_test = train_test_split(seisTrainData,labelData, test_size=0.45, random_state=42) #这里训练集75%:测试集25%

#交叉验证完之后,要区分训练特征和测试特征
train_feature = comb.detailFeature(seis_train)
test_feature = comb.detailFeature(seis_test)
all_feature = comb.detailFeature(seisTrainData)

# 得到单个mkl特征
# -----------------
xy = np.array(train_feature[0:2])
grad_1 = np.array(train_feature[2:3])
grad_2 = np.array(train_feature[3:4])
grad_3 = np.array(train_feature[4:5])
dirx_1 = np.array(train_feature[5:6])
dirx_2 = np.array(train_feature[6:7])
dirx_3 = np.array(train_feature[7:8])
dog_1 = np.array(train_feature[11:12])
dog_2 = np.array(train_feature[12:13])
dog_3 = np.array(train_feature[13:14])

xy_all = np.array(all_feature[0:2])
grad_1_all = np.array(all_feature[2:3])
grad_2_all = np.array(all_feature[3:4])
grad_3_all = np.array(all_feature[4:5])
dirx_1_all = np.array(all_feature[5:6])
dirx_2_all = np.array(all_feature[6:7])
dirx_3_all = np.array(all_feature[7:8])
dog_1_all = np.array(all_feature[11:12])
dog_2_all = np.array(all_feature[12:13])
dog_3_all = np.array(all_feature[13:14])

# shogun需要的训练特征格式
xy_train = shogun.RealFeatures(xy)
grad_1_train = shogun.RealFeatures(grad_1)
grad_2_train = shogun.RealFeatures(grad_2)
grad_3_train = shogun.RealFeatures(grad_3)
dirx_1_train = shogun.RealFeatures(dirx_1)
dirx_2_train = shogun.RealFeatures(dirx_2)
dirx_3_train = shogun.RealFeatures(dirx_3)
dog_1_train = shogun.RealFeatures(dog_1)
dog_2_train = shogun.RealFeatures(dog_2)
dog_3_train = shogun.RealFeatures(dog_3)

# shogun需要的特征格式,测试特征
xy_sgall = shogun.RealFeatures(xy_all)
grad_1_sgall = shogun.RealFeatures(grad_1_all)
grad_2_sgall = shogun.RealFeatures(grad_2_all)
grad_3_sgall = shogun.RealFeatures(grad_3_all)
dirx_1_sgall = shogun.RealFeatures(dirx_1_all)
dirx_2_sgall = shogun.RealFeatures(dirx_2_all)
dirx_3_sgall = shogun.RealFeatures(dirx_3_all)
dog_1_sgall = shogun.RealFeatures(dog_1_all)
dog_3_sgall = shogun.RealFeatures(dog_3_all)
dog_2_sgall = shogun.RealFeatures(dog_2_all)


train_combine = shogun.CombinedFeatures()
test_combine = shogun.CombinedFeatures()
all_combine = shogun.CombinedFeatures()
combined_kernel = shogun.CombinedKernel()

width =[1,1,1,1,1.5,1.5,1.5,1.5,1.5,1.5]
# 坐标特征
gauss_kernel_1 = shogun.GaussianKernel(width[0])
train_combine.append_feature_obj(xy_train)
all_combine.append_feature_obj(xy_sgall)
combined_kernel.append_kernel(gauss_kernel_1)

# 梯度特征
gauss_kernel_2 = shogun.GaussianKernel(width[1])
train_combine.append_feature_obj(grad_1_train)
all_combine.append_feature_obj(grad_1_sgall)
combined_kernel.append_kernel(gauss_kernel_2)

gauss_kernel_3 = shogun.GaussianKernel(width[2])
train_combine.append_feature_obj(grad_2_train)
all_combine.append_feature_obj(grad_2_sgall)
combined_kernel.append_kernel(gauss_kernel_3)

gauss_kernel_4 = shogun.GaussianKernel(width[3])
train_combine.append_feature_obj(grad_3_train)
all_combine.append_feature_obj(grad_3_sgall)
combined_kernel.append_kernel(gauss_kernel_4)

# 方向倒数x特征
gauss_kernel_5 = shogun.GaussianKernel(width[4])
train_combine.append_feature_obj(dirx_1_train)
all_combine.append_feature_obj(dirx_1_sgall)
combined_kernel.append_kernel(gauss_kernel_5)

gauss_kernel_6 = shogun.GaussianKernel(width[5])
train_combine.append_feature_obj(dirx_2_train)
all_combine.append_feature_obj(dirx_2_sgall)
combined_kernel.append_kernel(gauss_kernel_6)

gauss_kernel_7 = shogun.GaussianKernel(width[6])
train_combine.append_feature_obj(dirx_3_train)
all_combine.append_feature_obj(dirx_3_sgall)
combined_kernel.append_kernel(gauss_kernel_7)

# dog特征
gauss_kernel_8 = shogun.GaussianKernel(width[7])
train_combine.append_feature_obj(dog_1_train)
all_combine.append_feature_obj(dog_1_sgall)
combined_kernel.append_kernel(gauss_kernel_8)

gauss_kernel_9 = shogun.GaussianKernel(width[8])
train_combine.append_feature_obj(dog_2_train)
all_combine.append_feature_obj(dog_2_sgall)
combined_kernel.append_kernel(gauss_kernel_9)

gauss_kernel_10 = shogun.GaussianKernel(width[9])
train_combine.append_feature_obj(dog_3_train)
all_combine.append_feature_obj(dog_3_sgall)
combined_kernel.append_kernel(gauss_kernel_10)
# gauss_kernel_11 = shogun.GaussianKernel(27.0)
# gauss_kernel_12 = shogun.GaussianKernel(30.0)
# gauss_kernel_13 = shogun.GaussianKernel(32.0)
# combined_kernel.append_kernel(gauss_kernel_11)
# combined_kernel.append_kernel(gauss_kernel_12)
# combined_kernel.append_kernel(gauss_kernel_13)


combined_kernel.init(train_combine, train_combine)


svr_solver = shogun.SVRLight()
mkl = shogun.MKLRegression(svr_solver)
# mkl.set_mkl_norm(1)
# mkl.set_C(1, 1)
mkl.set_kernel(combined_kernel)
mkl.set_labels(shogun.RegressionLabels(label_train))
mkl.set_epsilon(0.1)
# mkl.set_mkl_epsilon(0.2)
# mkl.set_C_mkl(10)
mkl.train()

# trainMkl(combined_kernel,mkl,combined_all_feature)
beta = combined_kernel.get_subkernel_weights()
alpha = mkl.get_alphas()
print(beta)

combined_kernel.init(train_combine,all_combine)
labels_predict = mkl.apply_regression()
predit_porosity = labels_predict.get_labels()
##############
#测试剔除无效数据
##############
# zeroList = np.array(zeroList[0]);
# seisTrainData = np.concatenate((seisTrainData, zeroList),axis=0);
# zeroLabel = np.array(zeroLabel[0]);
# predit_porosity = np.append(predit_porosity,zeroLabel);
dv.visualize(seisTrainData, predit_porosity)
# dv.visualize(seisTrainData, seisTrainData[:,3])
#0:gaussion_r1  1:gaussion_r2  2:gaussion_r4
#3:grad_r1   4:grad_r2   5:grad_r4  6-11 direction_r1_r2_r4_x_y
#12:dog_r2_r1   13:dog_r4_r2   14:dog_r8_r6
# dv.visualizeFeature(seisTrainData,featureList[2])
aaa =  1

