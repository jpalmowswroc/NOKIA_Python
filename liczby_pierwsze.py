d = int(input("Podaj liczbe."))
liczby = []

for i in range(d):
    liczby.append(i)


for x in liczby: 
    for i in range(2, x):
       if x % i == 0:
          print (x, " dzieli się przez ", i)
          break
    else:
        print (x, " jest liczbą pierwszą")
