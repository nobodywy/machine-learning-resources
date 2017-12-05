# -*- coding:utf-8 -*-
pattenfile = open('patten.txt','r',encoding='UTF-8')
lines = pattenfile.readlines()
question = input()
for line in lines:
    line = line.strip()
    print (line)
    words = line.split(':')
    print (words[0])
    if question == words[0]:
        types = words[1]
print (types)
pattenfile.close()