#多进程: 可以加快程序运行速度
# 把数据分成几份，传入不同的进程并发运行
import time
import random
from multiprocessing import Process


def x(name):
    print('%s eeee' %name)
    time.sleep(random.randrange(1,5))
    print('%s aaaa' %name)



p1=Process(target=x,args=('egon',)) #必须加,号
p2=Process(target=x,args=('alex',))
p3=Process(target=x,args=('wupeqi',))
p4=Process(target=x,args=('yuanhao',))

p1.start()
p2.start()
p3.start()
p4.start()
print('主线程')

