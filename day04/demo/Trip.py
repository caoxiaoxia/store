def sum(x,y):
    s = x + y
    return s
print(sum(1,3))
print(sum(4,5))

# 定义一个方法，求和结果，无需返回，直接打印即可。
def sum(x,y):
    s = x + y
    print("求和结果为：", s)
sum(7,8)


# 定义方法，传入一个n，打印NxN的乘法表。具有功能单一性。不要讲一个方法即可一个功能又做其他功能。
def table(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,"x",i,"=",(i*j),"\t",end="")
        print()


n = int(input("请输入乘法表的层数："))
table(n)

def sum(x,y):
    return x + y

# a = 9  b = 3  c = 7
a = 9
b = 3
c = 7

s1 = sum(sum(a,b),c)
print(s1)