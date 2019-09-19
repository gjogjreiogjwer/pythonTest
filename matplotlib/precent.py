import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pylab 
# y轴用百分号表示

a = np.ones((3,2))
a[0][0] = 0.0276
a[0][1] = 0.1523
a[1][0] = 0.0311
a[1][1] = 0.2119
a[2][0] = 0.0333
a[2][1] = 0.1258

def to_percent(temp, position):
    return '%1.0f'%(100*temp) + '%'

index = ['Edit Distance', 'N-Gram', 'Jaro-Winkler Similarity']  # 行
columns = ['Precision', 'Recall']     # 列
df2 = pd.DataFrame(a, index=index, columns=columns)
print (df2)

df2.plot(kind='bar')
plt.title('Precision and Recall for different algorithms')
plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
# x轴标签旋转
pylab.xticks(rotation=360)
# 图上标数字
x = [0, 1, 2]
for i in range(3):
	a = x[i] - 0.12
	b = df2.Precision[i]
	c = x[i] + 0.12
	d = df2.Recall[i]
	plt.text(a, b+0.001, '%.4f' % b, ha='center', va= 'bottom',fontsize=9)
	plt.text(c, d+0.001, '%.4f' % d, ha='center', va= 'bottom',fontsize=9)
plt.show()




