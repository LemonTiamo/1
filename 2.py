x = "awesome"# 在函数内创建一个和全局变量相同名称的变量，这个变量是本地变量，只能在函数内部使用。

def myfunc():
  x = "fantastic"
  print ("python is " + x)

myfunc()


print ("python is " + x)



 
def myfunc():#函数内创建全局变量，用global
# 函数内创建的变量，是局部变量，只能在函数内部使用。
  global x 
  x = "fantastic"

myfunc()

print ("python is " + x)


import random #构造伪随机字节
print (random.randbytes(3))