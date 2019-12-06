'''
| 3   1   1 | 7 |
| 1   4   2 | 4 |
| 0   2   5 | 5 |
Resolver as 3 equações em ordem a x1, x2 e x3 respectivamente
Condição de convergência: valores da diagonal maior que a soma dos valores restantes da linha
Atualização dos guess através das equações
'''

import math

def f1(y,z):
    return (7-y-z)/3

def f2(x,z):
    return (4-x-2*z)/4

def f3(x,y):
    return (5-2*y)/5

def G_Jacobi(f1,f2,f3,x,y,z, erro):
    xtmp = x + 100*erro
    ytmp = y + 100*erro
    ztmp = z + 100*erro
    contador = 0
    while((abs(x-xtmp) > erro) or (abs(y-ytmp) > erro) or (abs(z-ztmp) > erro)):
        xtmp = x
        ytmp = y
        ztmp = z
        x = f1(ytmp, ztmp)
        y = f2(xtmp, ztmp)
        z = f3(xtmp, ytmp)
        contador += 1
        print("Contador: " + str(contador) + "\tX: " + str(round(x,7)) + "\tY: " + str(round(y,7)) + "\tZ: " + str(round(z,7)) )

def G_Seidel(f1,f2,f3,x,y,z,erro):
    xtmp = x + 100*erro
    ytmp = y + 100*erro
    ztmp = z + 100*erro
    contador = 0
    while((abs(x-xtmp) > erro) or (abs(y-ytmp) > erro) or (abs(z-ztmp) > erro)):
        xtmp = x
        ytmp = y
        ztmp = z
        x = f1(y, z)
        y = f2(x, z)
        z = f3(x, y)
        contador += 1
        print("Contador: " + str(contador) + "\tX: " + str(round(x,7)) + "\tY: " + str(round(y,7)) + "\tZ: " + str(round(z,7)) )

x = 0
y = 0
z = 0
erro = 10**(-3)
#G_Jacobi(f1,f2,f3,x,y,z,erro)
#print()
#G_Seidel(f1,f2,f3,x,y,z,erro)
