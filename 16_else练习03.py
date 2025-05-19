name = input("请输入用户名：")
if name == 'admin':
    print('欢迎admin')
if name == 'test':
    print('欢迎test')
else:
    print('查无此人')

username = input("请输入用户名：")
if username == 'admin' or username == 'test':
    print(f"欢迎进入本系统{username}")
else:
    print('查无此人')