def my_func(flaga=True, name='my_string'):
    if flaga:
        print(name.upper())
    else:
        print(name.lower())


my_func(False, name='Jacek')
my_func(name='Jacek')