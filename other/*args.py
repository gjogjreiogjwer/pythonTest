# -*- coding:utf-8 -*-

# *args 实质就是将函数传入的参数，存储在元组类型的变量args当中
def fun_var_args(farg, *args):  
    print ("arg:", farg)
    for value in args:  
        print ("other arg:", value)

def fun_input_list(var1, var2, var3):
    print (var1, var2, var3)

# **kargs 实质就是将函数的参数和值，存储在字典类型的kargs变量中
def fun_var_kargs(farg, **kargs):
    print ("firsr value %s" % farg)
    for key in kargs.keys():
        print (kargs[key])

def fun_input_dic(var1, var2=2, var3=3):
    print (var1, var2, var3)


if __name__ == '__main__':
	fun_var_args(1, "two", 3)

	print ('*********************')
	var_list = ["second", 3]
	fun_input_list(1, *var_list)

	print ('*********************')
	fun_var_kargs(1, var1="second", var2=35, var3="third")

	print ('*********************')
	dic_input = {"var2":2, "var3":"third"}
	fun_input_dic(1, **dic_input)