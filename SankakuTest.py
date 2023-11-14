#coding: shift-jis

try:
    a = int(input('辺長を入力してください：'))
    b = int(input('辺長を入力してください：'))
    c = int(input('辺長を入力してください：'))

    if a+b>c and a+c>b and b+c>a:
        raise Exception(f'三角形の辺長は{a},{b},{c}です。')
    else:
        print('三角形にできません！！')

except ValueError:
    print('Type Error!!') #タイプ異常提示

except Exception as e:
    print(e)　#異常獲得出力