import random

lista = []

for i in range(0, 6, 1):
    losowa=int(random.randint(1,100))
    lista.append(losowa)

lista.sort()
print(lista)





