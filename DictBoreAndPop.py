#coding: shift-jis

lis1 = [1,2,3,4,5] #���X�g��key���`
lis2 = ['Q','W','E','R','T']

dict1 = {key : value for key,value in zip(lis1,lis2)}#�����쐬
for item,value in dict1.items():#�����՗�
    print(item,'--->','value')

for item in dict1.items():#�^�v���̌^���ŕ՗�
    print(item)

print('*'*30)

lis = list(dict1.keys()) #�����̒l�����X�g�ɕϊ�
print(lis)
print(tuple(dict1.keys()))#�^�v���ŕϊ�
print('*'*30)

value = list(dict1.values())
print(value)
value2 = tuple(dict1.values())
print(value2)

lis3 = list(dict1.items())
print(lis3)
tuple1 = tuple(dict1.items())
print(tuple1)
print('*'*30)

print(dict1.pop(2))
print(dict1)

print(dict1.popitem())
print(dict1)

print(dict1.pop(99,'noetit'))

dict1.clear()
print(dict1)
