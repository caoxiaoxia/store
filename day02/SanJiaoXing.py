a = int(input("请输入第一边："))
b = int(input("请输入第二边："))
c = int(input("请输入第三边："))

if( a > 0 and b > 0 and c > 0 and a + b > c and b + c >a and a +c >b):
    if(a ==b == c):
        print("等边三角形")
    elif(a==b|a==c|b==c):
        print("等腰三角形")
    else:
        print("三角形")
else:
    print("不能构成三角形")