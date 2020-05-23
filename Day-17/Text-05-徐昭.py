"""
目的：实现24点算法
作者：徐昭
"""
# J代表11，Q代表12，K代表13，A代表1
import itertools
import random

card_num = []  # 存放抽到的随机扑克牌
list_set = []  # 存放随机牌的组对
card_group = ()  # 调用牌组
symbols = ["+", "-", "*", "/"]  # 存放加减乘除运算符
card_one, card_two, card_thr, card_four = 0, 0, 0, 0  # 初始化，用以存放四张随机扑克牌的信息
result_one, result_two, result_thr, result_else = 0, 0, 0, 0  # 初始化，用以存放运算的计算结果
card_result = []  # 存放运算结果
card_value = []  # 保存结果打印信息


# 发牌器
def card_send():
    for i in range(4):
        card_num.append(int(random.random() * 100 % 13) + 1)  # （0—1）* 100变成0—100的数，与13取余以后取整变成0—12，加一变成0—13即扑克牌数字
    list_set = list(set(itertools.permutations(card_num, 4)))  # 返回四张卡牌的所有数学全排列方式
    return list_set  # 存放排列方式的列表


# 计算方法
card_list = card_send()  # 将生成的四张牌所有排列顺序放入card_list中


def card_compute():
    for i in range(len(card_list)):
        card_group = card_list[i]  # 遍历每一种排列方式
        card_one, card_two, card_thr, card_four = card_group[0], card_group[1], card_group[2], card_group[3]  # 四张牌分别赋值
        flag = False
        # 为防止循环运算体系上的数学逻辑报错，用try进行检测
        try:
            for s1 in symbols:
                """
                把进行一步后的运算结果存在result_one里
                """
                if s1 == "+":
                    result_one = card_one + card_two
                elif s1 == "-":
                    result_one = card_one - card_two
                elif s1 == "*":
                    result_one = card_one * card_two
                elif s1 == "/":
                    result_one = card_one / card_two
                for s2 in symbols:
                    """
                    把进行二步后的运算结果存在result_two里
                    """
                    if s2 == "+":
                        result_two = result_one + card_thr
                    elif s2 == "-":
                        result_two = result_one - card_thr
                    elif s2 == "*":
                        result_two = result_one * card_thr
                    elif s2 == "/":
                        result_two = result_one / card_thr
                    for s3 in symbols:
                        """
                        把进行三步后的运算结果存在result_thr里
                        可能有的其他运算结果(3、4张牌进行运算)放在result_else里
                        """
                        if s3 == "+":
                            result_thr = result_two + card_four
                            result_else = card_thr + card_four
                        elif s3 == "-":
                            result_thr = result_two - card_four
                            result_else = card_thr - card_four
                        elif s3 == "*":
                            result_thr = result_two * card_four
                            result_else = card_thr * card_four
                        elif s3 == "/":
                            result_thr = result_two / card_four
                            result_else = card_thr / card_four

                        # 判断最终结果是否为24
                        if result_thr == 24:
                            card_value.append("((%s %s %s) %s %s ) %s %s = 24" % (
                                card_one, s1, card_two, s2, card_thr, s3, card_four))
                            flag = True
                        # 括号与括号的运算
                        elif result_thr != 24 and 24 % result_one == 0:
                            for s4 in symbols:
                                result_thr = 0
                                if s4 == "+":
                                    result_thr = result_one + result_else
                                elif s4 == "-":
                                    result_thr = result_one - result_else
                                elif s4 == "*":
                                    result_thr = result_one * result_else
                                elif s4 == "/":
                                    result_thr = result_one / result_else
                                if result_thr == 24:
                                    card_value.append("(%s %s %s) %s (%s %s %s) = 24" % (
                                        card_one, s1, card_two, s4, card_thr, s3, card_four))
                                    flag = True
                                if flag:
                                    break
                        # 如果得到结果，就退出3次运算的循环
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


# 执行主体
if __name__ == "__main__":
    compute = card_compute()
    print("您抽中的扑克牌为：%s %s %s %s" % (card_list[0][0], card_list[0][1], card_list[0][2], card_list[0][3]))
    print("这组扑克牌共有 %s 种算法，可凑成24点：" % (len(compute)))
    print("---" * 15)
    count = 0  # 计算可行运算方式的数量
    for i in compute:
        count += 1
        print("第%d种：" % count, end='')
        print(i)
    print("---" * 15)
