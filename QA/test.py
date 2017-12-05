import jieba.posseg as pseg


for item in pseg.cut(u'姚明的身高是多少？'):
    token, pos = item.word, item.flag
    print (token, pos)

