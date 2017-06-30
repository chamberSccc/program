import os
SHOGUN_DATA_DIR=os.getenv('SHOGUN_DATA_DIR', '../../../data')
import sys
# print sys.path
# sys.path.append('/usr/local/lib/python2.7/site-packages')


# a = [range(20,23) for x in range(1,10)]
# print a


a = '-99.00 -99.00 -99.00 -99.00\r\n'
print len(a)
print a[0:6]
b= a.strip('\r\n').rstrip().replace('-99.00','0').split(' ')
print b