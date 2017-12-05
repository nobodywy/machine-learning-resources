def Person_change(list):
    for word in list:
        if word ==u'谁':
            list.append(u'职业')
            list.remove(word)
    return list

def Number_change(list):
    for word in list:
        if word ==u'生日':
            list.append(u'出生日期')
        if word ==u'时候':
            list.append(u'日期')
            list.append(u'时间')
    return list
def Location_change(list):
    for word in list:
        if word ==u'哪':
            list.append(u'地区')
            list.remove(word)
        if word ==u'国人':
            list.append(u'国籍')
    return list

def Patten(list,pattens):
    # file = open('D:/Desktop/Cstopword.txt','r')
    # stop_lists = file.readlines();
    # stop_list =[]
    # for stop_word in stop_lists:
    #     stop_word = stop_word.strip()
    #     stop_list.append(stop_word)
    # for word in list:
    #     if word in stop_list:
    #         list.remove(word)
    if pattens=='Person':
        list =Person_change(list)
        return list
    elif pattens=='Location':
        list =Location_change(list)
        return list
    else:
        return list


