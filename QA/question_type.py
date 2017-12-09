# -*- coding:utf-8 -*-
import commands
class questionType:
        def Person_type(self,list):
            for word in list:
                if word ==u'谁':
                    list.append(u'职业')
            return list

        def Number_type(self,list):
            for word in list:
                if word ==u'生日':
                    list.append(u'出生日期')
                if word ==u'时候':
                    list.append(u'日期')
                    list.append(u'时间')
            return list
        def Location_type(self,list):
            for word in list:
                if word ==u'哪':
                    list.append(u'地理位置')
                    list.append(u'所属地区')
                    list.append(u'地点')
                    list.append(u'')
                if word ==u'国人':
                    list.append(u'国籍')
            return list

        def ques_type_list(self,list,types):
            # file = open('D:/Desktop/Cstopword.txt','r')
            # stop_lists = file.readlines();
            # stop_list =[]
            # for stop_word in stop_lists:
            #     stop_word = stop_word.strip()
            #     stop_list.append(stop_word)
            # for word in list:
            #     if word in stop_list:
            #         list.remove(word)
            if types=='Person':
                list =self.Person_type(list)
                return list
            elif types=='Location':
                list =self.Location_type(list)
                return list
            return list

        #import os.path
        # def correct(question):
        #     jarpath = os.path.join(os.path.abspath('.'),'G:/Desktop/')
        #     startJVM(getDefaultJVMPath(),'-ea','-Djava.class.path=%s'%(jarpath+'pattern.jar'))
        #     JDClass = JClass("QA.tiny_QA.tinyQA")
        #     jd = JDClass()
        #     jprint = java.lang.System.out.printIn
        #     jprint(jd.GetPatten(question))
        #     shutdownJVM()
        def get_type(question):
            command = 'java -cp pattern.jar tinyQA '+question
            quesType = str(commands.getoutput(command))
            return quesType

