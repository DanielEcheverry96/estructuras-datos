def sumarLista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + sumarLista(lista[1:])


print(sumarLista([1, 3, 5, 7, 9]))
