#coding: shift-jis

lis =[]
num = int(input('���i�̐�����͂��Ă��������F'))

for i in range (0,num):
    goods= input('���i�̔ԍ��Ə��i������͂��Ă��������F�i��F1001�V���c�j')
    lis.append(goods)

print('���i���X�g�F')
for index,value in enumerate(lis,start=1):
    print(index,'-->',value)

buy = []
while 1:

    good = input('�����̏��i������͂��Ă��������F(q�ŏI��)')
    Flag = False

    for item in lis:
        if good == item[0:4]:
            buy.append(item)
            print('���i�ǉ������I�I')
            Flag = True

    if Flag == 0 and good != 'q':
        print('�Y�����i�͑��݂��Ȃ�')

    if good =='q':
        break

buy.sort()
for item in buy:
    print(item[0:4],'-->',item[4:6])
