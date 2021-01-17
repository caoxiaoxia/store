class Computer:
    __screensize = 0
    __price = 0
    __cputype = ""
    __memorysize = ""
    __time = 0

    def setScreensize(self,screensize):
        self.__screensize = screensize
    def getScreensize(self):
        return self.__screensize
    def setPrice(self,price):
        self.__price = price
    def getPrice(self):
        return self.__price
    def setCputype(self,cputype):
        self.__cputype = cputype
    def getCputype(self):
        return self.__cputype
    def setMemorysize(self,memorysize):
        self.__memorysize = memorysize
    def getMemorysize(self):
        return self.__memorysize
    def setTime(self,time):
        self.__time = time
    def getTime(self):
        return self.__time

    def type(self):
        print("正在打字！")
    def game(self):
        print("正在打游戏")
    def video(self):
        print("正在使用他看视频！")
