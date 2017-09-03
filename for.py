#for while 

#for in 遍历tuple
names = ('obama','trump','xijingping')
for name in names:
    print(name)

#for in 遍历range
numbers = range(101)
sum = 0
for n in numbers:
    sum += n
print(sum)

#for in 遍历list
numbers = list(range(101))
sum = 0
for n in numbers:
    sum += n
print(sum)

#while循环做计算
sum = 0
n = 101
while n>0:
    sum += n
    n += -1
print(sum)
