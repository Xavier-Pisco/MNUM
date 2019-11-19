import math

def f(x):
    return x**10-1

def bissecao(a,b,erro):
    temp = 0
    x = (a+b)/2
    contador = 1
    while (abs(temp - x) > erro):
        print(str(contador) + '\t' + str(x))
        if (f(a)* f(x) > 0):
            a = x
            temp = x
            x = (a+b)/2
            contador += 1

        elif (f(a)*f(x) < 0):
            b = x
            temp = x
            x = (a+b)/2
            contador += 1

    print (str(contador) + '\t' + str(x) + '\n')
    print ("Zero: " + str(x) + '\n')


def corda(a,b,erro):
    temp = 0
    x = (a*f(b) - b*f(a))/(f(b)-f(a))
    contador = 1
    while (abs(temp - x) > erro):
        print(str(contador) + '\t' + str(x))
        if (f(a) * f(x) > 0):
            a = x
            temp = x
            x = (a*f(b) - b*f(a))/(f(b)-f(a))
            contador += 1
        
        elif (f(a) * f(x) < 0):
            b = x
            temp = x
            x = (a*f(b) - b*f(a))/(f(b)-f(a))
            contador += 1

    print(str(contador) + '\t' + str(x) + '\n')
    print ("Zero: " + str(x) + '\n')
        



a = 0
b = 1.5
erro = 10**(-5)

bissecao(a,b,erro)
corda(a,b,erro)