r = open("baidu_x_system.log","r+",encoding="utf-8")
lines = r.readlines()
ips = []
for item in lines:
    i = item.split(" ")
    ips.append(i[0])

for index,ip in enumerate(ips):
    if ip in ips[0:index]:
        continue
    num = ips.count(ip)
    print(ip,"出现了：",num)