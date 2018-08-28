liczba = int(input('Podaj liczbe'))

try:
    if liczba%2 == 0:
        raise ValueError
    if liczba < 0:
        raise TypeError
    if liczba > 10:
        raise IndexError

except ValueError:
    print('Liczba parzysta.')
except TypeError:
    print('Liczba mniejsza od zera.')
except IndexError:
    print('Liczba wieksza od 10.')



