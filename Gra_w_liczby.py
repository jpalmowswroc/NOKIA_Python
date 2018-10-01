import random

answer = random.randint(1,20)
guess = ''

print("Gra w liczby.")

while guess != answer:
    guess = int(input('Podaj liczbe z przedzialu od 1 do 20.: '))
    if guess > answer:
        print('Za duza liczba.')
    elif guess < answer:
        print('Za mala.')
    else:
        print('Wygrales.')