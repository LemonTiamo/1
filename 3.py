a = """python is awesome ,
Robin and Ted are the best,
Barney alwasys good ,
but they are not the best,
"""
print (a)   #用双引号将多行字符串分配给变量。

a = "Robin is beautiful"  # 1处的字符，第一个字符的位置是0
print (a[1])
print (len(a))  # 获取字符串长度。

for x in "banana":   #循环浏览banana中的字母：
  print (x)


txt = "Robin is beautiful"  # 检查字符串，if 条件语句。
if "is" in txt:
  print ("Yes,'is' in txt")


c = " Robin is beautiful "
print (c[:7])  # 从头开始切片。
print (c[2:])  # 从位置2处开始切片，切到最后。
print (c[-9:-1])  #用负索引，从后面往前切片。
print (c.upper())  #返回大写的字符串。
print (c.lower())  # 返回小写的字符串。
print (a.strip())  # 删除空格从头到尾。
print (c.replace("R","J"))  # 替换字符，将“R” 替换成"J“。

d = " Robin is ,beautiful "
print (d.split(","))  # 将”，“ 前的字符串与","的字符串拆分。

a = "wer"  ## 字符串串联
b = "wed"
c = a + b
d = a + " " + b
print (c)
print (d)

## 将字符串和数字连起来。
age = "23"
txt = "weyuxnk,i am {}"
print (txt.format(age))