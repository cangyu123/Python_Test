#coding: shift-jis

address = set()
num = int(input('人数：'))

for i in range (1,num+1):
    info = input(f'インフォメーション{i}入力してください：')

    address.add(info)

for item in address:
    print(item)
