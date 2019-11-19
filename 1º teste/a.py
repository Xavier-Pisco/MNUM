import math

def f(x):
    return x**3+2*x**2+10*x-17

def g(x):
    return 3*x**2+4*x+10

def Picard(x,erro,func):
    temp =  x
    x = func(x)
    contador = 1
    print(str(contador) + '\t' + str(x))
    while(abs(x-temp) > erro):
        temp = x
        x = func(x)
        contador += 1
        print(str(contador) + '\t' + str(x))


def Newton_sistemas(x,y,erro,func1,func2,func1x,func1y,func2x,func2y):
    xtmp = x
    ytmp = y
    x = xtmp - (func1(xtmp,ytmp)*func2y(xtmp,ytmp) - func2(xtmp,ytmp)*func1y(xtmp,ytmp))/(func1x(xtmp,ytmp)*func2y(xtmp,ytmp)-func1y(xtmp,ytmp)*func2x(xtmp,ytmp))
    y = ytmp - (func2(xtmp,ytmp)*func1x(xtmp,ytmp) - func1(xtmp,ytmp)*func2x(xtmp,ytmp))/(func1x(xtmp,ytmp)*func2y(xtmp,ytmp)-func1y(xtmp,ytmp)*func2x(xtmp,ytmp))
    contador = 1
    print(str(contador) + '\t' + str((x,y)))
    while(abs((x-xtmp)/x) > erro or abs((y - ytmp)/y) > erro):
        xtmp = x
        ytmp = y
        x = xtmp - (func1(xtmp,ytmp)*func2y(xtmp,ytmp) - func2(xtmp,ytmp)*func1y(xtmp,ytmp))/(func1x(xtmp,ytmp)*func2y(xtmp,ytmp)-func1y(xtmp,ytmp)*func2x(xtmp,ytmp))
        y = ytmp - (func2(xtmp,ytmp)*func1x(xtmp,ytmp) - func1(xtmp,ytmp)*func2x(xtmp,ytmp))/(func1x(xtmp,ytmp)*func2y(xtmp,ytmp)-func1y(xtmp,ytmp)*func2x(xtmp,ytmp))
        contador += 1
        print(str(contador) + '\t' + str((x,y)))


def Picard_sistemas(x,y,erro,funcx,funcy):
    xtmp = x
    ytmp = y
    x = funcx(xtmp,ytmp)
    y = funcy(xtmp,ytmp)
    contador = 1
    print(str(contador) + '\t' + str((x,y)))
    while(abs(x-xtmp) > erro or abs(y - ytmp) > erro):
        xtmp = x
        ytmp = y
        x = funcx(xtmp,ytmp)
        y = funcy(xtmp,ytmp)
        contador += 1
        print(str(contador) + '\t' + str((x,y)))


def bissecao(a,b,erro,func):
    temp = a
    x = (a+b)/2
    contador = 1
    print(str(contador) + '\t' + str(x))
    while (abs((temp - x)/x) > erro):
        if (func(a)*func(x) == 0):
            break
        if (func(a)*func(x) < 0):
            temp = x
            b = x
            x = (a+b)/2
            contador += 1
        else:
            temp = x
            a = x
            x = (a+b)/2
            contador += 1
        print(str(contador) + '\t' + str(x))


def corda(a,b,erro,func):
    temp = a
    x = (a*func(b) - b*func(a))/(func(b) - func(a))
    contador = 1
    print(str(contador) + '\t' + str(x))
    while (abs((temp - x)/x) > erro):
        if (func(a)*func(x) == 0):
            break
        if (func(a)*func(x) < 0):
            temp = x
            b = x
            x = (a*func(b) - b*func(a))/(func(b) - func(a))
            contador += 1
        else:
            temp = x
            a = x
            x = (a*func(b) - b*func(a))/(func(b) - func(a))
            contador += 1
        print(str(contador) + '\t' + str(x))


def newton(x,erro,func,func1):
    temp = 0
    x = x - func(x)/func1(x)
    contador = 1
    print(str(contador) + '\t' + str(x))
    while(abs((temp - x)/x) > erro):
        temp = x
        x = x - func(x)/func1(x)
        contador += 1
        print(str(contador) + '\t' + str(x))

newton(0, 10**(-3),f,g)
