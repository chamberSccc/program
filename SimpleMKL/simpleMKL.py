from sklearn import svm
import numpy as np
import SvrModel.ProsityWithCoor as CoorSvr


rate = 0.001
maxIter = 0
epsilon = 0
svrList = ['CoorSvr','GausianSvr']

#param
def getGadient(hDataMat,yDataMat):
    initDVector = np.zeros(hDataMat.shape[1])
    return


#mkl problem
def simpleMKL(svrNameList):
    initdVec = np.zeros(svrNameList)
    for i in range(1):
        dVector = 0
        for i in range(len(svrNameList)):
            svrName = svrNameList[i]
            svrModel = globals()[svrName]()  # reflect instance by classname
            clf = svrModel.creatSVR()
            preData = clf.predict(svrModel.trainData())
    return


