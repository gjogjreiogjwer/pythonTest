import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 解决中文显示问题
from matplotlib.font_manager import FontProperties
font = FontProperties(fname='/Library/Fonts/Songti.ttc')

'''
一. matplotlib基础知识*******************************************************************
基本图表包括的元素：
	x轴和y轴： axis
	x轴和y轴刻度： tick
	x轴和y轴刻度标签： tick label
	绘图区域（坐标系）： axes
	坐标系标题： title
	轴标签： xlabel，ylabel
'''
# 1.包含单条曲线的图********************************************************************
# 1.1 直线
x = [1,2,3,4,5]
y = [2,4,6,8,10]
# plt.plot(x, y)

# 1.2 正弦曲线
x1 = np.arange(-np.pi, np.pi, 0.01)
y1 = np.sin(x1)
# plt.plot(x1, y1)


# 2.包含多个曲线的图 subplot********************************************************************
# 2.1 连续调用多次plot函数
# plt.plot(x, y)
# plt.plot(x1, y1)

# 2.2 在一个plot()中传入多对x，y
# plt.plot(x1, y1, x1+1, y1+1)


# 3.将多个图绘制在一个table中********************************************************************
# 把table区域分成2行2列，最后一个1表示位置，可以去掉逗号
# a1 = plt.subplot(2, 2, 1)
# a1.plot(x1, y1)

# a2 = plt.subplot(222)
# a2.plot(x1, y1)
# a2.plot(x1+1, y1+1)

# a3 = plt.subplot(223)
# a3.plot(x1, y1)

# a4 = plt.subplot(224)
# a4.plot(x, y)


# 4.网格线 grid********************************************************************
'''
Args:
	axis: 'x', 'y', 'both' 绘制哪个方向的网格线，默认'both'
	color: 网格线颜色
	linestyle: 网格线风格 '-', '--', '-.'
	alpha: 透明度
'''
# plt.grid(color='r', linestyle='-.', alpha=0.5, axis='x')
# plt.plot(x1, y1)

# 绘制一个两行两列的曲线图阵，并设置网格
# a1 = plt.subplot(221)
# a1.grid()
# a1.plot(x1, y1)


# 5.坐标轴界限********************************************************************
# 5.1 axis([xmin, xmax, ymin, ymax])：修改x，y轴刻度值
# a1 = plt.subplot(121)
# a1.plot(x1, y1)
# a2 = plt.subplot(122)
# a2.axis([-4, 4, -2, 2])
# a2.plot(x1, y1)

# 5.2 axis('off')：关闭坐标轴
# plt.plot(x1, y1)
# plt.axis('off')

# 5.3 plt.figure(figsize=(a,b)):设置画布比例
# a: x轴刻度比例，b: y轴刻度比例
# (2,1) 表示x刻度为y刻度的2倍
# plt.figure(figsize=(10,5))
# plt.plot(x1, y1)

# 5.4 xlim(), ylim(): 设置坐标轴范围
# plt.xlim(-6, 6)
# plt.ylim(-2, 2)
# plt.plot(x, y)

# 5.5 通过对象的方式设置x，y的刻度值范围 ax.set_xlim(a,b)
# ax1 = plt.subplot(111)
# ax1.set_xlim(-4, 4)
# ax1.set_ylim(-2, 2)
# ax1.plot(x1, y1)


# 6.坐标轴标签********************************************************************
'''
Args:
	color: 颜色
	fontsize: 字体大小
	rotation: 标签旋转角度
	xlabel, ylabel: x，y轴标签
'''
# y1 = np.cos(x1)
# plt.title('cos()')
# plt.ylabel('啦啦啦', fontsize=16, rotation=90, color='r')
# plt.xlabel('么么么', fontsize=16, rotation=0, color='r')
# plt.plot(x1, y1)

# 通过对象的方式设置标签 ax.set_xlabel()
# ax = plt.subplot(111)
# ax.set_xlabel('x_label')
# ax.set_ylabel('y_label')
# ax.set_title('title', fontsize=19)
# ax.plot(x1, y1)


# 7.图例 legend********************************************************************
# loc参数：设置图例的位置 best,upper right, upper left...
# plt.plot(x1, y1, label='aaa')
# plt.plot(x1+1, y1+1, label='bbb')
# plt.legend()
# 或者
# plt.plot(x1 ,y1)
# plt.plot(x1+1, y1+1)
# plt.legend(['a', 'b'])


# 8.保存/读取图片********************************************************************
# 8.1 使用figure对象的savefig函数保存图片
'''
Args:
	fname: 图片名字
	dpi: 分辨率，默认为100
	facecolor: 图像背景颜色，默认为'w'白色
'''
# fig=plt.figure()
# plt.axis('off')
# plt.plot(x1, y1)
# fig.savefig(fname='gulu.png', dpi=500)

# 读取图片
# img = plt.imread('gulu.png')
# plt.imshow(img)


# 二. 设置plot风格和样式*******************************************************************
# plot语句支持除x，y以外的参数，以字符串形式存在

# 1.颜色********************************************************************
# Arg: color 或者 c
# plt.plot(x1, y1, c='g')
# plt.plot(x1+1, y1+1, color='b')


# 2.透明度********************************************************************
# Arg: alpha
# plt.plot(x1, y1, c='r', alpha=0.4)


# 3.背景色********************************************************************
# Arg: facecolor
# 设置坐标系的前景色
# ax = plt.subplot(111)
# ax.plot(x, y, c='r')
# ax.set_facecolor('green')

# 设置坐标系的背景色
# f = plt.figure()
# p = plt.plot(x1, y1)
# f.set_facecolor('yellow')

# 4.线型********************************************************************
# Arg: linestyle 或 ls
# '-': 实线, '-.': 点划线, ':': 虚线, '--': 破折线
# plt.plot(x1, y1, ls='--')


# 5.线宽********************************************************************
# Arg: linewidth 或 lw
# plt.plot(x1, y1, ls='-.', lw=5)


# 6.点型********************************************************************
# Arg: marker, markersize
# 's': 正方形, 'h/H': 六边形, '8': 八边形, 'p': 五边形,
# '.': 点, '*': 星号, ',': 像素, 'x': X, '+': 加号,
# 'o': 圆圈, 'd': 小菱形, 'D': 菱形,
# '1': 一角朝下的三脚架, '2': 一角朝上的三脚架, '3': 一角朝左的三脚架, '4': 一角朝右的三脚架 
# plt.plot(x, y, marker='p')


# 7.多参数连用********************************************************************
# 只可以设置颜色、点型、线型，把几种参数写在一个字符串内
# plt.plot(x, y, 'rs--')


# 8.在一条语句中为多个曲线进行设置********************************************************************
# 8.1 多个曲线同一设置,不能多参数连用
x = np.linspace(0,10,30)
y = x ** 2
# plt.plot(x, y, x+1, y-1, y+3, y-2, c='r')

# 8.2 多个曲线不同设置,可以多参数连用
# p1, p2, p3 = plt.plot(x, y, x+1, y-1, y+3, y-2)
# p1.set_lw(5)
# p3.set_color('y')

# plt.plot(x, y, 'or-.', x+1, y-1, 'yd', y+3, y-2, 'g--')



# 9. X,Y轴坐标刻度********************************************************************
# 9.1 对x，y轴的刻度做映射，并非修改
# plt.xticks([刻度列表], [名称列表])
# plt.xticks([0,2,4,6,8,10], ['a','b','c','d','e','f'])
# plt.plot(x,y)

# 9.1 使用面向对象的方法设置刻度方法
# ax = plt.subplot(111)
# ax.plot(x,y)
# ax.set_yticks([0,200,400,600,800,1000])
# ax.set_yticklabels(['q','w','e','r','t','y'])



# 三. 2D图形*******************************************************************

# 1.条形图 plt.bar()********************************************************************
'''
Args:
	第一个参数是索引
	第二个参数是数据值
	第三个参数是条形的宽度
'''
x = [1,2,3,4,5]
y = [2,4,6,8,10]
# plt.bar(x, y, 0.5)

# 水平条形图
# plt.barh(x, y, 0.5)





# data = pd.read_csv('train.csv')
# survivedInfo = data.Survived.value_counts()
# print (survivedInfo)
# survivedInfo.plot(kind='bar')

# 散点图
# print (data.Survived)
# print (data.Age)
# plt.scatter(data.Survived, data.Age)

# 密度图
# data.Age[data.Pclass==1].plot(kind='kde', label='头等舱')
# data.Age[data.Pclass==2].plot(kind='kde', label='2等舱')
# data.Age[data.Pclass==3].plot(kind='kde', label='3等舱')
# plt.legend()
# print (data.Age[data.Pclass==1])

# survived_0 = data.Sex[data.Survived==0].value_counts()
# survived_1 = data.Sex[data.Survived==1].value_counts()
# print (survived_0)
# df = pd.DataFrame({'获救':survived_1, '未获救':survived_0})
# print (df)
# plt.subplot(111)
# survived_0.plot(kind='bar')
# df.plot(kind='bar')

# print (data.Survived[data.Sex=='female'].value_counts())
# print (data.Survived[data.Sex=='female'][data.Pclass!=3].value_counts())
# data.Survived[data.Sex=='female'][data.Pclass!=3].value_counts().plot(kind='bar')

# g = data.groupby(['SibSp', 'Survived'])
# df = pd.DataFrame(g.count()['PassengerId'])
# print (df)


# print (data.Cabin.value_counts())
# survived_cabin = data.Survived[pd.notnull(data.Cabin)].value_counts()
# survived_nocabin = data.Survived[pd.isnull(data.Cabin)].value_counts()
# print (survived_cabin)
# df = pd.DataFrame({'有':survived_cabin, '无':survived_nocabin})
# df.plot(kind='bar')








plt.show()
