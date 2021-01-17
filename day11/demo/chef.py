class Chef:
    __name = None
    __age = None

    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self,age):
        self.__age = age

    def getAge(self):
        return self.__age

    def steam_rice(self,Steamedrice):
        print("年龄为",self.__age,"的",self.__name,"大厨，正在做！",Steamedrice)

#c = Chef()
#c.setName("小小")
#c.setAge(21)
#c.steam_rice("蒸饭")

class Vegetables(Chef):
    def cook(self,num):
        print("正在炒",num)
    def steam_rice(self,Steamedrice):
        super().steam_rice(Steamedrice)

class Grandson(Vegetables):
    def cook(self,num):
        print("正在炒",num)
    def steam_rice(self,Steamedrice):
        super().steam_rice(Steamedrice)


V = Vegetables()
V.setName("小小")
V.setAge(21)
V.steam_rice("米饭")
V.cook("土豆丝")
S = Grandson()
S.setName("大大")
S.setAge(12)
S.steam_rice("米饭")
S.cook("鱼香肉丝")
