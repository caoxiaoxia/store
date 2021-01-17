i = 0
while i < 3:
    i = i + 1
    username = input("请输入您的用户名：")
    password = input("请输入您的密码：")
    if username == 'jason' and password == 'admin':
        print("用户名或密码正确！")
    else:
        print("用户名密码错误，请重新输入！")

print("对不起！机会只有三次，您的账号密码被锁定！")