from day10.Bank.DBUtils import DBUtils
from day10.Bank.View import user_info
from day10.Bank.View import user1_info
class Bank:
    __db = DBUtils(database="银行数据库")
    __bankName = "中国工商银行北京市沙河支行"

    def getBankName(self):
        return self.__bankName

    def bankAddUser(self,user):
        sql1 = "select count(1) from t_user"  # 查询是否已满的数据库
        sql = "select * from t_user where username = %s" # 检查是否存在该用户
        sql2 = "insert into t_user(" \
               "account,username,password,country," \
               "province,street,door,money,registerDate,bankname)" \
               " values(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"
        param = [user.getUsername()]
        if self.__db.select(sql1,None)[0][0] >= 100:
            return 3
        elif len(self.__db.select(sql,param)) != 0:
            return 2
        else:
            param1 = [
                user.getAccount(),
                user.getUsername(),
                user.getPassword(),
                user.getAddress().getCountry(),
                user.getAddress().getProvince(),
                user.getAddress().getStreet(),
                user.getAddress().getDoor(),
                user.getMoney(),
                user.getBankName()
            ]
            self.__db.update(sql2,param1)

            print(user_info.format(account=user.getAccount(),
                          username=user.getUsername(),
                          password=user.getPassword(),
                          country=user.getAddress().getCountry(),
                          province=user.getAddress().getProvince(),
                          street=user.getAddress().getStreet(),
                          door=user.getAddress().getDoor(),
                          money=user.getMoney(),
                          time=user.getRegisterDate(),
                          bank_name=user.getBankName()))
            self.__db.releaseConnection()
            return 1

    def selectUser(self,account,password):
        sql = "select * from t_user where account = %s  and password = %s"
        param = [account,password]
        result = self.__db.select(sql,param,mode="one")

        return result

    def bankPutmoney(self,account,money):
        sql = "select * from t_user where username = %s"
        sql2 = "select money from t_user where account = %s"
        sql3 = "update t_user set money = %s where account = %s"
        param = [account]
        a = self.__db.select(sql,param)
        if len(a) != 0:
            return 2
        else:
            a = self.__db.select(sql2, param,mode="one")
            a = a[0] + money
            param1 = [a, account]
            self.__db.update(sql3,param1)
            self.__db.releaseConnection()
            return True

    def bankDrawmoney(self,account,password,money):
        sql = "select * from t_user where username = %s"
        sql1 = "select * from t_user where account = %s  and password = %s"
        sql2 = "select money from t_user where account = %s"
        sql3 = "update t_user set money = %s where account = %s"
        param = [account]
        param1 = [account,password]
        a = self.__db.select(sql2, param,mode="one")
        if len(self.__db.select(sql,param)) != 0:
            return 1
        elif len(self.__db.select(sql1,param1)) != 0:
            if a[0] < money:
                return 3
            else:
                b = a[0] - money
                param2 = [b, account]
                self.__db.update(sql3, param2)
                return 0
        else:
                return 2

    def bankTransfer(self,account,account1,password,money):
        sql = "select * from t_user where username = %s"
        sql1 = "select * from t_user where account = %s  and password = %s"
        sql2 = "select money from t_user where account  = %s"
        sql3 = "update t_user set money = %s where account = %s"
        param = [account]
        param1 = [account1]
        param2 = [account,password]
        a = self.__db.select(sql2, param, mode="one")
        c = self.__db.select(sql2, param1, mode="one")
        if len(self.__db.select(sql,param)) != 0  and  len(self.__db.select(sql,param1)) != 0:
            if len(self.__db.select(sql1, param2)) != 0:
                if a[0] < money:
                    return 3
                else:
                    b = a[0] - money
                    d = c[0] + money
                    param3 = [b, account]
                    param4 = [c, account1]
                    self.__db.update(sql3, param3)
                    self.__db.update(sql3, param4)
                    return 0
            else:
                return 2
        else:
            return 1

    def bankQuery(self,account,password):
        bank = Bank()
        sql = "select * from t_user where account  = %s"
        sql2 = "select * from t_user where account  = %s and password = %s"
        param = [account]
        param1 = [account,password]
        if  len(self.__db.select(sql,param)) == 0:
            print("该用户不存在!")
        elif len(self.__db.select(sql2,param1)) == 0:
            print("密码错误！")
        else:
            database = bank.selectUser(account, password)
            print(user1_info.format(account=database[1],
                                   password=database[2],
                                   country=database[3],
                                   province=database[4],
                                   street=database[5],
                                   door=database[6],
                                   money=database[7],
                                   bank_name=database[8]))

