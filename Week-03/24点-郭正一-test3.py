import itertools
import random

card_num = []  # 随机牌
list_set = []  # 随机牌组对
card_group = ()  # 调用
symbols = ["+", "-", "*", "/"]  #运算符
card_one, card_two, card_thr, card_four = 0, 0, 0, 0  # 四张随机牌的信息
result_one, result_two, result_thr, result_else = 0, 0, 0, 0  # 运算的计算结果
card_result = []  # 运算结果
card_value = []  # 保存

# J代表11，Q代表12，K代表13，A代表1

# 发牌
def card_send():
    for i in range(4):
        card_num.append(int(random.random() * 100 % 13) + 1)
    list_set = list(set(itertools.permutations(card_num, 4)))
    return list_set



card_list = card_send()


def card_compute():
    for i in range(len(card_list)):
        card_group = card_list[i]  # 遍历
        card_one, card_two, card_thr, card_four = card_group[0], card_group[1], card_group[2], card_group[3]  # 四张牌分别赋值
        flag = False
        # try检测
        try:
            for n1 in symbols:
                if n1 == "+":
                    result_one = card_one + card_two
                elif n1 == "-":
                    result_one = card_one - card_two
                elif n1 == "*":
                    result_one = card_one * card_two
                elif n1 == "/":
                    result_one = card_one / card_two
                    #存在result_one里
                for n2 in symbols:
                    if n2 == "+":
                        result_two = result_one + card_thr
                    elif n2 == "-":
                        result_two = result_one - card_thr
                    elif n2 == "*":
                        result_two = result_one * card_thr
                    elif n2 == "/":
                        result_two = result_one / card_thr
                        #存在result_two里
                    for n3 in symbols:
                        if n3 == "+":
                            result_thr = result_two + card_four
                            result_else = card_thr + card_four
                        elif n3 == "-":
                            result_thr = result_two - card_four
                            result_else = card_thr - card_four
                        elif n3 == "*":
                            result_thr = result_two * card_four
                            result_else = card_thr * card_four
                        elif n3 == "/":
                            result_thr = result_two / card_four
                            result_else = card_thr / card_four
                        # 判断最终结果是否为24
                        if result_thr == 24:
                            card_value.append("((%s %s %s) %s %s ) %s %s = 24" % (
                                card_one, n1, card_two, n2, card_thr, n3, card_four))
                            flag = True
                        elif result_thr != 24 and 24 % result_one == 0:
                            for n4 in symbols:
                                result_thr = 0
                                if n4 == "+":
                                    result_thr = result_one + result_else
                                elif n4 == "-":
                                    result_thr = result_one - result_else
                                elif n4 == "*":
                                    result_thr = result_one * result_else
                                elif n4 == "/":
                                    result_thr = result_one / result_else
                                if result_thr == 24:
                                    card_value.append("(%s %s %s) %s (%s %s %s) = 24" % (
                                        card_one, n1, card_two, n4, card_thr, n3, card_four))
                                    flag = True
                                if flag:
                                    break
                        # 得到结果即退出运算的循环
                        if flag:
                            break
                    if flag:
                        break
                if flag:
                    break
        except ZeroDivisionError:
            pass

    card_result = set(card_value)
    return card_result


if __name__ == "__main__":
    compute = card_compute()
    print("抽扑克牌为：%s %s %s %s" % (card_list[0][0], card_list[0][1], card_list[0][2], card_list[0][3]))
    print("共有 %s 种算法成24点：" % (len(compute)))
    print("---" * 15)
    count = 0  # 运算方式的数量
    for i in compute:
        count += 1
        print("第%d种：" % count, end='')
        print(i)
    print("---" * 15)


