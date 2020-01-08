import math

'''
------------FUNÇÕES GERAIS---------
'''

def qc(s,s1,s2):
    return abs((s1 - s)/(s2 - s1))

def determinante(x,y,fx, fy, gx, gy):
    return fx(x,y)*gy(x,y) - fy(x,y)*gx(x,y)


'''
------------------ENCONTRAR ZEROS DE FUNÇÕES E SISTEMAS DE 2 EQUAÇÕES------------
'''

def bissecao(a,b,f,n):
    """ Método da bisseção para encontrar um zero
    a,b: extremos esquerdo e direito do intervalo respetivamente
    f: função
    n: número de vezes a calcular
    print:   contador, extremo esquerdo, ponto médio, extremo direito
    return: ponto médio
    """
    contador = 0
    x = (a + b) / 2
    print(contador, a, x, b)
    for i in range(n):
        contador += 1
        if (f(x) * f(a) < 0):
            b = x
        else:
            a = x
        x = (a + b) / 2
        print(contador, a, x, b)
    return x

def corda(a,b,f,n):
    """ Método da corda para encontrar um zero
    a,b: extremos esquerdo e direito do intervalo respetivamente
    f: função
    n: número de vezes a calcular
    print:   contador, extremo esquerdo, ponto calculado, extremo direito
    return: ponto
    """
    contador = 0
    x = (f(a)*b - f(b)*a) / (f(a)-f(b))
    print(contador, a, x, b)
    for i in range(n):
        contador += 1
        if (f(a) * f(x) < 0):
            b = x
        else:
            a = x

        x = (f(a)*b - f(b)*a) / (f(a)-f(b))
        print(contador, a, x, b)
    return x


def tangente(x,f,f1,n):
    """ Método da tangente ou de Newton para encontrar um zero
    x: guess inicial
    f: função
    f1: derivada da função
    n: número de vezes a calcular
    print: contador, x
    return: ponto
    """
    contador = 0
    print(contador, x)
    for i in range(n):
        x = x - f(x) / f1(x)
        contador += 1
        if (f(x) == 0):
            return x
        print(contador, x)
    return x

def tangente_sistemas(x, y, f, fx, fy, g, gx, gy, n):
    """ Método da tangente ou Newton para encontrar um zero em sistemas
    x, y: guess inicial
    f, g: funções
    fx, fy, gx, gy: derivadas de primeira ordem em função de x e y
    n: número de vezes a calcular
    print: contador, x, y
    return: (x,y)
    """
    contador = 0
    print(contador, x, y)
    for i in range(n):
        contador += 1
        x1 = x - (f(x,y)*gy(x,y) - g(x,y)*fy(x,y)) / (fx(x,y) * gy(x,y) - fy(x,y) * gx(x,y))
        y = y - (g(x,y)*fx(x,y) - f(x,y)*gx(x,y)) / (fx(x,y) * gy(x,y) - fy(x,y) * gx(x,y))
        x = x1
        print(contador, x, y)
    return (x,y)


def picard(x, f, n):
    """ Método de Picard-Peano para encontrar um zero
    x: guess inicial
    f: função
    n: número de vezes a calcular
    print: contador, x
    return: x
    """
    contador = 0
    print(contador, x)
    for i in range(n):
        contador += 1
        x = f(x)
        print(contador, x)
    return x

def picard_sistemas(x, y, f, g, n):
    """ Método de Picard-Peano para encontrar um zero de sistemas
    x,y: guess inicial
    f,g: funções
    n: número de vezes a calcular
    print: contador, x, y
    return: (x,y)
    """
    contador = 0
    print(contador,x,y)
    for i in range(n):
        x1 = f(x,y)
        y = g(x,y)
        x = x1
        print(contador, x, y)
    return (x,y)


'''
------------------RESOLUÇÃO DE SISTEMAS DE 3 EQUAÇÕES------------
(facilemente adaptável para 4 ou mais equações)
'''

def gauss_jacobi(x, y, z, f, g, h, n):
    """Resolver sistemas de 3 equações usando o método Gauss-Jacobi
    f: 1ºa equação em função de y e z
    g: 2ºa equação em função de x e z
    h: 3ºa equação em função de x e y
    x, y, z: X0,Y0,Z0
    n: número de vezes a calcular
    print: contador, x, y, z
    return: (x,y,z)
    """
    contador = 0
    print(contador, x, y, z)
    for i in range(n):
        x1 = f(y,z)
        y1 = g(x,z)
        z = h(x,y)
        x = x1
        y = y1
        contador += 1
        print(contador, x, y, z)
    return (x,y,z)

def gauss_seidel(x, y, z, f, g, h, n):
    """Resolver sistemas de 3 equações usando o método Gauss-Seidel
    f: 1ºa equação em função de y e z
    g: 2ºa equação em função de x e z
    h: 3ºa equação em função de x e y
    x, y, z: X0,Y0,Z0
    n: número de vezes a calcular
    print: contador, x, y, z
    return: (x,y,z)
    """
    contador = 0
    for i in range(n):
        x = f(y,z)
        y = g(x,z)
        z = h(x,y)
        contador += 1
        print(contador, x, y, z)
    return (x,y,z)


'''
-------------------RESOLUÇÃO DE INTEGRAIS------------
'''

def trapezio(a, b, f, n):
    """Método do trapézio para integrais
    a, b: extremos do integral
    f: função que vai ser integrada
    n: número de divisões da função no intervalo
    return: area
    """
    h = (b - a)/n
    area = f(a)
    for i in range(1,n):
        area += 2*f(round(a + i*h,2))
    area += f(b)
    area = area * h / 2
    return area


def trapezio_duplo(xleft,xright, yleft,yright, f):
    """Método do trapézio para resolver integrais duplos de tamanho 2x2
    xletf, xright: extremos do integral de x
    yleft, yright: extremos do integral de y
    f: função que vai ser integrada
    return: solução
    """
    hx = (xright - xleft) / 2
    hy = (yright - yleft) / 2
    s = 0
    s += f(0,0) + f(xright,0) + f(0, yright) + f(xright,yright)
    s += 2*(f(yleft,yleft + hy) + f(xleft + hx,yleft) + f(xleft + hx,yright) + f(xright,yleft + hy))
    s += 4*(f(xleft + hx,yleft + hy))
    s = s*hx*hy/4
    return s

def simpson_iteracoes(left, right, f, n):
    """Método de Simpson para resolver integrais
    letf, right: extremos do integral
    f: função que vai ser integrada
    n: número de iterações
    return: solução
    """
    s = f(left)
    h = (right - left) / (2*n)
    for i in range(1,2*n):
        if (i%2 == 0):
            s += 2*f(round(left + i*h,2))
        else:
            s += 4*f(round(left + i*h,2))
    s = (s + f(right)) * h/3
    return s

def Simpson_duplo(xleft,xright,yleft,yright,f):
    """Método de Simpson para resolver integrais duplos de tamanho 2x2
    xletf, xright: extremos do integral de x
    yleft, yright: extremos do integral de y
    f: função que vai ser integrada
    return: solução
    """
    hx = (xright - xleft) / 2
    hy = (yright - yleft) / 2
    s = 0
    s += f(0,0) + f(xright,0) + f(0, yright) + f(xright,yright)
    s += 4*(f(yleft,yleft + hy) + f(xleft + hx,yleft) + f(xleft + hx,yright) + f(xright,yleft + hy))
    s += 16*(f(xleft + hx,yleft + hy))
    s = s*hx*hy/9
    return s


'''
--------------RESOLUÇÃO DE EQUAÇÕES DIEFERENCIAIS----------------
'''

def Euler(xmin,xmax,x,y,f,h):
    """Calculo de Euler para equações diferenciais
    xmin, xmax: x menor e x maior
    x,y: X0 e Y0
    f: função para diferenciar
    h: distância entre dois pontos
    return: y
    """
    for i in range(0, round((xmax-xmin)/h)):
        y += h*f(x,y)
        x += h

    return y


def RK2(xmin,xmax,x,y,f,h):
    """Calculo de Runge-Kutta de 2º grau para equações diferenciais
    xmin, xmax: x menor e x maior
    x,y: X0 e Y0
    f: função para diferenciar
    h: distância entre dois pontos
    return: y
    """
    for i in range(0, round((xmax - xmin)/h)):
        y += h * f(x+h/2, y + h/2*f(x,y))
        x += h

    return y


def RK4(xmin,xmax,x,y,f,h):
    """Calculo de Runge-Kutta de 4º grau para equações diferenciais
    xmin, xmax: x menor e x maior
    x,y: X0 e Y0
    f: função para diferenciar
    h: distância entre dois pontos
    return: y
    """
    for i in range(0, round((xmax - xmin)/h)):
        dy1 = h*f(x,y)
        dy2 = h*f(x + h/2, y + dy1 / 2)
        dy3 = h*f(x + h/2, y + dy2 / 2)
        dy4 = h*f(x + h, y + dy3)
        y += 1/6*dy1 + 1/3*dy2 + 1/3*dy3 + 1/6*dy4
        x += h

    return y

def diferential(xmin,xmax,x,y,f,h, n, Calc):
    """Cálculo de equações diferenciais de 1ª ordem
    xmin, xmax: x menor e x maior
    x,y: X0 e Y0
    f: função para diferenciar
    h: distância entre dois pontos
    n: numero de iterações
    Calc: Método para utilizar
    return: (s,s1,s2)
    """
    contador = 1
    s = Calc(xmin,xmax,x,y,f,h)
    h /= 2

    s1 = Calc(xmin,xmax,x,y,f,h)
    h /= 2

    s2 = Calc(xmin,xmax,x,y,f,h)
    h /= 2
    print(str(contador) + '\t  ' + str(round(s,5)) + '\t  ' + str(round(s1,5)) + '\t  ' + str(round(s2,5)) + '\t  ' + str(round(qc(s,s1,s2),5)))
    for i in range(n):
        contador += 1
        s = s1
        s1 = s2
        s2 = Calc(xmin,xmax,x,y,f,h)
        h /= 2
        print(str(contador) + '\t  ' + str(round(s,5)) + '\t  ' + str(round(s1,5)) + '\t  ' + str(round(s2,5)) + '\t  ' + str(round(qc(s,s1,s2),5)))
    return (s,s1,s2)

def Euler_sistemas(xmin,xmax,x,y,z,f,g,h):
    for i in range(0, round((xmax - xmin)/h)):
        y1 = y + h*f(x,y,z)
        z += h*g(x,y,z)
        y = y1
        x += h
    return (y,z)

def RK2_sistemas(xmin,xmax,x,y,z,f,g,h):
    for i in range(0, round((xmax - xmin)/h)):
        y1 = y + h * f(x + h/2, y + h/2 *  f(x,y,z), z + h/2 * g(x,y,z))
        z += h * g(x + h/2, y + h/2 *  f(x,y,z), z + h/2 * g(x,y,z))
        y = y1
        x += h
    return (y,z)

def RK4_sistemas(xmin,xmax,x,y,z,f,g,h):
    for i in range(0, round((xmax - xmin)/h)):
        dy1 = h*f(x,y,z)
        dz1 = h*g(x,y,z)
        dy2 = h*f(x + h/2, y + dy1 / 2, z + dz1/2)
        dz2 = h*g(x + h/2, y + dy1 / 2, z + dz1/2)
        dy3 = h*f(x + h/2, y + dy2 / 2, z + dz2/2)
        dz3 = h*g(x + h/2, y + dy2 / 2, z + dz2/2)
        dy4 = h*f(x + h, y + dy3, z + dz3)
        dz4 = h*g(x + h, y + dy3, z + dz3)
        y += 1/6*dy1 + 1/3*dy2 + 1/3*dy3 + 1/6*dy4
        z += 1/6*dz1 + 1/3*dz2 + 1/3*dz3 + 1/6*dz4
        x += h

    return (y,z)


def diferential_sistemas(xmin,xmax,x,y,z,f,g,h,n, Calc):
    """Cálculo de sistemas diferenciais de 1ª ordem ou equações de 2º grau
    xmin, xmax: x menor e x maior
    x,y,z: X0, Y0 e Z0
    f,g: funções para diferenciar
    h: distância entre dois pontos
    n: numero de iterações
    Calc: método para utilizar
    return: (s,s1,s2)
    """
    contador = 1
    s = Calc(xmin,xmax,x,y,z,f,g,h)
    h /= 2
    s1 = Calc(xmin,xmax,x,y,z,f,g,h)
    h /= 2
    s2 = Calc(xmin,xmax,x,y,z,f,g,h)
    h /= 2
    print(str(contador) + '\t  ' + str(s) + '\t  ' + str(s1) + '\t  ' + str(s2) + '\t  ' + str(round(qc(s[0],s1[0],s2[0]),5)) + '\t' + str(round(qc(s[1],s1[1],s2[1]),5)))
    for i in range(n):
        contador += 1
        s = s1
        s1 = s2
        s2 = Calc(xmin,xmax,x,y,z,f,g,h)
        h /= 2
        print(str(contador) + '\t  ' + str(s) + '\t  ' + str(s1) + '\t  ' + str(s2) + '\t  ' + str(round(qc(s[0],s1[0],s2[0]),5)) + '\t' + str(round(qc(s[1],s1[1],s2[1]),5)))
    return (s,s1,s2)


'''
-------------------OTIMIZAÇÃO----------------------
'''


def otimizacao_unidimensional(x1,x2,erro,min):
    """ Encontrar o mínimo/máximo de uma função
    x1,x2: min e máx do intervalo
    n: número de iterações
    min: True se for o minímo, False se for o máximo
    print: x, f(x)
    return x
    """
    contador = 0
    number = (sqrt(5)-1)/2
    x3 = x1 + number**2 * (x2 - x1)
    x4 = x1 + number * (x2 - x1)
    for i in range(n):
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
            return x1
        else:
            print(x2,f(x2))
            return x2
    else:
        if (f(x1) > f(x2)):
            print(x1,f(x1))
            return x1
        else:
            print(x2,f(x2))
            return x2


def gradiente(x,y,f,fx,fy,h,n):
    """ Encontrar o mínimo de uma função de duas variáveis
    x, y: ponto inicial
    f: função
    fx: derivada em ordem a x
    fy: derivada em ordem a y
    h: lambda
    n: número de iterações
    print: contador, x, y
    return: valor da função em x,y
    """
    contador = 1
    x1 = x - h*fx(x,y)
    y1 = y - h*fy(x,y)
    print(contador, x1, y1)
    for i in range(n - 1):
        if (f(x1,y1) < f(x,y)):
            h *= 2
            x = x1
            y = y1
        else:
            h /= 2

        x1 = x - h*fx(x,y)
        y1 = y - h*fy(x,y)
        contador += 1
        print(contador, x1, y1)
    return w(x1,y1)


def quadrica(x,y,f,fx,fy,fxx,fxy,fyx,fyy,n):
    """ Encontrar o mínimo de uma função de duas variáveis
    x, y: ponto inicial
    n: número de iterações
    f: função
    fx: derivada em ordem a x
    fy: derivada em ordem a y
    fxx,fxy,fyx,fyy: segundas derivadas
    print: contador, x, y
    return: valor da função em x,y
    """
    contador = 1
    x1 = x - 1/determinante(x,y,fxx,fxy,fyx,fyy) * fx(x,y)
    y1 = y - 1/determinante(x,y,fxx,fxy,fyx,fyy) * fy(x,y)
    for i in range(n):
        x = x1
        y = y1
        x1 = x - 1/determinante(x,y,fxx,fxy,fyx,fyy) * fx(x,y)
        y1 = y - 1/determinante(x,y,fxx,fxy,fyx,fyy) * fy(x,y)
        print(contador, x1, y1)
    return w(x1,y1)


def lm(x,y,f,fx,fy,fxx,fxy,fyx,fyy,n,a, delta):
    """ Encontrar o mínimo de uma função de duas variáveis
    x, y: ponto inicial
    f: função
    fx: derivada em ordem a x
    fy: derivada em ordem a y
    fxx,fxy,fyx,fyy: segundas derivadas
    n: número de iterações
    a, delta: don't really know
    print: contador, x, y
    return: valor da função em (x,y)
    """
    contador = 1
    x1 = x - (a*fx(x,y) + 1/determinante(x,y,fxx,fxy,fyx,fyy)*fx(x,y))
    y1 = y - (a*fy(x,y) + 1/determinante(x,y,fxx,fxy,fyx,fyy)*fy(x,y))
    for i in range(n):
        if (f(x1,y1) > f(x,y)):
            a += delta
        else:
            a -= delta
        x = x1
        y = y1
        x1 = x - (a*fx(x,y) + 1/determinante(x,y,fxx,fxy,fyx,fyy)*fx(x,y))
        y1 = y - (a*fy(x,y) + 1/determinante(x,y,fxx,fxy,fyx,fyy)*fy(x,y))
        print(contador, x1, y1)
    return w(x1,y1)


def f(x):
    return math.sqrt(1+(1.5*math.exp(1.5*x))**2)

s=simpson_iteracoes(0,2,f,4)
s1=simpson_iteracoes(0,2,f,8)
s2=simpson_iteracoes(0,2,f,12)

print(s,s1,s2)
print(qc(s,s1,s2))
