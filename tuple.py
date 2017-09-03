#tuple是python中一个有序的集合，和list最大的区别是不能随意修改

t = ()  #定义了一个空的tuple
print(t)        
t = (1) #这里要注意，会当成一个数字，括号会被当成数学表达式
print(t)
t = (1,) #如果要初始化一个元素，请在后面加个逗号
print(len(t))

t1 = ('xiaoming','xiaohong',[5,8]) #tuple指向的元素永远不变，切记这点！！！！！！！！！
t1[2][0] = 6 #tuple指向的元素永远不变，切记这点！！！！！！！！！,这里只是list元素变了
print(t1)