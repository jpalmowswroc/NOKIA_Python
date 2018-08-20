lista = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
a = len(lista)

for i in range(a):
        print(lista[i])

for b in range(3):
    listab = [] 

    for i in range(a):
         listab.append(lista[i][b])
        
    print(listab)

