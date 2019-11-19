import math

def a(x):
    return (((-x**4+x+1)/2)**(1/3))  #  x^4 + 2x^3 -x -1

def f(x):
    return 2*math.log(x) + 5

def fa(x):
    return math.e**((x-5)/2)

def g1(x,y):
    return math.sqrt((x*y+5*x-1)/2)

def g2(x,y):
    return math.sqrt(x+3*math.log(x))

def h1(x,y):
    return 2*x**2 - x*y - 5*x+1

def h2(x,y):
    return x+3*math.log(x) - y**2

def h1x(x,y):
    return 4*x-5-y

def h1y(x,y):
    return -x

def h2x(x,y):
    return 3/x+1

def h2y(x,y):
    return -2*y

def picardi(x,erro, func):
    temp = x
    x = func(temp)
    contador = 1
    print(str(contador) + '\t' + str(x) + '\t' + str(temp))
    while (abs(x - temp) > erro):
        contador += 1
        temp = x
        x = func(temp)
        print(str(contador) + '\t' + str(x) + '\t' + str(temp))

    print ("Zero: " + str(x) + '\n')

def picardi_sistema(x,y,erro,funcx,funcy):
    xtemp = x
    ytemp = y
    x = g1(xtemp,ytemp)
    y = g2(xtemp,ytemp)
    contador = 1
    print(str(contador) + '\t (' + str(x) + ',' + str(y) + ')')
    while (abs(x-xtemp) > erro or abs(y-ytemp) > erro):
        contador += 1
        xtemp = x
        ytemp = y
        x = g1(xtemp,ytemp)
        y = g2(xtemp,ytemp)
        print(str(contador) + '\t (' + str(round(x,7)) + ',' + str(round(y,7)) + ')')

    print ("Zero: (" + str(round(x,7)) + ',' + str(round(y,7)) + ')' + '\n')


def newton(x,y,erro, f1,f2,f1x,f1y,f2x,f2y):
    xtemp = x
    ytemp = y
    x = xtemp - (f1(xtemp,ytemp)*f2y(xtemp,ytemp) - f2(xtemp,ytemp)*f1y(xtemp,ytemp)) / (f1x(xtemp,ytemp) * f2y(xtemp,ytemp) - f1y(xtemp,ytemp) * f2x(xtemp,ytemp))
    y = ytemp - (f2(xtemp,ytemp)*f1x(xtemp,ytemp) - f1(xtemp,ytemp)*f2x(xtemp,ytemp)) / (f1x(xtemp,ytemp) * f2y(xtemp,ytemp) - f1y(xtemp,ytemp) * f2x(xtemp,ytemp))
    contador = 1
    print(str(contador) + '\t (' + str(x) + ',' + str(y) + ')')
    while (abs(x-xtemp) >= erro or abs(y-ytemp) >= erro):
        contador += 1
        xtemp = x
        ytemp = y
        x = xtemp - (f1(xtemp,ytemp)*f2y(xtemp,ytemp) - f2(xtemp,ytemp)*f1y(xtemp,ytemp)) / (f1x(xtemp,ytemp) * f2y(xtemp,ytemp) - f1y(xtemp,ytemp) * f2x(xtemp,ytemp))
        y = ytemp - (f2(xtemp,ytemp)*f1x(xtemp,ytemp) - f1(xtemp,ytemp)*f2x(xtemp,ytemp)) / (f1x(xtemp,ytemp) * f2y(xtemp,ytemp) - f1y(xtemp,ytemp) * f2x(xtemp,ytemp))
        print(str(contador) + '\t (' + str(round(x,7)) + ',' + str(round(y,7)) + ')')

    print ("Zero: (" + str(round(x,7)) + ',' + str(round(y,7)) + ')' + '\n')

x2 = 15
x1 = 0.01
erro = 10**(-5)

print()
#picardi(x1,erro,fa)
#picardi(x2,erro,f)

x = 4
y = 4

#picardi_sistema(x,y,erro,g1,g2)
#newton(x,y,erro,h1,h2,h1x,h1y,h2x,h2y)
picardi(0.6 ,erro,a)
