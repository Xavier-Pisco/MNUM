'''
Intragração Numérica

Regra dos trapézios
Divide-se a área num número n de trapézios

intregral(x0 -> xn) y. dx = h/2 (y(0) + 2*y(1) + 2*y(2) + ... + 2* y(n-1) + y(n-1))
intregral(x0 -> x) y. dx = h/2 (y(0) + 2*somatório(1 -> n-1) y(i) + y(n-1))

sin(x)(0->pi):
n       4       8       16      32
h     pi/4    pi/8    pi/16   pi/32
s     1.896   1.9742  1.9936  1.9984
Erro
Absoluto

QC = (s' - s)/(s'' - s') ≃ 4
'''

import math

def g(x):
    return math.sin(x)

def trapezio_iteracoes(left,right,f,n):
    h = (left + right)/n
    area = f(left)
    for i in range(1,n):
        area += 2*f(i*h)
    area += f(right)
    area = area * h / 2
    print("Area: " + str(area))

def trapezio_qc(left, right, f, erro):
    contador = 1
    n = 2
    h = (right - left) / n
    s = f(left)
    s1 = f(left)
    s2 = f(left)
    for i in range(1,n):
        s += 2*f(i*h)
    s = (s + f(right))* h/2
    n *= 2
    h = (right - left) / n
    for i in range(1,n):
        s1 += 2*f(i*h)
    s1 = (s1 + f(right))* h/2
    n *= 2
    h = (right - left) / n
    for i in range(1,n):
        s2 += 2*f(i*h)
    s2 = (s2 + f(right)) * h/2
    print("Contador: " + str(contador) + "\tS: " + str(round(s,7)) + "\tS1: " + str(round(s1,7)) + "\tS2: " + str(round(s2,7)))
    while (abs(abs((s1-s)/(s2-s1)) - 4) > erro):
        s = s1
        s1 = s2
        s2 = f(left)
        n *= 2
        h = (right - left) / n
        for i in range(1,n):
            s2 += 2*f(i*h)
        s2 = (s2 + f(right)) * h/2
        print("Contador: " + str(contador) + "\tS: " + str(round(s,7)) + "\tS1: " + str(round(s1,7)) + "\tS2: " + str(round(s2,7)))

erro = 10**(-3)

#trapezio_iteracoes(0,math.pi,g,4)
#trapezio_qc(0,math.pi,g,erro)


'''
Método de Simpson

integral(x0 -> xn) y.dx = h/3 * (y0 + 4* somatorio(impares -> 2*n - 1)yi + 2* somatorio(pares -> 2*n - 2) + yn)

n = 4
0.75254
n = 8
0.16158
n = 16
0.20282

3D
integral(x0 -> xn) integral(y0, yn) f(x,y).dy.dx = hx*hy/9 * (somatorio dos vertices + 4*somatorio dos pontos medios + 16*centro)
'''

def simpson_iteracoes(f,left, right, n):
    s = f(left)
    h = (right - left) / (2*n)
    for i in range(1,2*n):
        if (i%2 == 0):
            s += 2*f(i*h)
        else:
            s += 4*f(i*h)
    s = (s + f(right)) * h/3
    return s

def simpson(f,left,right,erro):
    contador = 1
    n = 1
    n *= 2
    s = simpson_iteracoes(f,left,right,n)
    n *= 2
    s1 = simpson_iteracoes(f,left,right,n)
    n *= 2
    s2 = simpson_iteracoes(f,left,right,n)
    print("Contador: " + str(contador) + "\tS: " + str(round(s,15)) + "\tS1: " + str(round(s1,15)) + "\tS2: " + str(round(s2,15)))
    while (abs(abs((s1-s)/(s2-s1)) - 16) > erro):
        contador += 1
        s = s1
        s1 = s2
        n *= 2
        s2 = simpson_iteracoes(f,left,right,n)
        print("Contador: " + str(contador) + "\tS: " + str(round(s,15)) + "\tS1: " + str(round(s1,15)) + "\tS2: " + str(round(s2,15)))
        
erro = 10**(-2)

#print("s: " + str(simpson_iteracoes(g,0,math.pi, 16)))
#simpson(g,0,math.pi,erro)

def f(x,y):
    return math.sin(x+y);

def Simpson3D(f,xleft,xright,yleft,yright):
    hx = (xright - xleft) / 2
    hy = (yright - yleft) / 2
    s = 0
    s += f(0,0) + f(xright,0) + f(0, yright) + f(xright,yright)
    s += 4*(f(yleft,yleft + hy) + f(xleft + hx,yleft) + f(xleft + hx,yright) + f(xright,yleft + hy))
    s += 16*(f(xleft + hx,yleft + hy))
    s = s*hx*hy/9
    return s

print("s: " + str(Simpson3D(f,0,math.pi/2,0,math.pi/2)))


'''
1)
integral(0->4) (1-e^(-2x)) n0 = 4
a) Aplicar Simpson e calcular 3 QC sucessivos
b)    "    Trapézio "                 "

2) x    -2  0   2   4   6   8   10 
  f(x)  35  5  -10  2   5   3   20
Aplicar Simpson e Trapézios
'''

