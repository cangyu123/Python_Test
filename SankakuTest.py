#coding: shift-jis

try:
    a = int(input('�Ӓ�����͂��Ă��������F'))
    b = int(input('�Ӓ�����͂��Ă��������F'))
    c = int(input('�Ӓ�����͂��Ă��������F'))

    if a+b>c and a+c>b and b+c>a:
        raise Exception(f'�O�p�`�̕Ӓ���{a},{b},{c}�ł��B')
    else:
        print('�O�p�`�ɂł��܂���I�I')

except ValueError:
    print('Type Error!!') #�^�C�v�ُ��

except Exception as e:
    print(e)�@#�ُ�l���o��