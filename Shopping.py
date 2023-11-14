#coding: shift-jis

lis =[]
num = int(input('商品の数を入力してください：'))

for i in range (0,num):
    goods= input('商品の番号と商品名を入力してください：（例：1001シャツ）')
    lis.append(goods)

print('商品リスト：')
for index,value in enumerate(lis,start=1):
    print(index,'-->',value)

buy = []
while 1:

    good = input('検索の商品名を入力してください：(qで終了)')
    Flag = False

    for item in lis:
        if good == item[0:4]:
            buy.append(item)
            print('商品追加成功！！')
            Flag = True

    if Flag == 0 and good != 'q':
        print('該当商品は存在しない')

    if good =='q':
        break

buy.sort()
for item in buy:
    print(item[0:4],'-->',item[4:6])
