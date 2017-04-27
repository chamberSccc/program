import numpy as np


def a1():
    a = [[1, 1], [1, 1]]
    a = np.reshape(a, (1, -1))
    b = np.zeros((4, 4))

    for i in range(4):
        b[i, :] = a
    print b

def a2():
    a=[128,127,225,200,254,255]
    b = np.array(a)
    d = np.round(b/255.0,decimals=2)
    f = np.round(d)
    e = np.round([0.37,0.58])
    print b
    print d
    print e
    print f
a2()
