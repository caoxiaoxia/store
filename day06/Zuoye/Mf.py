f = open("scores.txt", "r+", encoding="utf-8")
line = f.readlines()
database = {}
for line in line:
    ites = line.replace("\n","").split(" ") # ["罗恩",56,12,36]
    database[ites[0]] = ites[1:]    # [start:end]  会从start角标开始提取到end结束

for i in database:
    sum = 0
    values = database[i] # ["56","12","36"]
    for value in values:
        sum = sum + int(value)
    print(i , "总分为：",sum)

f.close()


