# -*- coding: utf-8 -*-
import os
import shutil
#木構造で深度検索
def search_dir(path,result):
    #保存元の分岐を得る
    child_files = os.listdir(path)
   # print('chile_files:%s'%(child_files))
    for child in child_files:
            #path\childというパスを得る
            child = os.path.join(path,child)
           # print(child)
            result.append(child)
            if os.path.isdir(child):
                search_dir(child,result)


input_path = input('input:')#元保存先
out_path = input('output:')

files = list()
MYNUM = 20

search_dir(input_path,files)
for file in files:
    print('Find:'+file)
    if os.path.isfile(file) and file.endswith('.txt'):

        print('Move:' + file)
        shutil.move(file,out_path)
