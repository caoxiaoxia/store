class Calculator:
    def add(self, num1,num2):
         return num1 + num2

    def sub(self,num1,num2):
        return num1 - num2

    def mul(self,num1,num2):
        return num1 * num2

    def div(self,num1,num2):
        return num1 / num2

C = Calculator()
while True:
    num1 = float(input("请输入第一个数："))
    num2 = float(input("请输入第二个数："))
    print("1:加法  2：减法  3：乘法  4：除法  5:退出")
    choose = input("请输入选项：")
    if choose == '1':
        print("结果为：", C.add(num1, num2))
    elif choose == '2':
        print("结果为：", C.sub(num1, num2))
    elif choose == '3':
        print("结果为：", C.mul(num1, num2))
    elif choose == '4':
        print("结果为：",C.div(num1, num2))
    else:
        break