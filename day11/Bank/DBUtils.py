import pymysql

class DBUtils:
    host = "localhost"
    user = "root"
    password = "111111"
    database  = "company"
    con = None
    cursor = None
    def __init__(self,host="localhost",user="root",password="111111",database="company"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.con = pymysql.connect(host = self.host,
                        user = self.user,
                        password = self.password,
                        database = self.database)  # 将连接赋值给全局con
        self.cursor = self.con.cursor()
#   增删改：1 : 执行一条     2：多条
    def update(self,sql,param,mode="1"):
        if mode == "1":
            self.cursor.execute(sql,param)
        else:
            self.cursor.executemany(sql,param)
        self.con.commit()

    def select(self,sql,param,mode="all",size = 1):
        self.cursor.execute(sql,param) # 执行sql语句
        if mode == "all":  # 判断取值模式
            return self.cursor.fetchall()
        elif mode == "many":
            return self.cursor.fetchmany(size)
        elif mode == "one":
            return self.cursor.fetchone()

    # 释放资源
    def releaseConnection(self):
        self.cursor.close()
        self.con.close()

# db  = DBUtils()
# sql = "select * from t_employees where ename = %s"
# param = ["关二爷"]
# result = db.select(sql,param,mode="all")
# print(result)
# db.releaseConnection()
#

