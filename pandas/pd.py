import pandas as pd
import numpy as np

'''
pandas主要有两种数据对象
1. Series: 一种带索引的序列对象
2. DataFrame： 类似于数据库table有行列的数据对象
'''
s1 = pd.Series(list('qwer'))
print ('s1:*********************')
print (s1)

# 通过numpy二维数组创建
df1 = pd.DataFrame(np.random.rand(6,4))
print ('df1:*********************')
print (df1)

a = np.ones((3,2))
a[0][1] = 2
a[2][1] = 6
print ('a:*********************')
print (a)

index = ['a', 'b', 'c']  # 行
columns = ['d', 'e']     # 列
print ('df2:*********************')
df2 = pd.DataFrame(a, index=index, columns=columns)
print (df2)

# 通过字典创建
df3 = pd.DataFrame({'A' : 1,
					'B' : pd.Series(1, index = list(range(4)), dtype='float32'),
					'C' : np.array([3]*4, dtype='int32'),
					'D' : 'ttt'})
print ('df3:*********************')
print (df3)

# 索引
print ('s1索引:*********************')
print (s1.index)
print ('df1索引:*********************')
print (df1.index)

# 为了有足够数据用于展示，选择tushare的数据
import tushare as ts
df = ts.get_k_data('000001')
print ('df:*********************')
print (df)

# 查看每列的数据类型
print ('df.dtypes:*********************')
print (df.dtypes)

# 查看前5行
print ('df.前5行:*********************')
print (df.head())

# 查看后5行
print ('df.后5行:*********************')
print (df.tail())

# 查看前10行
print ('df.前10行:*********************')
print (df.head(10))

# 查看第1行
print ('df.第1行:*********************')
print (df[0:1])

# 查看10-20行
print ('df.第10-20行:*********************')
print (df[10:21])

# 查看date列前5个数据
print ('date列前5个数据:*********************')
print (df.date.head())  #或者 df["date"].head()

# 查看date列, code列前5个数据
print ('date列, code列前5个数据:*********************')
print (df[['date', 'code']].head())  

# loc
print ('*****************************************************************************************')
# 查看date列, code列第10行
print ('date列, code列第10行:*********************')
print (df.loc[10, ['date', 'code']])  

# 查看date列, code列第10-20行
print ('date列, code列第10-20行:*********************')
print (df.loc[10:20, ['date', 'code']])  

# iloc
print ('*****************************************************************************************')
# 通过索引值iloc查看第1行
print ('第1行:*********************')
print (df.iloc[0])

# iloc区分loc
print ('df2:*********************')
df2 = pd.DataFrame(a, index=index, columns=columns)
print (df2)
print ('loc第1行:*********************')
print (df2.loc['a'])
print ('iloc第1行:*********************')
print (df2.iloc[0])

# 通过索引值iloc查看最后1行
print ('第1行:*********************')
print (df.iloc[-1])

# 通过索引值iloc查看第1列，前五个数值
print ('第1列，前五个数值:*********************')
print (df.iloc[:,0].head()) 

# 通过索引值iloc查看前2到4行，第1，3列
print ('前2到4行，第1，3列:*********************')
print (df.iloc[1:4, [0,2]]) 

# 条件筛选
print ('*****************************************************************************************')
# 查看open列大于10的前5行
print ('open列大于10的前5行:*********************')
print (df[df.open>10].head()) 

# 查看open列大于10小于10.6的前5行
print ('open列大于10小于10.6的前5行:*********************')
print (df[(df.open>10) & (df.open<10.6)].head()) 


# 增加
print ('*****************************************************************************************')

print ('创建2018-08-08到2018-08-15的时间序列，默认时间间隔为day:*********************')
print (pd.date_range('20180808', periods=7))

print ('创建2018-08-08 00:00 到2018-08-15 00:00 的时间序列，时间间隔为hour:*********************')
print (pd.date_range('20180808', '20180809', freq='H'))

print ('通过已有序列创建时间序列:*********************')
print (pd.to_datetime(df.date.head()))


# 修改
print ('*****************************************************************************************')
# 将df的索引值修改为date列的数据
print ('df:*********************')
print (df.head())
df.index = pd.to_datetime(df.date)
print ('df修改index后:*********************')
print (df.head())

# 修改列的字段
print ('df修改columns后:*********************')
df.columns = ['Date', 'Open', 'Close', 'High', 'Low', 'Volume', 'Code']
print (df.head())

# 将Open列每个数值+1，apply()不直接修改原数据
df.Open = df.Open.apply(lambda x: x+1)
print ('Open+1:*********************')
print (df.head())

# 将Open,Close列每个数值+1，apply()不直接修改原数据
print ('Open, Close+1:*********************')
print (df[['Open', 'Close']].head().apply(lambda x:x.apply(lambda x: x+1)))



# 删除
print ('*****************************************************************************************')
# drop()不直接修改原数据，如果要对原dataframe修改，传入inplace=True
# 行的值在axis=0, 列的值在axis=1

print ('删除Open列:*********************')
print (df.drop('Open', axis=1).head())

print ('删除第1，3列:*********************')
print (df.drop(df.columns[[1,3]], axis=1).head())

# 统计
print ('*****************************************************************************************')
print ('df.describe():*********************')
print (df.describe())

print ('查看open列每个值出现次数:*********************')
print (df.Open.value_counts().head())

# 处理缺失值
print ('*****************************************************************************************')
# 删除含有NaN的任意行
df.dropna(how='any')

# 删除含有NaN的任意列
df.dropna(how='any', axis=1)

# 将NaN的值改为5
df.fillna(5)


# 排序
print ('*****************************************************************************************')
# 默认不修改原数据
print ('按index排序:*********************')
print (df.sort_index(axis=1).head())

print ('按index排序,递减:*********************')
print (df.sort_index(ascending=False).head())

print ('按Open列升序:*********************')
print (df.sort_values(by='Open'))


# 特征因子化，输出数值型特征
print ('*****************************************************************************************')
df3.iloc[0,3] = 'yyy'
print (df3)
dummies_D = pd.get_dummies(df3['D'], prefix='D')
print (dummies_D)


# 合并
print ('*****************************************************************************************')
split_rows = [df.iloc[0:2,:], df.iloc[2:4,:], df.iloc[4:9]]
# concat(axis), 默认axis为0，列对齐，不同行的两张表合并（行数变多）
print ('行方向合并:*********************')
print (pd.concat(split_rows))

# concat(axis), axis为1，行对齐，不同列的两张表合并（列数变多）
print ('列方向合并:*********************')
# 第2列，第3，4列
split_columns = [df.iloc[:,1:2], df.iloc[:,2:4]]
print (pd.concat(split_columns, axis=1))

print ('insert()追加行:*********************')
print (df.append(df.iloc[0,:], ignore_index=True))

# 复制
print ('*****************************************************************************************')
print ('dataframe是引用对象，显示调用copy()以复制')

# 数据读写
print ('*****************************************************************************************')
print ('将数据保存到stock.csv*********************')
df.to_csv('stock.csv')

print ('查看stock.csv前5行*********************')
with open('stock.csv') as rf:
	print (rf.readlines()[:5])

print ('读取stock.csv并将第一行作为columns *********************')
df2 = pd.read_csv('stock.csv', index_col=0)
print (df2)

print ('读取stock.csv并将第一行作为columns,将Code中的000001作为str类型读取，不然会解析成整数 *********************')
df2 = pd.read_csv('stock.csv', index_col=0, dtype={'Code':str})
print (df2)

# 查找包含str
print ('*****************************************************************************************')
print (df3.D.str.contains('y'))
print (df3.D.str.contains('y|t'))

# 查找不包含str
print (df3.D.str.contains('y')==False)

# 添加一列
df3['Q'] = 2
print (df3)

# 索引
print (df3.loc[2,'Q'])
print (df3.iloc[0,3])










