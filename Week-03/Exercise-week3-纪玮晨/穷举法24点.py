import itertools

cards = eval(input("请输入四个数字的列表："))

for nums in itertools.permutations(cards):# 四个数排列组合
    for ops in itertools.product('+-*/', repeat=3):#三个运算符排列组合
        # 构造三种中缀表达式
        s1 = '({0}{4}{1}){5}({2}{6}{3})'.format(*nums, *ops)  # (a+b)*(c-d)
        s2 = '(({0}{4}{1}){5}{2}){6}{3}'.format(*nums, *ops)  # (a+b)*c-d
        s3 = '{0}{4}({1}{5}({2}{6}{3}))'.format(*nums, *ops)  #  a/(b-(c/d))

        for i in [s1, s2, s3]: # 遍历
            try:
                if abs(eval(i) - 24.0) < 1e-10:   # eval函数
                    print(i)
            except ZeroDivisionError: # 零除错误！
                continue