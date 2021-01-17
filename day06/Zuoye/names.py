name={}

welcome='''
*****************************
*        用户使用系统        *
*****************************
*1.注册                     *
*2.登录                     *
*3.修改密码                 *
*4.退出                     *
*****************************
'''

'''file = open("name.txt","w+",encoding="utf-8")
input(file.write(""))'''
#登录
def login():
    f=open("names.txt","r+",encoding="utf-8")
    names=f.readlines()
    for item in names:
        its=item.split(",")
        name[its[0]]=its[1].replace("\n","")

    while True:
        username=input("请输入您的用户名：")
        password=input("请输入您的密码：")
        if username in name and password == name[username]:
            print("登陆成功")
            break
        else:
            print("登陆失败，用户名或密码错误！")

#注册和上传头像
def readnames():
    file = open("names.txt", "a+", encoding="utf-8")
    names = file.readlines()
    for item in names:
        its = item.split(",")
        name[its[0]] = {
            "username":its[0],
            "password":its[1],
            "sex":its[2],
            "age":its[3],
            "address":its[4],
            "path":its[5]
        }
    file.close()
def upData(username,password,sex,age,address,path):
    readnames()
    if username in name:
        print("用户已存在！")
    else:
        name[username] = {
            "username":username,
            "password":password,
            "sex":sex,
            "age":age,
            "address":address,
            "path":path
        }
        write = open("names.txt", "a+", encoding="utf-8")
        write.write("\r")
        for i in name[username]:
            write.write(name[username][i])
            if i == "path":
                write.write("")
            else:
                write.write(",")
        write.close()
def upPhoto(path):
    photo = open(path, "rb+")
    write = open("F:\测试技术开发\python\day06\Zuoye\picture1\photo.jpg", "wb")#  存放路径
    data = photo.read()
    write.write(data)
    write.close()
    photo.close()
    print("上传成功！")
def register():
    username = input("请输入用户名：")
    password = input("请输入密码：")
    sex = input("请输入性别：")
    age = input("请输入年龄：")
    address = input("请输入地址：")
    print("上传头像：")
    path1 = input("请输入头像路径：")
    last = ".jpg"
    path = path1 + last
    if path1 != path:
        path1 = path
    upData(username, password, sex, age, address, path1)
    upPhoto(path1)

#修改密码
def change():
    username=input("请输入您的用户名：")
    password=input("请输入您的密码：")
    if username in name:
        if password == name[username]["password"]:
            password1 = input("请输入新密码：")
            name[username]["password"] = password1
            write = open("names.txt", "w+", encoding="utf-8")
            for i in name:
                for j in name[i]:
                    write.write(name[i][j])
                    if j == "path":
                        write.write("")
                    else:
                        write.write(",")
            print("修改成功！")
        else:
            print("账号或密码错误！")

    else:
        print("账号不存在！")


while True:
    print(welcome)
    chose = input("请选择您要办的业务：")
    if chose =="1":
        register()
    elif chose=="2":
        login()
    elif chose=="3":
        change()
    elif chose=="4":
        print("再见")
        break
    else:
        print("您选择的业务不存在！")