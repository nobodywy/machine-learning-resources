# -*-coding:utf-8-*-
import jieba
import jieba.posseg as pseg

from entity_extension import EntityExtension
from knowledge_base import knowledge_base
from search_W2V import search_W2V
from question_type import questionType

class Client:
    def get_knowledge(self, question):
        answer = kb.show_knowledge(question)
        if len(answer[1]) == 0:
            entity = self.get_pos(question)[0]
            #     别名表有错，先用原词查一遍
            answer = kb.show_knowledge(entity)
            if len(answer[1]) == 0:
                result = mid.search_entity(entity)
                answer = kb.show_knowledge(result)
        return answer

    def get_pos(self, question):
        s = pseg.cut(question)
        other = []
        for item in s:
            token, pos = item.word, item.flag
            if pos == 'nr':
                result = token
            else:other.append(token)
        print("entity:"+result+'\n')
        return (result, other)

if __name__ == '__main__':
    mid = EntityExtension()
    mid.load_alias()
    kb = knowledge_base()
    questype = questionType()
    kb.load()
    sear = search_W2V()
    c = Client()
    while True:
        print('Input question:')
        try:
            question = input()
            if(question == -1):
                break
            qtype = questype.get_type()
            #print(c.get_knowledge(question))
            list = c.get_knowledge(question)[1]
            requlist = c.get_pos(question)[1]
            requlist = questype.ques_type_list(requlist,qtype)
            print(sear.find_answer(list,requlist))
        except Exception as e:
            print("exception",e,'\n')
            print('不知道~')
            continue
