#coding: shift-jis

address = set()
num = int(input('�l���F'))

for i in range (1,num+1):
    info = input(f'�C���t�H���[�V����{i}���͂��Ă��������F')

    address.add(info)

for item in address:
    print(item)
