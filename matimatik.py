
hamisiyogan = "kaysar test".lower() #这是里全部变大
hamisikiqik = "kaysar test".upper() #这里是全部变小
baxtikiyogan = "kaysar test".capitalize() #这里第一个字母变大
tamtersi = "kaysar test".swapcase() #这里是相反变大或者变小
yuwitix = "++kaysar test".strip("+") #这里会删除你想要的部分

#以下是列表的优化方式
isim = "kaysar"
soyisim ="kahar"
yixi = 25

print("isim:{}\nsoyisim:{}\nyixi:{}.".format(isim,soyisim,yixi)) #这里是一个列表的优化表达方式{}这个表示obj也就是你表达的表


#这里是input方式,也就是提取用户数据的方法,更简单的说提取用户输入的数据
kisiisim = input("Ismigizni yizig :")
kisips = int(input("Mima Kirig :"))

#以下是基本课的总结,我们做了一个简单的测试BMI的功能,利用我们以上学的知识来制作.

sinig_kiloyug = int(input("Hazirki Kiloyugni Kir:"))
sinig_buyug = int(input("Hazirki Buyugni Kir:"))

print("*"*30)
sinig_bmi = (sinig_buyug+sinig_kiloyug)/0.45
print(f"BMI:{sinig_bmi}")
print("*"*30)

#以下是关于表也就是列表

