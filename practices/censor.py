#-*- coding:utf-8 -*-
#���ı���ƥ��ĵ��ʱ��*��*�ĸ����뵥����ĸ������ͬ
def censor(text,word):
    text_list = text.split(' ')
    for i in range(len(text_list)):
        if text_list[i] == word:
            w = ''
            for j in range(len(word)):
                w = w + '*'
            text_list[i] = w
    text = ' '.join(text_list)
    return text
    
print censor("hey back hey","hey")
