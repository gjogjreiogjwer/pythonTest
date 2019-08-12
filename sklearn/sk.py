# 1. 获取数据*******************************************************************
# 1.1 导入sklearn数据集
# 导入datasets模块以使用sklearn的数据集
from sklearn import datasets
from sklearn.model_selection import train_test_split

import numpy as np
import pandas as pd
a = [['波士顿房价', 'load_boston()','回归','506*13'],
	['鸢尾花', 'load_iris()','分类','150*4'],
	['糖尿病', 'load_diabetes()','回归','442*10'],
	['手写数字', 'load_digits()','分类','5620*64'],	]
a = np.array(a)
df = pd.DataFrame(a, columns=['数据集名称', '调用方式', '适用算法', '数据规模'])
print (df)

# 导入数据集
iris = datasets.load_iris()
# 获得特征向量
X = iris.data
# 获得样本标签
Y = iris.target
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)


# 1.1.1 手写数字数据集
digits = datasets.load_digits()
print (digits.data.shape)
print (digits.target.shape)
print (digits.images.shape)

# import matplotlib.pyplot as plt 
# plt.matshow(digits.images[0])
# plt.show()


# 2. 数据预处理*******************************************************************
from sklearn import preprocessing
# 2.1 z-score标准化 StandardScaler
# 标准化后，各特征0均值，单位方差

# scaler内存有均值和方差
scaler = preprocessing.StandardScaler().fit(X)

# 用scaler中的均值和方差来转换X，使X标准化
scaler.transform(X)
# 也要对测试集做同样的标准化


# 2.2 min-max标准化化
# 对原始数据进行线性变化，使结果落到[0,1]区间
scaler = preprocessing.MinMaxScaler(feature_range=(0,1)).fit(X_train)
scaler.transform(X_train)
scaler.transform(X_test)

# 2.3 正则化
'''
当你想要计算两个样本的相似度时必不可少的一个操作，就是正则化。
其思想是：首先求出样本的p范数，然后该样本的所有元素都要除以该范数，这样最终使得每个样本的范数都是1。
规范化（Normalization）是将不同变化范围的值映射到相同的固定范围，常见的是[0,1]，也成为归一化。

我们可以发现对于每一个样本都有0.4^2+0.4^2+0.81^2=1
这就是L2 norm，变换后每个样本的各维特征的平方和为1
类似的，L1 norm则是变换后每个样本的各维特征的绝对值之和为1
'''
x = [[1,-1,2],
	[2,0,0],
	[0,1,-1]]
x_normalized = preprocessing.normalize(x, norm='l2')
print (x_normalized)



# 3. 数据集拆分*******************************************************************
'''
Args:
	test_size: 样本占比
	random_state: 随机数的种子

Returns:
	X_train: 划分出的训练集数据
	X_test: 划分出的测试集数据
	Y_train: 划分出的训练集标签
	Y_test: 划分出的测试集标签
'''
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)



# 4. 模型定义*******************************************************************
# 4.1 线性回归
from sklearn.linear_model import LinearRegression
'''
Args:
	fit_intercept: 是否计算截距
	normalize: 当fit_intercept为True时，该参数才存在。normalize为True时，回归系数通过减去平均值并除以l2范数归一化
	n_jobs: 指定线程数
'''
model = LinearRegression(fit_intercept=True, normalize=False, copy_X=True, n_jobs=1)

# 4.2 逻辑回归
from sklearn.linear_model import LogisticRegression
'''
Args:
	penalty：使用指定正则化项（默认：l2）
    dual: n_samples > n_features取False（默认）
    C：正则化强度的反，值越小正则化强度越大
    n_jobs: 指定线程数
    random_state：随机数生成器
    fit_intercept: 是否需要常量
'''
model = LogisticRegression(penalty='l2', dual=False, tol=0.0001, C=1.0,
    fit_intercept=True, intercept_scaling=1, class_weight=None,
    random_state=None, solver='liblinear', max_iter=100, multi_class='ovr',
    verbose=0, warm_start=False, n_jobs=1)


# 4.3 朴素贝叶斯算法
from sklearn import naive_bayes
'''
文本分类问题常用MultinomialNB
Args:
    alpha：平滑参数
    fit_prior：是否要学习类的先验概率；false-使用统一的先验概率
    class_prior: 是否指定类的先验概率；若指定则不能根据参数调整
    binarize: 二值化的阈值，若为None，则假设输入由二进制向量组成
'''
model = naive_bayes.GaussianNB() # 高斯贝叶斯
model = naive_bayes.MultinomialNB(alpha=1.0, fit_prior=True, class_prior=None)
model = naive_bayes.BernoulliNB(alpha=1.0, binarize=0.0, fit_prior=True, class_prior=None)

# 4.4 决策树
from sklearn import tree
'''
Args:
    criterion ：特征选择准则gini/entropy
    max_depth：树的最大深度，None-尽量下分
    min_samples_split：分裂内部节点，所需要的最小样本树
    min_samples_leaf：叶子节点所需要的最小样本数
    max_features: 寻找最优分割点时的最大特征数
    max_leaf_nodes：优先增长到最大叶子节点数
    min_impurity_decrease：如果这种分离导致杂质的减少大于或等于这个值，则节点将被拆分。
'''
model = tree.DecisionTreeClassifier(criterion='gini', max_depth=None,
    min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0,
    max_features=None, random_state=None, max_leaf_nodes=None,
    min_impurity_decrease=0.0, min_impurity_split=None,
     class_weight=None, presort=False)


# 4.5 支持向量机
from sklearn.svm import SVC
'''
Args:
    C：误差项的惩罚参数C
    gamma: 核相关系数。浮点数，If gamma is ‘auto’ then 1/n_features will be used instead.
'''
model = SVC(C=1.0, kernel='rbf', gamma='auto')


# 4.6 kNN
from sklearn import neighbors
'''
Args:
    n_neighbors： 使用邻居的数目
    n_jobs：并行任务数
'''
model = neighbors.KNeighborsClassifier(n_neighbors=5, n_jobs=1) # 分类
model = neighbors.KNeighborsRegressor(n_neighbors=5, n_jobs=1) # 回归

# 4.7 多层感知器（神经网络）
from sklearn.neural_network import MLPClassifier
'''
Args:
    hidden_layer_sizes: 元祖
    activation：激活函数
    solver ：优化算法{‘lbfgs’, ‘sgd’, ‘adam’}
    alpha：L2惩罚(正则化项)参数。
'''
model = MLPClassifier(activation='relu', solver='adam', alpha=0.0001)





















