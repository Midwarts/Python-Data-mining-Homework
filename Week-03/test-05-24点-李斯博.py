

#在网上学习的代码，尽自己的努力对其进行的修改和改进

from random import randint
from itertools import permutations

#随机4个数字和2个运算符可能组成的表达式形式
exps = ('((%s %s %s) %s %s) %s %s',
        '(%s %s %s) %s (%s %s %s)',
        '(%s %s (%s %s %s)) %s %s',
        '%s %s ((%s %s %s) %s %s)',
        '%s %s (%s %s (%s %s %s))')
ops = r'+-*/'

def test24(v):
    result = []
    #这个函数对字符串表达式求值并验证是否等于24
    def check(exp):
        try:
            #有可能会出现除0异常，所以放到异常处理结构中
            return abs(float(eval(exp)) - 24) < 0.05
        except:
            return False
    #全排列，枚举4个数的所有可能顺序
    for a in permutations(v):
        #这4个数能实现24的表达式的种类
        t = [exp % (a[0], op1, a[1], op2, a[2], op3, a[3]) for op1 in ops for op2 in ops for op3 in ops for exp in exps if check(exp %(a[0], op1, a[1], op2, a[2], op3, a[3]))]
        if t:
            result.extend(t)
    return result

for i in range(20):
    print('='*20)
    #生成随机数字进行测试
    lst = [randint(1, 14) for j in range(4)]
    r = test24(lst)
    if r:
        for j in range(len(r)):
            print(r[j])
    else:
        print('No answer for ', lst)
