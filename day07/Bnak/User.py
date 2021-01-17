from day07.Bnak.ID import Address
class User:
    __account = ""
    __username = ""
    __password = ""
    __address = ""
    __money = 0
    __date = ""
    __bankname = ""

    def setAccount(self,account):
        self.__account = account
    def getAccount(self):
        return self.__account
    def setUsername(self,username):
        self.__username = username
    def getUsernamme(self):
        return self.__username
    def setPassword(self,password):
        self.__password = password
    def getPassword(self):
        return self.__password
    def setAddress(self,address):
        self.__address=address
    def getAddress(self):
        return self.__address
    def setMoney(self,money):
        self.__money = money
    def getMoney(self):
        return self.__money
    def setDate(self,date):
        self.__date = date
    def getDate(self):
        return self.__date
    def setBankname(self,bankname):
        self.__bankname=bankname
    def getBankname(self):
        return self.__bankname


    def usr(self):
        self.a=Address
        print(
            "账号为：",self.getAccount(),"\n"
            "用户名：",self.getUsernamme(),"\n"
            "密码为：",self.getPassword(),"\n"
            "地址为：","\n\t"
                "国家:",self.__address.getCountry(),"省份:",self.__address.getProvince(),"街道:",self.__address.getStreet(),"门牌号:",self.__address.getDoor(),
            "余额为：",self.getMoney(),"\n"
            "注册时间：",self.getDate(),"\n"
            "银行名称：",self.getBankname())

