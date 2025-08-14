
#Loja1
loja1 = {"Sansung J2 Prime", "Moto E6 Plus", "Iphone 12 Pro Max"}

#Loja2
loja2 = {"Sansung J2 Prime", "Moto E6 Plus", "Xiaomi Redmi"}


print(loja1)
print(loja2)

#Quantos modelos de smartphones estão disponíveis nas duas lojas
print("Modelos disponíveis em ambas as lojas:",loja1.intersection(loja2))

#Quantos modelos de smartphones estão disponíveis no total
print("Modelos disponíveis no total:", (loja1.union(loja2)))