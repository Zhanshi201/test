
password = ('a123456')
i = 3 # 剩余登陆次数

while True:
	PWD = input('请输入密码:')

	if PWD == password:
		print('登陆成功')
		break

	else: 
		i = i - 1
		print('密码错误，还有', i ,'次机会')
		if i == 0:
			break
			

	