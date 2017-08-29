#在Python3中是支持Unicode的。
#Python在读取字符串时用Unicode编码，在写入文件时会转换成UTF-8(utf8变长编码)

str1 = "abc"  #此时在内存中使用的是unicode编码，每个字符对应多个字节。
str2 = b"abc" #此时在内存中每个字符对应单个字节，在字符串前面加上b前缀，标识字节存储。
print(str1,str2)

#一些字符API

print(ord("中"),chr(20013))  #ord可以得出某个字符的值，chr可以根据整数值获取字符

print('中文'.encode('utf-8'))       #encode可以指定编码，然后转换成对应内存中的byte
print(b'\xe4\xb8\xad\xe5\x9b\xbd\xe4\xba\xba'.decode('utf-8'))   #decode可以把byte解析为指定的编码

print(len('中文'))                  #len可以得到字符串长度
print(len('中文'.encode('utf-8')))  #len可以得到字节个数

#格式化字符串,%s可以将任何类型转换为string
print("hello,%s" % "liubin") 
print("my name is %s,my age is %d,I have %f pounds" % ('king',19,688.123)) 
print("%4d"%1988)
print("%.2f"%2.5678989)
print("compelete %d%%"%98) #如果想输出一个%