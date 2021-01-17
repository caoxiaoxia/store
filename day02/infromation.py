username = "曹小霞"
ID = "140422199920202027"
age = 22
sex = "女"
height = 1.57
weight = 45

info = '''
-----------------------个人信息存储---------------------
姓名：{username}
身份证号：{ID}
年龄：{age}岁
性别：{sex}
身高：{height}m
体重：{weight}kg
------------------------------------------------------
'''

print(info.format(username=username,ID = ID,age = age,sex = sex, height = height, weight = weight))