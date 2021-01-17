class Person:
    age = None
    sex = None
    name = None

class worker(Person):
    def work(self,work):
        print("年龄为",self.age,"的",self.name,"正在干活！",work)

class student(Person):
    id = None
    def sing(self,sing):
        print("年龄为",self.age,"的",self.name,"的",self.id,"学生正在!" ,sing)

    def study(self, study):
        print("年龄为", self.age, "的", self.name, "的", self.id, "学生正在!", study)

w = worker()
w.name = "张三"
w.age = 13
w.sex = "女"
w.work("监工")

s = student()
s.name = "李四"
s.age = 21
s.sex = "男"
s.id = "1211111"
s.sing("唱歌")
s.study("学习")