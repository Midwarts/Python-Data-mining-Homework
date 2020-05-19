n = 0
while n<3:
    a = int(input('请输入密码'))
    correct = 865
    if a == correct:
        print('登陆成功')
    else:
        print('用户名或密码错误，若连续3次错误则自动锁死账号')
    n+=1
print('因连续3次输入用户名或密码错误，账号已锁死')