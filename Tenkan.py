
print(int(98.5)+5)

print(str(54)+'esdf')

print(int('7878')+78)

print(bool(4546))

str2 = 'Hello World'

print(list(str2))

print(tuple(str2))

print(divmod(14,3))

print(abs(-98))

print(pow(3,3))

print(round(3.1323232,3))

st = [56,45,32,99,100,44,5,3,9]

st2 = reversed(st)

print(list(st2))

st3 = sorted(st,reverse=True)

print(list(st3)) 

def fun(num):
    return num%3==0

test = filter(fun,range(0,30))

print(list(test))

str4 = ['hell','efsv']
str5 =[]
for item in str4:
    new_item=item.upper()
    print(item)
    str5.append(new_item)

print(str5)

def fun2(x):
    return x.upper()


str7 = map(fun2,str4)

print(list(str7))