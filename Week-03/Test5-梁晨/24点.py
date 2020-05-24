import random
import itertools
def getallresult():
    list_card = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    A = 1
    J = 11
    Q = 12
    K = 13
    random.shuffle(list_card)  # 洗牌
    print(list_card)
    list_operator = ['+', '-', '*', '/']       #运算符
    list_four =[random.choice(list_card) for i in range(4)]  #随机取出4张牌
    print("你获得以下四张牌：")
    print(list_four)            #输出四张牌的值
    result_list = []          #储存四张牌全排列的列表
    # set() 用于去除重复的排列，itertools.permutations()用于生成全排列的各个组合
    for i in set(itertools.permutations(list_four, len(list_four))):
        result_list.append(list(i))

    result_list1 = []  #存储四个运算符的列表
    for j in set(itertools.product(list_operator,repeat=  4)):
        templist = list(j)
        templist.pop()    #在实际运算过程中，4个数只需要3个运算符，删掉最后一个运算符，保留3个运算符
        if templist not in result_list1:
            result_list1.append(templist)

    expression_list = []    #存放各个符合条件的表达式
    count = 0               #计数器
    for i in result_list:
        for j in result_list1:

            expression1 = str(i[0]) + j[0] + str(i[1]) + j[1] + str(i[2]) + j[2] + str(i[3])    #将各个数都转化为str类型

           #捕获异常，此处可能出现的是除数为0的异常
            try:
                result = eval(expression1)
            except:
                result = 0
            if result == 24:
                expression_list.append(expression1 + '=' + str(result))
                count += 1
            else:
                expression2 = '(' + str(i[0]) + j[0] + str(i[1]) + ')' + j[1] + str(i[2]) + j[2] + str(i[3])
                try:
                    result = eval(expression2)
                except:
                    result = 0
                if result == 24:
                    expression_list.append(expression2 + '=' + str(result))
                    count += 1
                else:
                    expression3 = str(i[0]) + j[0] + '(' + str(i[1]) + j[1] + str(i[2]) + ')' + j[2] + str(i[3])
                    try:
                        result = eval(expression3)
                    except:
                        result = 0
                    if result == 24:
                        expression_list.append(expression3 + '=' + str(result))
                        count += 1
                    else:
                        expression4 = str(i[0]) + j[0] + str(i[1]) + j[1] + '(' + str(i[2]) + j[2] + str(i[3]) + ')'
                        try:
                            result = eval(expression4)
                        except:
                            result = 0
                        if result == 24:
                            expression_list.append(expression4 + '=' + str(result))
                            count += 1           #计算结果为24则计数+1
    print("如下结果：")
    for each in expression_list:
        print(each)                #列出每一种可能的表达式
    print('一共有%d个表达式' % count)
