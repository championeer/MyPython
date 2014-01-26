# -*- coding: utf-8 -*-
# Filename:split_txt.py
path = raw_input('please enter the file path: ')
savepath = raw_input('please enter the save path:(not include the last \'\\\')')
newname = raw_input('please enter the new name:')
fr = file(path,'r')
flag = True
i = 0 #记录数
c = 1 #分割文件
while flag:
    line = fr.readline()
    i+=1
    if i < 1000001:         #分割1000000行
        save =savepath +'\\'+ newname + str(c) + ".txt"
        file(save,'a').write(line)
    else:
        i = 0    #记录数清零
        c+=1      #文件名+1
        continue   #继续循环
    if len(line) == 0:
        flag = False
fr.close()
#fs.close()
