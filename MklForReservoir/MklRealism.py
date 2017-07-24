# -*- coding: utf-8 -*-
import numpy as np
import os
SHOGUN_DATA_DIR=os.getenv('SHOGUN_DATA_DIR', '../../../data')
import modshogun as shogun

# train_data = np.array([[1,2,3],[1.1,2.1,3.1]],dtype=float)
# train_label = np.array([1,2,3],dtype=float)
# test_data = np.array([[2,3,4],[2.1,3.1,4.1]],dtype=float)
# test_label = np.array([2,3,4],dtype=float)
#获取核函数的组合实例
def getCombinKernel():
    kernel_Dog_1 = shogun.GaussianKernel(1.0)
    kernel_Grad_1 = shogun.GaussianKernel(2.0)
    # kernel_DirX = shogun.GaussianKernel(1.0)
    # kernel_DirY = shogun.GaussianKernel(1.0)
    combined_kernel = shogun.CombinedKernel()
    combined_kernel.append_kernel(kernel_Dog_1)
    combined_kernel.append_kernel(kernel_Grad_1)
    # combined_kernel.append_kernel(kernel_DirX)
    # combined_kernel.append_kernel(kernel_DirY)
    return combined_kernel

def reshapeData():
    features_train = shogun.RealFeatures(train_data)
    features_test  = shogun.RealFeatures(test_data)
    features_train_label = shogun.RegressionLabels(train_label)
    features_test_label = shogun.RegressionLabels(test_label)
    return features_train,features_test,features_train_label,features_test_label

def trainData():
    return
train_data = np.array([[1,2,3],[1.1,2.1,3.1]],dtype=float)
train_data1 = shogun.RealFeatures(np.array([[1.2,2.2,3.2],[1.3,2.3,3.3],[1.4,2.4,3.4]],dtype=float))
train_label = np.array([1,2,3],dtype=float)
test_data = np.array([[2,3,4],[2.1,3.1,4.1]],dtype=float)
test_label = np.array([2,3,4],dtype=float)
traindata,testdata,traindatalabel,testdatalabel = reshapeData()
kernel_Dog_1 = shogun.GaussianKernel(traindata,traindata,float(0.5))
kernel_Grad_1 = shogun.GaussianKernel(train_data1,train_data1,float(1))
combin_feature = shogun.CombinedFeatures()
combin_feature.append_feature_obj(traindata)
combin_feature.append_feature_obj(train_data1)


combin_kernel = shogun.CombinedKernel()
combin_kernel.append_kernel(kernel_Dog_1)
combin_kernel.append_kernel(kernel_Grad_1)
combin_kernel.init(combin_feature,combin_feature)

binary_svm_solver = shogun.SVRLight()
mkl = shogun.MKLRegression(binary_svm_solver)
mkl.set_kernel(combin_kernel)
mkl.set_labels(traindatalabel)
# mkl.set_C(1, 1)
mkl.set_mkl_norm(1)
mkl.train()
beta = combin_kernel.get_subkernel_weights()
alpha = mkl.get_alphas()
combin_kernel.init(testdata, testdata)
labels_predict = mkl.apply_regression()
b = labels_predict.get_labels()

aaa=1

aaaa=1


