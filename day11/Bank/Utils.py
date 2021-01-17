import random
class Utils:
    # 获取8位随机账号
    def getRandom(self):
        ch = ["0","1","2","3","4","5","6","7","8","9"]
        str  = ""
        for i in range(8):
            str =  str + ch[int(random.random()*len(ch))]
        return str


