#coding: shift-jis

Dict_Ticket = {
    'KN1001' : ['秦野->東京','ホーム1','12:12','13:12',60],
    'KN1002' : ['秦野->大阪','ホーム2','12:13','14:13',121],
    'KN1003' : ['秦野->京都','ホーム3','12:14','15:15',181],
    'KN1004' : ['秦野->福岡','ホーム4','12:15','16:16',241],
    'KN1005' : ['秦野->横浜','ホーム5','12:16','13:17',61]
    }
print('車両     始発      出発     発車      到着    経過')
for key in Dict_Ticket.keys():
    print(key,end=' ')
    for value in Dict_Ticket.get(key):
        print(value,end = '   ')
    print()
print()

ticket = input('購入の車両を選択ください：')
key1 = Dict_Ticket.get(ticket,'該当車存在しない')

person = []
if key1 != '該当車存在しない':
    num  = int(input('乗車者人数：'))
    for i in range (num):
        name = input('乗車者：')
        person.append(name)

    print(ticket+'車両を購入しました。')
    
    for i in range (num):
        print(person[i],end='さん,')
    print(key1[0]+'の乗車ホームは'+key1[1]+'です,'+'発車時間は'+key1[2]+'です'+'到着時間は'+key1[3]+'で'+'およそ'+str(key1[4])+'分かかります。')

else:
    print(key1)