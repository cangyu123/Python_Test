# -*- coding: utf-8 -*-
import os
import shutil
#�؍\���Ő[�x����
def search_dir(path,result):
    #�ۑ����̕���𓾂�
    child_files = os.listdir(path)
   # print('chile_files:%s'%(child_files))
    for child in child_files:
            #path\child�Ƃ����p�X�𓾂�
            child = os.path.join(path,child)
           # print(child)
            result.append(child)
            if os.path.isdir(child):
                search_dir(child,result)


input_path = input('input:')
out_path = input('output:')

files = list()
MYNUM = 20

search_dir(input_path,files)
for file in files:
    print('Find:'+file)
    if os.path.isfile(file) and file.endswith('.txt'):

        print('Move:' + file)
        shutil.move(file,out_path)