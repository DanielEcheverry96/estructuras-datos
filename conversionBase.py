def conversionBase(num, base):
    cadena = "0123456789ABCDEF"

    if num < base:
        return cadena[num]
    else:
        return conversionBase(num // base, base) + cadena[num % base]


print(conversionBase(528, 7))
