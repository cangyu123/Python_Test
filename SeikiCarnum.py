#coding: shift-jis

import re

Car_Num = []
pattern1 = '[A-Z]{1}[0-9]{4}'

while True:
    test = input('�i���o�[�v���[�g����͂��Ă�������(q�ŏI��)�F')
    if test !='q':#���[�v�I���̏���
        if re.match(pattern1,test):#���Ă͂܂�i���o�[��ۑ�
            Car_Num.append(test)

        else:
            print(test,'�͓��Ă͂܂�Ȃ��I�I���������͂��Ă��������B')#�Ƃ�Ȃ��ꍇ�G���[�\��
    else:
        break

City_dict = {'A': 'Alpha','B':'Boston','C':'City','S':'Spain'}#�������̑Ή�����
for item in Car_Num:
    if City_dict.get(item[:1]):#���X�g���f�̓������Ŏ������璊�o
        print(item,'-->',City_dict[item[:1]])

    else:
        print('�Y���Ȃ�')

