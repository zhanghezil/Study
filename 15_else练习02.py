name = input("请输入用户名：")
password = input("请输入密码：")
if name == 'admin' and password == '123456':
    print("请进入本系统")
else:
    print("登陆信息错误")
