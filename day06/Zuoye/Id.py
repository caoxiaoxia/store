sft = input("请输入您的证件路径：")
read = open(sft, "rb")
write = open("D:\\景甜.jpg","wb")
data = read.read()
write.write(data)

read.close()
write.close()