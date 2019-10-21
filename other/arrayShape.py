import numpy as np


a = np.random.randn(5)
b = np.random.randn(5,1)
print ('a shape: ', a.shape)
print ('b shape: ', b.shape)
# 不要用这种，这个是秩为1的数组，既不是行向量也不是列向量，它只有一个[]
print (a)
# 观察数组括号
print (b)
