names = [
    ["何登勇","56","男","106","IBM", 500 ,"50"],
    ["曹东雪","19","女","230","微软", 501 ,"60"],
    ["刘营营", "19", "女", "210", "Oracle", 600, "60"],
    ["李汉聪", "45", "男", "230", "Tencent", 700 , "10"]
]
#1、统计每个人的平均薪资
sum=0
for i in range(0,len(names)):
    sum = sum + names[i][5]
print("平均薪资：",sum / 4)

#2、统计每个人的平均年龄
age = 0
for i in range(0,len(names)):
    age = age + int(names[i][1])
print("平均年龄：",age / 4)

#3、公司新来一个员工，张佳伟，45，男，220，alibaba，500,30，添加到列表中
for i in range(0,len(names)+1):
    a = ["张佳伟", "45", "男", "220", "alibaba", 500 , "30"]
names.append(a)
print("names=",names)

#4、统计公司男女人数
men = 0
women = 0
for i in range(0,len(names)):
    if names[i][2] == '男':
        men = men + 1
    else:
        women = women +1
print("男生的人数为：",men,"人","\n""女生的人数为：",women,"人")

#5、每个部门的人数
do50 = 0
do60 = 0
do10 = 0
do30 = 0
for i in range(0,len(names)):
    if names[i][6] == "50":
        do50 = do50 + 1
    elif names[i][6] == "60":
        do60 = do60 + 1
    elif names[i][6] == "10":
        do10 = do10 + 1
    elif names[i][6] == "30":
        do30 = do30 + 1
print("50这个部门的人数为：",do50,"人","\n""60这个部门的人数为：",do60,"人","\n""10这个部门的人数为：",do10,"人","\n""30这个部门的人数为：",do30,"人")