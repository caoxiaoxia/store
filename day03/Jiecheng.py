'''
sum = 0
a = 1
for i in range(1,21):
    a = a*i
    sum = sum + a
print("20以内数阶乘和为：",sum)
'''

def func(n):    #‘定义递归函数实现求阶乘功能‘
    if n == 1:
        return 1
    else:
         return  n * func(n-1)
sum = 0
for i in range(1,21):
    sum = sum + func(i)
print("20以内数阶乘和为：",sum)