# -*- coding:utf-8 -*-
import gensim.models
from gensim.models import Word2Vec
from modeltype import Patten

class search_W2V:
    def __init__(self): 
        self.mod = gensim.models.KeyedVectors.load_word2vec_format('/home/wangy/QAsystem/word2vec/vector.bin',binary=True)
    
    def relation_list(self,list):
        relist = []
        for (rel,ans) in list:
            relist.append(rel)
        return relist

    def find_answer(self,list,requestion,type):
        relist = self.relation_list(list)
        max = 0
        requestion = Patten(requestion,type)
        #print(requestion)
        #print("list:",list,'\n')
        for ques in requestion :
            for reword in relist:
                try:
                    tmp = self.mod.similarity(ques,reword)
                    # vec_a = self.mod[ques]
                    # vec_b = self.mod[reword]
                    # print('vec_a:')
                    # print(vec_a)
                    # print(':::end:::')
                    if tmp > max:
                        max = tmp
                        ans_relation = reword
                except:
                    continue
        for (ans_re,ans) in list:
            if ans_relation == ans_re:
                return ans





