#if of python
age = input("please enter your age")
age = int(age)
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')