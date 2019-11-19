import math


def f(x):
    return x**4+2*x**3-x-1

def f1(x):
    return 4*x**2  + 6*x**2 - 1


def bissecao(a,b,erro,func):
    x = (a+b)/2
    temp = x+erro*10000
    contador = 1
    if (func(a) == 0):
        return a
    if (func(b) == 0):
        return b
    while (abs(x-temp) > erro):
        if (func(x) == 0):
            return x

        if (func(x) * func(a) < 0):
            b = x
            temp = x
            print(str(contador) + '\t' + str(x))
            x = (a+b)/2
            contador += 1

        elif (func(x) * func(a) > 0):
            a = x
            temp = x
            print(str(contador) + '\t' + str(x))
            x = (a+b)/2
            contador += 1

    return x

def corda(a,b,erro,func):
    x = (a*f(b)-b*f(a))/(f(b)-f(a))
    temp = x + erro * 10000
    contador = 1
    if (func(a) == 0):
        return a
    if (func(b) == 0):
        return b
    while (abs(x-temp) > erro):
        if (func(x) == 0):
            return x

        if (func(x) * func(a) < 0):
            b = x
            temp = x
            print(str(contador) + '\t' + str(x))
            x = (a*f(b)-b*f(a))/(f(b)-f(a))
            contador += 1

        elif (func(x) * func(a) > 0):
            a = x
            temp = x
            print(str(contador) + '\t' + str(x))
            x = (a*f(b)-b*f(a))/(f(b)-f(a))
            contador += 1
    return x

def tangente(x,erro,func,func1):
    temp = x + erro * 10000
    x = x - func(x)/func1(x)
    contador = 1
    print(str(contador) + '\t' + str(x))
    while (abs(x-temp) > erro):
        if (func(x) == 0):
            return x

        else:
            temp = x
            x = temp - func(temp)/func1(temp)
            contador += 1
            print(str(contador) + '\t' + str(x))

    return x



casas_decimais = 5
erro = 10**(-(casas_decimais+1))

print("Zero: " + str(bissecao(0,1,erro,f)))
print ("Zero: " + str(corda(0,1,erro,f)))
print("Zero: " + str(tangente(1,erro,f,f1)))
