from sklearn import svm
X = [[0, 0],[0,1], [1, 1], [1, 0]]  # training samples
y = [0,0, 1, 1]  # training target
clf = svm.SVC()  # class
clf.fit(X, y)  # training the svc model
z=[[2, 2],[-2,1]]
result = clf.predict([[-1,1],[1,1]])  # predict the target of testing samples
print result  # target

print clf.support_vectors_  # support vectors

print clf.support_  # indeices of support vectors

print clf.n_support_  # number of support vectors for each class