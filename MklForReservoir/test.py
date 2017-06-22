import pylab as pl
from matplotlib import *
import os
SHOGUN_DATA_DIR=os.getenv('SHOGUN_DATA_DIR', '../../../data')
# import all shogun classes
from modshogun import *
from numpy import *


kernel = CombinedKernel()
num=30;
num_components=4
means=zeros((num_components, 2))
means[0]=[-1,1]
means[1]=[2,-1.5]
means[2]=[-1,-3]
means[3]=[2,1]

covs=array([[1.0,0.0],[0.0,1.0]])

gmm=GMM(num_components)
[gmm.set_nth_mean(means[i], i) for i in range(num_components)]
[gmm.set_nth_cov(covs,i) for i in range(num_components)]
gmm.set_coef(array([1.0,0.0,0.0,0.0]))
xntr=array([gmm.sample() for i in xrange(num)]).T
xnte=array([gmm.sample() for i in xrange(5000)]).T
gmm.set_coef(array([0.0,1.0,0.0,0.0]))
xntr1=array([gmm.sample() for i in xrange(num)]).T
xnte1=array([gmm.sample() for i in xrange(5000)]).T
gmm.set_coef(array([0.0,0.0,1.0,0.0]))
xptr=array([gmm.sample() for i in xrange(num)]).T
xpte=array([gmm.sample() for i in xrange(5000)]).T
gmm.set_coef(array([0.0,0.0,0.0,1.0]))
xptr1=array([gmm.sample() for i in xrange(num)]).T
xpte1=array([gmm.sample() for i in xrange(5000)]).T
traindata=concatenate((xntr,xntr1,xptr,xptr1), axis=1)
trainlab=concatenate((-ones(2*num), ones(2*num)))

testdata=concatenate((xnte,xnte1,xpte,xpte1), axis=1)
testlab=concatenate((-ones(10000), ones(10000)))

#convert to shogun features and generate labels for data
feats_train=RealFeatures(traindata)
labels=BinaryLabels(trainlab)

_ = pl.jet()
pl.figure(figsize=(18, 5))
pl.subplot(121)
# plot train data
_ = pl.scatter(traindata[0, :], traindata[1, :], c=trainlab, s=100)
pl.title('Toy data for classification')
pl.axis('equal')
colors = ["blue", "blue", "red", "red"]
# a tool for visualisation
from matplotlib.patches import Ellipse


def get_gaussian_ellipse_artist(mean, cov, nstd=1.96, color="red", linewidth=3):
    vals, vecs = pl.eigh(cov)
    order = vals.argsort()[::-1]
    vals, vecs = vals[order], vecs[:, order]
    theta = numpy.degrees(arctan2(*vecs[:, 0][::-1]))
    width, height = 2 * nstd * sqrt(vals)
    e = Ellipse(xy=mean, width=width, height=height, angle=theta, \
                edgecolor=color, fill=False, linewidth=linewidth)

    return e


for i in range(num_components):
    pl.gca().add_artist(get_gaussian_ellipse_artist(means[i], covs, color=colors[i]))

pl.show()
