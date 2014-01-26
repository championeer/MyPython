import os
import sys
import os.path
import random

def file_cut(txt):
   # if not os.path.isfile(txt):
    #    print txt,"is not a file."
     #   exit(1)
    txtfile = open(txt, "r")
    dirname = os.path.dirname(txt)
    #random.shuffle(txtfile)
    line_count = 0
    file_index = 0
    #将文本行随机处理，以便后面输出随机的行
    olines = []
    lines = txtfile.readlines() #读取文件为一个列表
    while lines:
        olines.append(lines.pop(random.randrange(len(lines)))) #将lines列表的内容变成随机的
    outfile = open(dirname+'test_%d'%(file_index)+'.txt','w')
    for line in olines: #遍历olines这个随机列表
        if line_count < 10:
            outfile.write(line)
            line_count += 1
        else:
            outfile.close()
            file_index += 1
            outfile = open(dirname+'test_%d'%(file_index)+'.txt','w')
            line_count = 0
    outfile.close()
    txtfile.close()

file_cut("h:\\0.txt")
