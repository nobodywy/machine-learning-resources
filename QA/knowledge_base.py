# -*-coding:utf-8-*-

import codecs

import global_data


class knowledge_base:
    def __init__(self):
        self.knowledge_base = {}

    def load(self, knowledge_base_file=global_data.knowledge_base_file_name):
        file_object = codecs.open(knowledge_base_file, 'r', encoding='utf-8')
        for i, line in enumerate(file_object.readlines()):
            try:
                subject, predicate, object = line.rstrip().split(' ||| ')
                if subject in self.knowledge_base:
                    self.knowledge_base[subject].append((predicate, object))
                else:
                    self.knowledge_base[subject] = [(predicate, object)]
            except:
                continue
        file_object.close()
        print('Loading knowledge base finished.')

    def show(self, total=30):
        for i, entity in enumerate(self.knowledge_base.keys()):
            print(entity)
            for predicate, object in self.knowledge_base[entity]:
                print(predicate, object)
            if i > total:
                break

    def show_knowledge(self, entity):
        if entity in self.knowledge_base:
            return (entity, self.knowledge_base[entity])
        else:
            return (entity, '')


if __name__ == '__main__':
    kb = knowledge_base()
    kb.load()
    # kb.print()
    entity = input()
    print(kb.show_knowledge(entity))
    # print(kb.show_knowledge("计算机应用基础"))
