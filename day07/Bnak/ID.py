class Address:
    __country = ""
    __province = ""
    __street = 0
    __door = 0

    def setCounty(self, country):
        self.__country = country

    def getCountry(self):
        return self.__country

    def setProvince(self, province):
        self.__province = province

    def getProvince(self):
        return self.__province

    def setStreet(self, street):
        self.__street = street

    def getStreet(self):
        return self.__street

    def setDoor(self, door):
        self.__door = door

    def getDoor(self):
        return self.__door

    def output(self):
        print("国家：",self.getCountry(),"\n""省份：",self.getProvince(),"\n""街道：",self.getStreet(),"\n""门牌号：",self.getDoor())