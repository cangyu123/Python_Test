s = lambda a,b:a*b
print(type(s))

print(s(10,20))

str1 = [{'A':10,'B':20,'C':60,'D':40,'E':50},
        {'A':10,'B':20,'C':60,'D':40,'E':60},
        {'A':10,'B':20,'C':60,'D':40,'E':70}]

str2=sorted(str1,key = lambda s : s.get('E'),reverse=True)
print(str2)