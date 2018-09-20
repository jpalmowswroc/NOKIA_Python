def my_func(*args, glue=":"):
    lista = []
    lista1 = []
    for args in args:
        if len(args) > 3:
            lista.append(args)
    lista1 = glue.join(lista)
    return (lista1)

print(my_func('abdc', 'gfwdff', 'wd', 'd', 'dddd'))