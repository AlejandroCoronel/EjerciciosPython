def imprimeNumeros():
    for i in range(10,21):
        print(i)

def factorialSinRecursividad(x):
    m = x
    for i in range(1,x):
        m = m * (x - 1)
        x = x -1
    return m

def factorialRecursiva(x):
    if x > 1:
        return x * factorialRecursiva(x - 1)
    else:
        return 1

def numerosTriangulares(n):
    x = 0
    for i in range(1, n + 1):
        x = x + i
        print(i, x)

def imprimirParesEntre(x,y):
    for i in range(x, y + 1):
        if i % 2 == 0:
            print(i)

def imprimirFichasDomino():
    contador = 1
    for i in range(1,7):
        for j in range(i,7):
            print(contador,'(', i, j, ')')
            contador += 1

imprimirFichasDomino()
print('----------------')
numero = int(input('de 1 hasta que número desea ver sus factoriales?: '))
for i in range(1, numero + 1):
    print(i, ': ', factorialRecursiva(i))