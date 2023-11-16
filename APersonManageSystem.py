import re
import time
import os

filename = 'Person.txt'

def menu():

    print('===================================情報管理システム===================================')
    print('-------------------------------------機能メニュー-------------------------------------')
    print('\t\t\t\t1.メッセージを入力')
    print('\t\t\t\t2.メッセージを削除')
    print('\t\t\t\t3.メッセージを修正')
    print('\t\t\t\t4.メッセージを検索')
    print('\t\t\t\t5.順序を並べる')
    print('\t\t\t\t6.人数を統計する')
    print('\t\t\t\t7.情報を公開する')
    print('\t\t\t\t8.Exit')
    print('======================================================================================')
    print()

def main():
    while True:
        menu()
        try:
            choice = int(input('操作を選択してください：'))

        except ValueError:
            print()
            print('入力エラー、再入力してください!!!')
            time.sleep(2)

        else:

            if choice not in [1,2,3,4,5,6,7,8]:
                print()
                print('入力エラー、再入力してください!!!')

            elif choice == 1:
                insert()

            elif choice == 2:
                delete()

            elif choice == 3:
                change()

            elif choice == 4:
                search()

            elif choice == 5:
                sort1()
                
            elif choice == 6:
                total()

            elif choice == 7:
                show()

            elif choice == 8:
                break

def insert():
    while True:        
        ID = ID_test()
        name = input('名前を入力してください：')
        age = age_test()
        date = date1()
        address = input('出身を入力してください：')
        school = input('卒業学校を入力してください：')
        per = {'ID':ID,'name':name,'age':age,'date':date,'address':address,'school':school}
        save(per)
        cho = input('入力を続けますか(y/n):')
        
        while cho != 'n' and cho != 'y':
            cho = input('入力エラー、再入力してください:')
            
        if cho == 'n':
            break

    
def ID_test():#ID正規表現フィルタ
    while True:
        ID = input('IDを入力してください(例:20230001):')
        pattern1 = '2023[0-9]{4}$'#ID正規表現
        if not re.match(pattern1,ID):
            print('ID型式は異常、再入力してください:')#型式入力エラー

        else:
            break

    return ID

def age_test():#年齢正規表現フィルタ
    while True:
        try:
            age = int(input('年齢を入力してください：'))
            if age >70 or age<18:
                print('年齢は正しくない！！！')

            else:
                break
            
        except ValueError:
            print('タイプエラー,再入力してください！！！')

    return age

def date1():#生年月日正規表現フィルタ
    
    while True:
        date = input('生年月日を入力してください(例:20001001):')
        pattern2 = '[0-9]{4}[0-9]{1,2}[0-9]{1,2}$'
        if not re.match(pattern2,date):
            print('年月型式は異常、再入力してください：')
        else:
            break

    return date
'''def check(per):#ユーザーもう存在するかどうかを判断
    flag = 0
    print('checking')
    with open(filename,'r') as perfile:
        print('checking2')     
        lis = perfile.readlines()
        print(lis)

    for item in lis:#異常あり
        item2 = dict(eval(item))
        print(item2.get('ID'),item2.get('name'))
        print(per.get('ID'),per.get('name'))
        if item2.get('ID') == per.get('ID'): #and item2.get('name') == per.get('name'):
            print('該当のユーザーはもう存在しています！')
            flag = 1
        else:
            flag = 0
    return flag'''

def save(per):
    per_list = []#list of souce files
    per2 = open(filename,'a+')  #ファイルを開く
    per3 = open(filename,'r')   #ファイルを読む
    lis = per3.readlines()  #ファイル内容をリストに付与
    flag = 0    #ユーザーもう存在するかどうかを判断

    for item in lis:

        item2 = dict(eval(item)) #dict型に変換
        if item2.get('ID') == per.get('ID'):    #ID判断
            print('該当のユーザーはもう存在しています！')   #ユーザーが存在している場合
            flag = 1#flag
    if flag == 0:     
        per_list.append(per)    #ユーザーは存在しない追加
        for item in per_list:   
            per2.write(str(item)+'\n')
    per2.close()
    per3.close()

def delete():
    flag = True
    flag2 = True
    pattern1 = '2023[0-9]{4}$'
    while flag:#ループ終了条件
        num = input('削除しようIDを入力してください:')
        if re.match(pattern1,num):#空判断
            if os.path.exists(filename):#ファイル存在判断
                with open(filename,'r') as perfile:#ファイル内容を読む
                    per_list = perfile.readlines()#ファイル内容をリストに付与
                    #print(per_list)
                for item in per_list:
                    d = dict(eval(item))
                    if d.get('ID') == num:#ID判断
                        per_list.remove(item)
                        
                        print('削除成功')
                    else:
                        print('該当のユーザーは存在しない！')
                        flag2 = False

                if flag2:
                    for item in per_list:
                        with open(filename,'w') as reperwrite:
                            reperwrite.write(str(item)+'\n')
            else:
                print('ファイルは存在しない！！')

        else:
            print('正しいIDを入力してください!')

        cho = input('削除を続けますか　y/n:')
        while cho != 'n' and cho != 'y':
            cho = input('入力エラー、再入力してください:')
        if cho == 'n':
            break
        
def change():
    flag2 = True
    
    if not os.path.exists(filename):
        print('ファイルは存在しない！！')
    
    else:
        with open(filename, 'r') as filelist:
            per_list2 = filelist.readlines()
            while True:
                per_list = []#出力重複利用
                writefile = open(filename, 'w')#データをチェンジする為ファイルを開く
                print('Mで終了')
                num = input('IDを入力してください:')#IDや終了指令
                if num == 'm':#終了指令
                    break
                for item in per_list2:
                    item2 = dict(eval(item))    
                    if item2.get('ID') == num:#ID判断
                        per_list.append(item2)
                        showper(per_list)
                        print('修正しよう内容を入力してください：')
                        item2['ID'] = ID_test()
                        item2['name'] = input('名前を入力してください：')
                        item2['age'] = age_test()
                        item2['date'] = date1()
                        item2['address'] = input('住所を入力してください：')
                        item2['school'] = input('卒業学校を入力してください：')
                        writefile.write(str(item2)+'\n')#新データを書き込む
                        print('修正しました！')
                        writefile.close()
                        flag2 = False
                        
                    else:
                        writefile.write(str(item2))#対象以外のデータは変わらずに再書き込む
                if flag2:
                    print('ユーザーは存在しない！')
                    
                cho = input('修正を続けますか　y/n:')
                while cho!= 'y' and cho!= 'n':
                    cho = input('入力エラー、再入力してください:')
                    
                if cho == 'n':
                    break

def search():
    flag = 0
    
    while True:
        per_list = []
        if not os.path.exists(filename):
            print('ファイルは存在しない！！')
        
        else:
            with open(filename, 'r') as rfile:
                per_list2 = rfile.readlines()
                Id = ID_test()
                
                for item in per_list2:#ファイル内容をリストに付与
                    item2 = dict(eval(item))
                    if item2.get('ID') == Id:#ID判断
                        per_list.append(item2)#転換後のデータを保存
                        flag = 1#detaが存在している場合
                        
                if flag == 0:
                    print('該当のユーザーは存在しない！')
                    
                else:
                    showper(per_list)    
                
        cho = input('検索を続けますか　y/n:')
        
        while cho!= 'y' and cho!= 'n':
            cho = input('入力エラー、再入力してください:')
            
        if cho == 'n':
            break
    
    
def sort1():
    per_list = []
    if os.path.exists(filename):
        with open(filename, 'r') as rfile:
            per_list2 = rfile.readlines()
            
        for item in per_list2:
            item2 = dict(eval(item))

            per_list.append(item2)
                
        asc_or_desc = int(input('IDで昇順、降順(0:昇順, 1:降順):'))
        if asc_or_desc == 0:
            cho = False
        elif asc_or_desc == 1:
            cho = True
            
        per_list.sort(key=lambda x: int(x.get('ID')), reverse=cho)
        showper(per_list)
        while True:
            ck = input('ファイルは存在しない,Mでメニューに戻る')
            if ck == 'm':
                break
            
    else:   
        while True:
            ret = input('ファイルは存在しない,mでメニューに戻る:')
            if ret == 'm':
                break

def total():
    per_list = []
    if os.path.exists(filename):
        with open(filename, 'r') as rfile:
            per_list2 = rfile.readlines()
        for item in per_list2:
            item2 = dict(eval(item))
            per_list.append(item2)

        print(f'人数:{len(per_list)}')

    else:
        print('file not found')
    
    while True:
        cho = input('mでメインメニューに戻る:')
        if cho == 'm':
            break
        else:
            print('入力エラー、再入力してください！')

def show():
    per_list = []#list of source files
    if not os.path.exists(filename):
        print('ファイルは存在しない！！')
        
    else:
        with open(filename, 'r') as rfile:
            per_list2 = rfile.readlines()
            for item in per_list2:
                item2 = dict(eval(item))
                per_list.append(item2)
                
            showper(per_list)
    cho = input('mでメニューに戻る:')
    while cho!= 'm':
        cho = input('入力エラー、再入力してください:')
        
        
def showper(lis):
    formater = '{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}'#テーブル型式

    if len(lis) == 0:
        print('ファイルにデータは存在しない、データを入力してください！')
        
    else:
        print(formater.format('ID','名前','年齢','生年月日','住所','卒業学校'))
        for item in lis:
            print(formater.format(item['ID'],item['name'],item['age'],item['date'],item['address'],item['school']))

if __name__ == '__main__':
    main()
