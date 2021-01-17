class Cup:
    __height = 0
    __volume = 0
    __color = ""
    __texture = ""
    def setHeight(self,height):
        self.__height = height
    def getHeight(self):
        return self.__height
    def setVolume(self,volume):
        self.__volume = volume
    def getVolume(self):
        return self.__volume
    def setColor(self,color):
        self.__color = color
    def getColor(self):
        return self.__color
    def setTexture(self,texture):
        self.__texture = texture
    def getTexture(self):
        return self.__texture
    def bulk(self):
        print("存放的体积为：",self.getVolume(),"高为：",self.getHeight(),"颜色为：",self.getColor(),"使用的材质为：",self.getTexture())