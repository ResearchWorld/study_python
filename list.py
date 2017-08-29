#list是python中一种有序的数据集合

classmates = ['xiaoming','xiaohua','xiaohong',3]
print('list的长度:',len(classmates)) #得到长度
print('list的最后一个元素:%d' % classmates[-1])  #取出最后一个元素
print('list倒数第二个元素:%s' % classmates[-2])
classmates.append(4) #末尾追加元素
print(classmates)
end_elem = classmates.pop() #末尾删除元素
print("末尾删除的元素:%s" % end_elem,"容器中的元素:%s" % classmates)
classmates.pop(0)
print('删除了指定位置的元素,最前面的')
print(classmates)

