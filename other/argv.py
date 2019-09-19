# -*- coding:utf-8 -*-
# sys.argv 是获取运行python的时候命令行参数，以list形式存储
# sys.argv[0] 表示当前module名字
# 在终端输入 python3 argv.py tt rr ff
# 输出 ['argv.py', 'tt', 'rr', 'ff']   4

import sys
a = sys.argv
b = len(sys.argv)
print (a)
print (b)
