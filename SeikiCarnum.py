#coding: shift-jis

import re

Car_Num = []
pattern1 = '[A-Z]{1}[0-9]{4}'

while True:
    test = input('ナンバープレートを入力してください(qで終了)：')
    if test !='q':#ループ終了の条件
        if re.match(pattern1,test):#当てはまるナンバーを保存
            Car_Num.append(test)

        else:
            print(test,'は当てはまらない！！もう一回入力してください。')#嵌らない場合エラー表示
    else:
        break

City_dict = {'A': 'Alpha','B':'Boston','C':'City','S':'Spain'}#頭文字の対応辞書
for item in Car_Num:
    if City_dict.get(item[:1]):#リスト元素の頭文字で辞書から抽出
        print(item,'-->',City_dict[item[:1]])

    else:
        print('該当なし')

