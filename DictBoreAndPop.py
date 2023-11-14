#coding: shift-jis

lis1 = [1,2,3,4,5] #リストでkeyを定義
lis2 = ['Q','W','E','R','T']

dict1 = {key : value for key,value in zip(lis1,lis2)}#辞書作成
for item,value in dict1.items():#辞書遍歴
    print(item,'--->','value')

for item in dict1.items():#タプルの型式で遍歴
    print(item)

print('*'*30)

lis = list(dict1.keys()) #辞書の値をリストに変換
print(lis)
print(tuple(dict1.keys()))#タプルで変換
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
