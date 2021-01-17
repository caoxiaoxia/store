'''
    1.去商场购物
        1.1 在浏览商城会展示一堆商品
        1.2 看见一堆商品，可以向您的购物车里添加一堆商品
        1.3 您的薪资减去钱。
    2.技术选型
        商品信息放到列表中。list []
        购物车也是list["方便面","辣条"]    list.append("辣条")
        买一个结算一个。
        买法：薪资够买这个商品，可以买。
            薪资不够，不能买，提示信息：您的钱不够
        买完之后，打印一个小条。（您的买商品，您的余额）
'''
import random
shop = [
    ["IPhone 8p",1000],
    ["Mac loptop",12000],
    ["IWatch",500],
    ["lenovo PC",4000],
    ["辣条",10],
    ["洗衣粉",23.5]
]

#1、展示您的商品
def showShop():
    for item, value in enumerate(shop):
        print(item, value)

#2、让用户输入自己的薪资
while True:
    salary = input("请输入您的薪资：")
    if salary.isdigit():    #isdigit() 判断某个字符串是否是数字组成
        salary = int(salary)
        break
    else:
        print("请输入合适的薪资")
# 我的购物车，里面是空
mycart = []
sum = 0
total = 0
# 3、开始购物
while True:
    # 3.1 先展示商品
    print("----------------欢迎来到某某某购物商城---------------------")
    showShop()

    # 3.2 请输入要买的编号
    chose = input("请输入您要买的编号：")
    if chose.isdigit():
        chose = int(chose)
        if chose >= len(shop):
            print("\033[41;20;1m您输入的商品他不存在！\033[0m")
        else:
            if salary < shop[chose][1]: # 如果钱不够
                print("\033[41;20;1m您的余额不足！下次再来吧!\033[0m")
            else:# 正常买东西，添加到我的购物车，薪资减去相对应的商品金钱
                mycart.append(shop[chose])
                salary = salary -shop[chose][1]
                sum = sum + shop[chose][1]
                print("\033[32;20;1m购买成功！您的余额为：",salary,"\033[0m")
    elif chose == 'Q' or chose == 'q':
        break
    else:
        print("您的输入不合法，请重新输入！")
if sum >= 0 and sum <= 5000:
    total = total + 200
else:
    total = total + 400
choice = ["满1000减200","满4000减800","满10000减1800"]
print("----------------欢迎下次再来---------------------")
print("以下就是您的购物信息：")
for item in mycart:
    print(item)
print("您的优惠券为：",random.choice(choice))
dis = 0
if random.choice(choice) == "满1000减200":
    dis=200
elif random.choice(choice) == "满4000减800":
    dis = 800
elif random.choice(choice) == "满10000减1800":
    dis = 1800
if sum >= dis:
    money = sum-dis
else:
    money = sum
print("您的应付金额为：",money)
print("您的余额为：",salary)
print("您消费的余额：",sum)
print("您的积分为：",total)


