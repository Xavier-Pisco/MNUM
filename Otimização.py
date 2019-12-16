'''
Otimização Unidimensional
Pesquisa de extremos da função

Regra aurea
x3 = x1 + A(x2 - x1)
x4 = x1 + B(x2 - x1)

B = (sqrt(5) - 1)/2
A = B**2

if (f(x3) < f(x4)): 
    x2 = x4

elif (f(x4) < f(x3)):
    x1 = x3

Exercício:
f(x) = (2*x + 1)**2 - 5*cos(10*x)
Pesquisar min e max em [-1,0]
critério de paragem |x2-x1| < 10**(-3)
'''

from math import cos,sin,sqrt

def f(x):
    return (2*x + 1)**2 - 5*cos(10*x)


def otimizacao_unidimensional(x1,x2,erro,min):
    """
    x1,x2: min e máx do intervalo
    erro: erro máximo entre x2 e x1
    min: True se for o minímo, False se for o máximo
    """
    contador = 0
    number = (sqrt(5)-1)/2
    x3 = x1 + number**2 * (x2 - x1)
    x4 = x1 + number * (x2 - x1)
    while(abs(x2-x1) > erro):
        contador += 1
        if (min == True):
            if (f(x3) < f(x4)): 
                x2 = x4
            else:
                x1 = x3
        else:
            if (f(x3) > f(x4)): 
                x2 = x4
            else:
                x1 = x3

        x3 = x1 + number**2 * (x2 - x1)
        x4 = x1 + number * (x2 - x1)
    if (min == True):
        if (f(x1) < f(x2)):
            print(x1,f(x1))
        else:
            print(x2,f(x2))
    else:
        if (f(x1) > f(x2)):
            print(x1,f(x1))
        else:
            print(x2,f(x2))


#otimizacao_unidimensional(-1,0,10**(-3),True)
#otimizacao_unidimensional(-1,0,10**(-3),False)


'''
Otimização Multidimensional

1) Gradiente
X(n+1)i = X(n)i - h * gradiente(X(n)i)

*X(n)i -> X atual de ordem i, normalemnte ordem = x,y,z...

Se f(Xn+1) < f(Xn) h aumenta
Se f(Xn+1) > f(Xn) h diminui

Exercício:
    f(x,y): y**2 - 2*x*y - 6*y + 2*x**2 +12
    x0 = y0 = 1
    h0 = 1

    |Xn+1-Xn| < 10**(-3) para todos os i


2) Quádrica
X(n+1)i = X(n)i - H⁻¹ * gradiente(X(n)i)
H : Determinante das derivadas do número de variávies


3) Levemberg-Marquardt
X(n+1)i = X(n)i - h(X(n)i)

h(x) = a*gradiente(X(n)i) + H⁻¹ * gradiente(X(n)i)

if (f(x1) > f(x)):
    a += delta_a
else:
    a -= delta_a

Exercício anterior com a = 0.1, delta_a = 0.01
'''

def f(x,y):
    return y**2 - 2*x*y - 6*y + 2*x**2 +12

def fx(x,y):
    return -2*y + 4*x

def fy(x,y):
    return 2*y - 2*x - 6

def fxx(x,y):
    return 4

def fxy(x,y):
    return -2

def fyx(x,y):
    return -2

def fyy(x,y):
    return 2

def h(x,y):
    return fxx(x,y)*fyy(x,y) - fxy(x,y)*fyx(x,y)

def gradiente(x,y,erro):
    contador = 1
    h = 1
    x1 = x - h*fx(x,y)
    y1 = y - h*fy(x,y)
    while(abs(x1 - x) > erro or abs(y1 - y) > erro):
        if (f(x1,y1) < f(x,y)):
            h *= 2
            x = x1
            y = y1
        else:
            h /= 2

        x1 = x - h*fx(x,y)
        y1 = y - h*fy(x,y)
        contador += 1
    print("Contador: ", contador)
    print("x: ",x1, "\ty: ",y1)
    print("f(x,y): ",f(x,y))


def quadrica(x,y,erro):
    contador = 1
    x1 = x - 1/h(x,y) * fx(x,y)
    y1 = y - 1/h(x,y) * fy(x,y)
    while(abs(x1 - x) > erro or abs(y1 - y) > erro):
        x = x1
        y = y1
        x1 = x - 1/h(x,y) * fx(x,y)
        y1 = y - 1/h(x,y) * fy(x,y)
    print("Contador: ", contador)
    print("x: ",x, "\ty: ",y)
    print("f(x,y): ",f(x,y))


def lm(x,y,erro,a, delta):
    contador = 1
    x1 = x - (a*fx(x,y) + 1/h(x,y)*fx(x,y))
    y1 = y - (a*fy(x,y) + 1/h(x,y)*fy(x,y))
    while(abs(x1 - x) > erro or abs(y1 - y) > erro):
        if (f(x1,y1) > f(x,y)):
            a += delta
        else:
            a -= delta
        x = x1
        y = y1
        x1 = x - (a*fx(x,y) + 1/h(x,y)*fx(x,y))
        y1 = y - (a*fy(x,y) + 1/h(x,y)*fy(x,y))
    print("Contador: ", contador)
    print("x: ",x1, "\ty: ",y1)
    print("f(x,y): ",f(x,y))

gradiente(1,1,10**(-3))
quadrica(1,1,10**(-3))
lm(1,1,10**(-3),0.1,0.01)