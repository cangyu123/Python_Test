#coding: shift-jis

num = int(input('�Ј����F'))
lis = [i for i in range(0,num)]
for i in range(0,num):
    print('�N��F',end='')
    lis[i] = int(input())
    
print('�N��X�g�F')
print(lis)

for index in range(len(lis)):
    if lis[index]>23:
        lis[index] = lis[index] + 1900

    else:
        lis[index] = lis[index] + 2000


print(lis)