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
    #���ı�����������Ա��������������
    olines = []
    lines = txtfile.readlines() #��ȡ�ļ�Ϊһ���б�
    while lines:
        olines.append(lines.pop(random.randrange(len(lines)))) #��lines�б�����ݱ�������
    outfile = open(dirname+'test_%d'%(file_index)+'.txt','w')
    for line in olines: #����olines�������б�
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
