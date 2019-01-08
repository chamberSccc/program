# -*- coding: utf-8 -*-
import numpy as np
from sklearn.cross_validation import train_test_split
import os
SHOGUN_DATA_DIR=os.getenv('SHOGUN_DATA_DIR', '../../../data')
import modshogun as shogun


def getCombinKernel(kernelWidth, trainDataList, predictList):
    """
    Get combined kernel function instance
    Parameter
    ---------
    kernelWidth: list_like kernel width param list for each kernel
    TrainDataList: feature data list
                   data format:[feature1,feature2,feature3......]
    """
    sgTrainDataList = trainDataList
    sgPredictList = predictList
    # 把特征数据中不是nparray的数据,转为具有维度的nparray数据
    # for x in trainDataList:
    #     dimen = x.shape
    #     if len(dimen) == 1:
    #         temp = x.reshape((-1, x.size))
    #     else:
    #         temp = x
    #     sgTrainDataList.append(shogun.RealFeatures(temp))
    #
    # for v in predictList:
    #     dimenv = v.shape
    #     if len(dimenv) == 1:
    #         tempv = v.reshape((-1, v.size))
    #     else:
    #         tempv = v
    #     sgPredictList.append(shogun.RealFeatures(tempv))
    kernel_X_Y = shogun.GaussianKernel(sgTrainDataList, sgPredictList, kernelWidth[0])
    kernel_Gau_R1 = shogun.GaussianKernel(sgTrainDataList, sgPredictList, kernelWidth[1])
    kernel_Gau_R2 = shogun.GaussianKernel(sgTrainDataList, sgPredictList, kernelWidth[2])
    kernel_Gau_R4 = shogun.GaussianKernel(sgTrainDataList, sgPredictList, kernelWidth[3])
    kernel_Grad_R1 = shogun.GaussianKernel(sgTrainDataList, sgPredictList, kernelWidth[4])
    kernel_Grad_R2 = shogun.GaussianKernel(sgTrainDataList, sgPredictList, kernelWidth[5])
    kernel_Grad_R4 = shogun.GaussianKernel(sgTrainDataList, sgPredictList, kernelWidth[6])
    kernel_Dir_R1_X = shogun.GaussianKernel(sgTrainDataList, sgPredictList, kernelWidth[7])
    kernel_Dir_R2_X = shogun.GaussianKernel(sgTrainDataList, sgPredictList, kernelWidth[8])
    kernel_Dir_R4_X = shogun.GaussianKernel(sgTrainDataList, sgPredictList, kernelWidth[9])
    kernel_Dir_R1_Y = shogun.GaussianKernel(sgTrainDataList, sgPredictList, kernelWidth[10])
    kernel_Dir_R2_Y = shogun.GaussianKernel(sgTrainDataList, sgPredictList, kernelWidth[11])
    kernel_Dir_R4_Y = shogun.GaussianKernel(sgTrainDataList, sgPredictList, kernelWidth[12])
    kernel_Dog_R2_R1 = shogun.GaussianKernel(sgTrainDataList, sgPredictList, kernelWidth[13])
    kernel_Dog_R4_R2 = shogun.GaussianKernel(sgTrainDataList, sgPredictList, kernelWidth[14])
    kernel_Dog_R8_R6 = shogun.GaussianKernel(sgTrainDataList, sgPredictList, kernelWidth[15])

    kernel_train_list = [kernel_X_Y,kernel_Gau_R1,kernel_Gau_R2,kernel_Gau_R4,kernel_Grad_R1,kernel_Grad_R2,kernel_Grad_R4,
                         kernel_Dir_R1_X,kernel_Dir_R2_X,kernel_Dir_R4_X,kernel_Dir_R1_Y,kernel_Dir_R2_Y,kernel_Dir_R4_Y,
                         kernel_Dog_R2_R1,kernel_Dog_R4_R2,kernel_Dog_R8_R6]
    # kernel_train_list = [kernel_X_Y, kernel_Gau_R1]

    combined_kernel = shogun.CombinedKernel()
    for kernel in kernel_train_list:
        combined_kernel.append_kernel(kernel)
    return combined_kernel

#get shogun's combined feature
def getShogunFeature(trainDataFeature):
    combin_feature = shogun.CombinedFeatures()
    for x in trainDataFeature:
        dimen = x.shape
        if len(dimen) == 1:
            temp = x.reshape((-1, x.size))
        else:
            temp = x
        combin_feature.append_feature_obj(shogun.RealFeatures(temp))
    return combin_feature

#get mkl instance
def getMkl(kernel,label):
    svr_solver = shogun.SVRLight()
    mkl = shogun.MKLRegression(svr_solver)
    mkl.set_kernel(kernel)
    mkl.set_labels(shogun.RegressionLabels(label))
    mkl.set_mkl_norm(1)
    return mkl

#cross validation get the train data/label and test data/label
def crossValid(feature,label):
    feature_train,feature_text,label_train,labe_test = train_test_split(feature,label,test_size = 0.4)
    return feature_train,feature_text,label_train,labe_test




