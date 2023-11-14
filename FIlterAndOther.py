def fun(num):
    return num!='x'

num2 = filter(fun,'xhihihixkhkhkhxkhkhx')

print(list(num2))

def fun2(x):
    return x

def fun3():
    print('Y')


str2 = map(fun2,range(10))

print(list(str2))

print(format('Hello World','-^20'))

print(format(65,'b'))

print(format(65,'o'))

print(format(65,'x'))

print(type(fun3),type(fun3()))