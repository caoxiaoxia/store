read = open("picture/景甜.jpg", "rb")
write = open("D:\\景甜1.jpg","wb")
data = read.read()
write.write(data)

read.close()
write.close()