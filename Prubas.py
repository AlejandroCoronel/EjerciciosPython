from datetime import datetime

def par(numero):
    if int(numero) % 2 == 0:
        return True
    else:
        return False

def primo(numero2):
    devolver = True
    contador = int(numero2) // 2
    for i in range(2, contador + 1):
        if int(numero2) % i == 0:
            devolver = False
    return devolver


ahora = datetime.now()
print(ahora.date())
print(ahora.time())
print('-----------------')
x = input('Ingrese un número: ')
if par(x):
    print('numero par')
else:
    print('numero impar')

if primo(x):
    print('numero primo')
else:
    print('numero no primo')

x = input('Ingrese la cantidad de números primos que desea listar: ')
print('-----------------')

j = 1
for m in range(1,int(x) + 1):
    while not primo(j):
        j += 1
    print(j)
    j += 1