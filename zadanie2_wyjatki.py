my_list = [1,2,3,4,5,6]

index = int(input("podaj index"))

try:
    if index <= len(my_list):
        print(my_list[index])
    if index > len(my_list):
        raise IndexError

except IndexError:
    print('Poza zakresem')



