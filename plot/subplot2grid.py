'''
在一张大图里分列几个小图
'''

import matplotlib.pyplot as plt
# 解决中文显示问题
from matplotlib.font_manager import FontProperties
font = FontProperties(fname='/Library/Fonts/Songti.ttc')

fig = plt.figure()
# 2行3列，从（0，0）开始
plt.subplot2grid((2,3), (0,0))
plt.title('啦啦啦')

plt.subplot2grid((2,3), (0,1))
plt.subplot2grid((2,3), (0,2))
# 行跨度为2，列跨度：rowspan
plt.subplot2grid((2,3), (1,0), colspan=2)
plt.subplot2grid((2,3), (1,2))
plt.show()










