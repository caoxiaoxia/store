from day07.Bnak.User import User
from day07.Bnak.ID import Address

u = User()
u.setAccount("04901697")
u.setUsername("黎明")
u.setPassword("110236")
address = Address()
a = Address()
address.setCounty("中国")
address.setProvince("香港")
address.setStreet(21)
address.setDoor(12)
u.setAddress(address)
u.setMoney(3200)
u.setDate("2020-11-22")
u.setBankname("中国工商银行的昌平支行")
u.usr()



