Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> d = np.array([4,5,8,6,4,12,21,3,65,7,43,66])
>>> len(d)
12
>>> labels = np.array([0,0,0,0,0,0,1,1,1,1,1,1])
>>> np.argsort(d)
array([ 7,  0,  4,  1,  3,  9,  2,  5,  6, 10,  8, 11], dtype=int64)
>>> s = np.argsort(d)
>>> s
array([ 7,  0,  4,  1,  3,  9,  2,  5,  6, 10,  8, 11], dtype=int64)
>>> labels[s]
array([1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1])
>>> labels[s][:5]
array([1, 0, 0, 0, 0])
>>> np.sort(d)
array([ 3,  4,  4,  5,  6,  7,  8, 12, 21, 43, 65, 66])
>>> lab =labels[s][:5]
>>> lab
array([1, 0, 0, 0, 0])
>>> np.unique(lab)
array([0, 1])
>>> np.unique(lab, return_counts = True)
(array([0, 1]), array([4, 1], dtype=int64))
>>> count = np.unique(lab, return_counts = True)
>>> count
(array([0, 1]), array([4, 1], dtype=int64))
>>> count[0]
array([0, 1])
>>> count[0][np.argmax(count[1])]
0
>>> count[0][0]
0
>>> count[0][1]
1
>>> count[1]
array([4, 1], dtype=int64)
>>> np.argmax(count[1])
0
>>> 
