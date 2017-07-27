# -*- coding: utf-8 -*-
import CombinDataAndFeature as comb
import PreMklProcess as pMkl
import numpy as np

featureList =  comb.generateFeatureMat()
wellTrainData ,seisTrainData = comb.combinDataAndFeature(comb.seisDataList,comb.wellLogList,featureList)
wellFeatureDataList,seisFeatureDataList = comb.detailFeature(wellTrainData ,seisTrainData)

#测井数据训练
kernelWidthList = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,
                   1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,]
combined_kernel = pMkl.getCombinKernel(kernelWidthList,wellFeatureDataList)
combined_shogun_Feature = pMkl.getShogunFeature(wellFeatureDataList)
#孔隙度与渗透率标签
porosity_Well = np.array(wellTrainData[:,5])
permeability_Well = np.array(wellTrainData[:,4])
mkl_Well = pMkl.getMkl(combined_kernel,porosity_Well)

aaa =  1