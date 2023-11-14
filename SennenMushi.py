#coding: shift-jis

num = int(input('社員数：'))
lis = [i for i in range(0,num)]
for i in range(0,num):
    print('年齢：',end='')
    lis[i] = int(input())
    
print('年齢リスト：')
print(lis)

for index in range(len(lis)):
    if lis[index]>23:
        lis[index] = lis[index] + 1900

    else:
        lis[index] = lis[index] + 2000


print(lis)