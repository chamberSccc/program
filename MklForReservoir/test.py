import os
import pylab as pl
SHOGUN_DATA_DIR=os.getenv('SHOGUN_DATA_DIR', '../../../data')
from modshogun import *
from numpy import *
from matplotlib import *
from scipy.io import loadmat, savemat
from os       import path, sep

mat  = loadmat(sep.join(['..','..','..','data','multiclass', 'usps.mat']))
Xall = mat['data']
Yall = array(mat['label'].squeeze(), dtype=double)

# map from 1..10 to 0..9, since shogun
# requires multiclass labels to be
# 0, 1, ..., K-1
Yall = Yall - 1

random.seed(0)

subset = random.permutation(len(Yall))

#get first 1000 examples
Xtrain = Xall[:, subset[:1000]]
Ytrain = Yall[subset[:1000]]

Nsplit = 2
all_ks = range(1, 21)


# MKL training and output
labels = MulticlassLabels(Ytrain)
feats  = RealFeatures(Xtrain)
#get test data from 5500 onwards
Xrem=Xall[:,subset[5500:]]
Yrem=Yall[subset[5500:]]

#test features not used in training
feats_rem=RealFeatures(Xrem)
labels_rem=MulticlassLabels(Yrem)

kernel = CombinedKernel()
feats_train = CombinedFeatures()
feats_test = CombinedFeatures()

#append gaussian kernel
subkernel = GaussianKernel(10,15)
feats_train.append_feature_obj(feats)
feats_test.append_feature_obj(feats_rem)
kernel.append_kernel(subkernel)

#append PolyKernel
feats  = RealFeatures(Xtrain)
subkernel = PolyKernel(10,2)
feats_train.append_feature_obj(feats)
feats_test.append_feature_obj(feats_rem)
kernel.append_kernel(subkernel)

kernel.init(feats_train, feats_train)

mkl = MKLMulticlass(1.2, kernel, labels)

mkl.set_epsilon(1e-2)
mkl.set_mkl_epsilon(0.001)
mkl.set_mkl_norm(1)

mkl.train()

#initialize with test features
kernel.init(feats_train, feats_test)

out =  mkl.apply()
evaluator = MulticlassAccuracy()
accuracy = evaluator.evaluate(out, labels_rem)
print "Accuracy = %2.2f%%" % (100*accuracy)



