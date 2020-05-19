import re
email = input("请输入需要判定的电子邮箱：")

pattern = r"[0-9a-zA-Z.]+@[0-9a-zA-Z.]+?com"

if re.match(pattern,email):
	print("邮箱地址有效！")
else:
	print("邮箱地址无效！")