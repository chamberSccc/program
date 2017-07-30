# -*- coding: utf-8 -*-
import CombinDataAndFeature as comb
import PreMklProcess as pMkl
import numpy as np
import  DataVisualize as dv


featureList =  comb.generateFeatureMat()
wellTrainData ,seisTrainData = comb.combinDataAndFeature(comb.seisDataList,comb.wellLogList,featureList)
wellFeatureDataList,seisFeatureDataList = comb.detailFeature(wellTrainData ,seisTrainData)

#测井数据训练
kernelWidthList = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,
                   1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,]#核宽度参数
combined_kernel = pMkl.getCombinKernel(kernelWidthList,wellFeatureDataList)#组合核函数
combined_Train_sgFeature = pMkl.getShogunFeature(wellFeatureDataList)#第一次组合测井训练数据
combined_Test_sgFeature = pMkl.getShogunFeature(seisFeatureDataList)#第一次组合地震测试数据
#孔隙度与渗透率训练标签
porosity_Well = np.array(wellTrainData[:,5])
permeability_Well = np.array(wellTrainData[:,4])

mkl = pMkl.getMkl(combined_kernel, porosity_Well)
combined_kernel.init(combined_Train_sgFeature, combined_Train_sgFeature)
mkl.train()#训练MKL
beta = combined_kernel.get_subkernel_weights()
alpha = mkl.get_alphas()


combined_kernel.init(combined_Train_sgFeature, combined_Test_sgFeature)
labels_predict = mkl.apply_regression()
predit_porosity = labels_predict.get_labels()
dv.visualize(seisTrainData, predit_porosity)
aaa =  1

