from random import choice
from itertools import permutations

#定义一副牌和运算符
list1 = ['+','-','*',r'/']
list_card = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
A = 1
J = 11
Q = 12
K = 13

#随机抽取4张牌
card1 = choice(list_card)
card2 = choice(list_card)
card3 = choice(list_card)
card4 = choice(list_card)
list_four = [card1,card2,card3,card4]
print('抽出的4张牌是',str(list_four))

#穷尽4张牌的全排列
list_cards = []
for i in set(permutations(list_four, len(list_four))):
    list_cards.append(i)

#随机生成3个运算符并穷尽排列
list_operater = []
while True:
    if len(list_operater) < 64:
        operater1 = choice(list1)
        operater2 = choice(list1)
        operater3 = choice(list1)
        list2 = [operater1,operater2,operater3]
        if list2 not in list_operater:
            list_operater.append(list2)
    else:
        break

#开始运算
result_list = []
for i in list_cards:
    for j in list_operater:
        str1 = str(i[0]) + j[0] + str(i[1]) + j[1] + str(i[2]) + j[2] + str(i[3])
        try:
            result = eval(str1)
        except:
            result = 0
        if result == 24:
            result_list.append(str1)

#输出结果
if len(result_list) != 0:
    for i in result_list:
        print(str(i),'=24')
else:
    print('不能构成24')
