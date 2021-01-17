from day10.Bank.View import view
from day10.Bank.User import User
from day10.Bank.Bank import Bank
from day10.Bank.Address import Address

def putmoney():
    bank = Bank()
    #存钱逻辑
    account = input("请输入您的账号：")
    money = int(input("请输入您的余额："))
    if bank.bankPutmoney(account, money):
        print("存款成功！")

def drawmoney():
    bank = Bank()
    account = input("请输入您的账号：")
    password = input("请输入您的密码：")
    money = int(input("请输入您的余额："))
    third = bank.bankDrawmoney(account,password,money)
    if third == 3:
        print("余额不足")
    elif third == 2:
        print("账号密码不正确")
    elif third == 1:
        print("账号不存在！")
    else:
        print("取款成功！")

def transfer():
    bank = Bank()
    account = input("请输入转入账号：")
    account1 = input("请输入转出账号：")
    password = input("请输入转出账号的密码：")
    money = int(input("请输入转出的金额："))
    fourth = bank.bankTransfer(account,account1,password,money)
    if fourth == 3:
        print("转出的金额不足")
    elif fourth == 2:
        print("密码错误")
    elif fourth == 1:
        print("对不起，您输入的账号不存在或同账户不能互转！")
    else:
        print("恭喜！转账成功!")

def query():
    bank = Bank()
    #查询逻辑
    account = input("请输入查询的账号：")
    password = input("请输入查询账号的密码：")
    bank.bankQuery(account,password)


def addUser():
    bank = Bank()
    # 开户逻辑
    username = input("请输入您的姓名：")
    password = input("请输入您的密码：")
    print("接下来要输入您的地址信息：")
    country = input("国家：")
    province = input("省份：")
    street = input("街道：")
    door = input("门牌号：")
    money = int(input("请输入您的余额："))

    address = Address(country,province,street,door)

    user = User(username=username,password=password,address=address,money=money)
    # user.setAddress(address)
    # user.setUsername(username)
    # user.setMoney(money)
    # user.setPassword(password)

    # 将上述数据传输给银行开户逻辑
    status = bank.bankAddUser(user)

    if status == 3:
        print("对不起，本银行用户库已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("对不起，您的个人信息已存在！请稍后再试！")
    elif status == 1:
        print("恭喜！开户成功！以上就是您的开户信息！")




while True:
    # 1.打印视图
    print(view)

    # 2.让用户输入 ,并判断输入是否合法
    choose=input("请输入您的业务编号:")# 输入
    if choose.isdigit():# 判断输入是否是数字
        if not int(choose) in range(1,7):# 业务编号是否在可控范围
            print("您的输入非法！请重新输入！")
            continue
        else:
            choose=int(choose)
    if choose == 1:
        addUser()
    elif choose ==2:
        putmoney()
    elif choose == 3:
        drawmoney()
    elif choose == 4:
        transfer()
    elif choose == 5:
        query()
    elif choose == 6:
        print("-------------------这位爷！欢迎下次光临!-------------------")
        exit(0) # 退出
























