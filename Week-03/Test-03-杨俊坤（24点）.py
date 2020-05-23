'''
对于任意给定的四张牌，计算是否有构成24的方法，如果有的话给出所有的可能方法。
'''
import random
from itertools import permutations
from itertools import product

number=list(range(1,13))
color=['方片','梅花','红桃','黑桃']  #抽取花色
Card1=random.choice(number)
Card2=random.choice(number)
Card3=random.choice(number)
Card4=random.choice(number)
Color1=random.choice(color)  #抽取数字
Color2=random.choice(color)
Color3=random.choice(color)
Color4=random.choice(color)
print('抽取的四张牌为：',Color1,Card1,',',Color2,Card2,',',Color3,Card3,',',Color4,Card4)
Card=[Card1,Card2,Card3,Card4]
Card_zuhe=permutations(Card,4)   #对所有数字进行去全排列，使用itertools.permutations来完成
Card_list=[]
for i in Card_zuhe:
    Card_list.append(i)

sign_of_operation=['+','-','*',r'/']
x=product(sign_of_operation,repeat=3)           #用itertools.product对运算符号全排列
Sign_list=[]
for i in x:
    Sign_list.append(i)

result_list=[]
for i in Card_list:                        #这里网上查的都看不懂 就用了一下郑妍同学的思路
    for j in  Sign_list:
        str1 = str(i[0]) + j[0] + str(i[1]) + j[1] + str(i[2]) + j[2] + str(i[3])
        result=eval(str1)      #eval() 函数用来执行一个字符串表达式，并返回表达式的值
        if result !=24:
            pass
        if result ==24:
            result_list.append(str1)

if len(result_list)>0:
    print('可以组成24点，结果如下：')
    for i in result_list:
     print(str(i),'=24')
else:
    print('无法组成24点')

