def fun(x):
    for item in x:
        if 'A'<=item<='Z':
            return item.lower()
        elif 'a'<=item<='z':
            return item.upper()
        else:
            return item

str1 = input('mjiretsu:')

str2 = map(fun,str1)

str3=tuple(str2)

print(''.join(str3))