x = chr(9)
cadena = 'esto es un tabulador' + str(x) + 'y nada mas' + str(x) + 'papamasa'
print(cadena)
lista = cadena.split(chr(9))
for p in lista:
    print(p)