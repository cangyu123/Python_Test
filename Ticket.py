#coding: shift-jis

Dict_Ticket = {
    'KN1001' : ['�`��->����','�z�[��1','12:12','13:12',60],
    'KN1002' : ['�`��->���','�z�[��2','12:13','14:13',121],
    'KN1003' : ['�`��->���s','�z�[��3','12:14','15:15',181],
    'KN1004' : ['�`��->����','�z�[��4','12:15','16:16',241],
    'KN1005' : ['�`��->���l','�z�[��5','12:16','13:17',61]
    }
print('�ԗ�     �n��      �o��     ����      ����    �o��')
for key in Dict_Ticket.keys():
    print(key,end=' ')
    for value in Dict_Ticket.get(key):
        print(value,end = '   ')
    print()
print()

ticket = input('�w���̎ԗ���I�����������F')
key1 = Dict_Ticket.get(ticket,'�Y���ԑ��݂��Ȃ�')

person = []
if key1 != '�Y���ԑ��݂��Ȃ�':
    num  = int(input('��ԎҐl���F'))
    for i in range (num):
        name = input('��ԎҁF')
        person.append(name)

    print(ticket+'�ԗ����w�����܂����B')
    
    for i in range (num):
        print(person[i],end='����,')
    print(key1[0]+'�̏�ԃz�[����'+key1[1]+'�ł�,'+'���Ԏ��Ԃ�'+key1[2]+'�ł�'+'�������Ԃ�'+key1[3]+'��'+'���悻'+str(key1[4])+'��������܂��B')

else:
    print(key1)