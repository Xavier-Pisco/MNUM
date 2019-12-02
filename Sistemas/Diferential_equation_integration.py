'''
Método de ordem 1 (euler)

Xn+1 = Xn + h
Yn+1 = Yn + h*Y'(Xn,Yn)

QC = 2

Quanto menor o h, melhor a solução


Método de ordem 2

Xn+1 = Xn + h
Yn+1 = Yn + h*Y'(Xn + h/2, Yn + h/2 * Y'(Xn,Yn))

Método de ordem 4
Xn+1 = Xn + h
Yn+1 = Yn + 1/6dy1 + 1/3dy2 + 1/3dy3 + 1/6dy4
dy1 = h*Y'(Xn,Yn)
dy2 = h*Y'(Xn + h/2, Yn + dy1 / 2)
dy3 = h*Y'(Xn + h/2, Yn + dy2 / 2)
dy4 = h*Y'(Xn + h, Yn + dy3)
'''

'''
Exercício:
y' = x**2 + y**2
[0,1.4]
(x0,y0) = (0,0)
h = 0.1
'''

def f(x,y):
    return x**2+y**2

def QC(S,S1,S2):
    return (S1 - S)/(S2 - S1)

def SCalc(xmin,xmax,x,y,f,h):
    for i in range(0, int((xmax - xmin)/h) + 1):
        y += h*f(x,y)
        x += h

    return y


def SCalc2(xmin,xmax,x,y,f,h):
    for i in range(0, int((xmax - xmin)/h) + 1):
        y += h * f(x+h/2, y + h/2*f(x,y))
        x += h

    return y

def SCalc4(xmin,xmax,x,y,f,h):
    for i in range(0, int((xmax - xmin)/h) + 1):
        dy1 = h*f(x,y)
        dy2 = h*f(x + h/2, y + dy1 / 2)
        dy3 = h*f(x + h/2, y + dy2 / 2)
        dy4 = h*f(x + h, y + dy3)
        y += 1/6*dy1 + 1/3*dy2 + 1/3*dy3 + 1/6*dy4
        x += h

    return y

def diferential_integration(xmin,xmax,x,y,f,h, erro):
    contador = 1
    s = SCalc(xmin,xmax,x,y,f,h)
    h /= 2

    s1 = SCalc(xmin,xmax,x,y,f,h)
    h /= 2

    s2 = SCalc(xmin,xmax,x,y,f,h)
    h /= 2
    print(str(contador) + '\t  ' + str(round(s,5)) + '\t  ' + str(round(s1,5)) + '\t  ' + str(round(s2,5)) + '\t  ' + str(round(QC(s,s1,s2),2)))
    while(abs(QC(s,s1,s2) - 2) > erro):
        contador += 1
        s = s1
        s1 = s2
        s2 = SCalc(xmin,xmax,x,y,f,h)
        h /= 2
        print(str(contador) + '\t  ' + str(round(s,5)) + '\t  ' + str(round(s1,5)) + '\t  ' + str(round(s2,5)) + '\t  ' + str(round(QC(s,s1,s2),2)))


def diferential_integration2(xmin,xmax,x,y,f,h,erro):
    contador = 1
    s = SCalc2(xmin,xmax,x,y,f,h)
    h /= 2
    s1 = SCalc2(xmin,xmax,x,y,f,h)
    h /= 2
    s2 = SCalc2(xmin,xmax,x,y,f,h)
    h /= 2
    print(str(contador) + '\t  ' + str(round(s,5)) + '\t  ' + str(round(s1,5)) + '\t  ' + str(round(s2,5)) + '\t  ' + str(round(QC(s,s1,s2),2)))
    while (abs(QC(s,s1,s2) - 4) > erro):
        contador += 1
        s = s1
        s1 = s2
        s2 = SCalc2(xmin,xmax,x,y,f,h)
        h /= 2
        print(str(contador) + '\t  ' + str(round(s,5)) + '\t  ' + str(round(s1,5)) + '\t  ' + str(round(s2,5)) + '\t  ' + str(round(QC(s,s1,s2),2)))


def diferential_integration4(xmin,xmax,x,y,f,h,erro):
    contador = 1
    s = SCalc4(xmin,xmax,x,y,f,h)
    h /= 2
    s1 = SCalc4(xmin,xmax,x,y,f,h)
    h /= 2
    s2 = SCalc4(xmin,xmax,x,y,f,h)
    h /= 2
    print(str(contador) + '\t  ' + str(round(s,5)) + '\t  ' + str(round(s1,5)) + '\t  ' + str(round(s2,5)) + '\t  ' + str(round(QC(s,s1,s2),2)))
    while (abs(QC(s,s1,s2) - 16) > erro):
        contador += 1
        s = s1
        s1 = s2
        s2 = SCalc4(xmin,xmax,x,y,f,h)
        h /= 2
        print(str(contador) + '\t  ' + str(round(s,5)) + '\t  ' + str(round(s1,5)) + '\t  ' + str(round(s2,5)) + '\t  ' + str(round(QC(s,s1,s2),2)))

x = 0
y = 0
xmin = 0
xmax = 1.4
h = 0.1
erro = 10**(-2)
#diferential_integration(xmin,xmax,x,y,f,h,erro)
#diferential_integration2(xmin,xmax,x,y,f,h,erro)
#diferential_integration4(xmin,xmax,x,y,f,h,erro) #NOT WORKING


'''
Sistemas

Euler
Xn+1 = Xn + h
Yn+1 = Yn + h*Y'(Xn,Yn,Zn)
Zn+1 = Zn + h*Z'(Xn,Yn,Zn)

RK2
Xn+1 = Xn + h
Yn+1 = Yn + h * Y'(Xn + h/2, Yn + h/2 *  Y'(Xn,Yn,Zn), Zn + h/2 * Z'(Xn,Yn,Zn))
Zn+1 = Zn + h * Z'(Xn + h/2, Yn + h/2 *  Y'(Xn,Yn,Zn), Zn + h/2 * Z'(Xn,Yn,Zn))
'''

'''
Exercicio:
dy/dx = -0.5*y
dz/dx = 4 - 0.3*z - 0.1*y

(X0,Ỹ0,Z0) = (0,4,6)
h = 0.5
X0 = 0
Xn = 2
'''

def g1(x,y,z):
    return -0.5*y

def g2(x,y,z):
    return 4 - 0.3*z - 0.1*y

def Euler(xmin,xmax,x,y,z,f,g,h):
    for i in range(0, round((xmax - xmin)/h)):
        y1 = y + h*f(x,y,z)
        z += h*g(x,y,z)
        y = y1
        x += h
    return (y,z)

def RK2(xmin,xmax,x,y,z,f,g,h):
    for i in range(0, round((xmax - xmin)/h)):
        y1 = y + h * f(x + h/2, y + h/2 *  f(x,y,z), z + h/2 * g(x,y,z))
        z += h * g(x + h/2, y + h/2 *  f(x,y,z), z + h/2 * g(x,y,z))
        y = y1
        x += h
    return (y,z)

def dif_int_sistemas(xmin,xmax,x,y,z,f,g,h,erro, Calc):
    contador = 1
    s = Calc(xmin,xmax,x,y,z,f,g,h)
    h /= 2
    s1 = Calc(xmin,xmax,x,y,z,f,g,h)
    h /= 2
    s2 = Calc(xmin,xmax,x,y,z,f,g,h)
    h /= 2
    print(str(contador) + '\t  ' + str(s) + '\t  ' + str(s1) + '\t  ' + str(s2) + '\t  ' + str(round(QC(s[0],s1[0],s2[0]),5)) + '\t' + str(round(QC(s[1],s1[1],s2[1]),5)))
    if (Calc(xmin,xmax,x,y,z,f,g,h) == RK2(xmin,xmax,x,y,z,f,g,h)):
        erro += 2
    while (abs(QC(s[0],s1[0],s2[0]) - 2) > erro or abs(QC(s[1],s1[1],s2[1]) - 2) > erro):
        contador += 1
        s = s1
        s1 = s2
        s2 = Calc(xmin,xmax,x,y,z,f,g,h)
        h /= 2
        print(str(contador) + '\t  ' + str(s) + '\t  ' + str(s1) + '\t  ' + str(s2) + '\t  ' + str(round(QC(s[0],s1[0],s2[0]),5)) + '\t' + str(round(QC(s[1],s1[1],s2[1]),5)))

x = 0
y = 4
z = 6
h = 0.5
xmin = 0
xmax = 2
erro = 10**(-2)
#dif_int_sistemas(xmin,xmax,x,y,z,g1,g2,h,erro, Euler)
#dif_int_sistemas(xmin,xmax,x,y,z,g1,g2,h,erro, RK2)

'''
dy/dx = z*y + x
dz/dx = z*x + y
(x0,y0,z0) = (0,1,1)
h = 0.05
x0 = 0

Aplicar Euler e RK2
a) Calcular o valor da função em x = 0.1 e x = 0.5
b) Calcular QC e erro para x = 0.5

'''

def h1(x,y,z):
    return z*y + x

def h2(x,y,z):
    return z*x + y

def Euler_sistemas(xi, xf, x,y,z, h, f1, f2):
    s = Euler(xi,xf,x,y,z,f1,f2,h)
    h /= 2
    s1 = Euler(xi,xf,x,y,z,f1,f2,h)
    h /= 2
    s2 = Euler(xi,xf,x,y,z,f1,f2,h)
    print((round(s[0],5),round(s[1],5)), (round(s1[0],5),round(s1[1],5)), (round(s2[0],5),round(s2[1],5)), round(QC(s[0],s1[0],s2[0]),5), round(QC(s[1],s1[1],s2[1]),5), round(s1[0] - s2[0],5), round(s1[1] - s2[1],5))


def RK2_sistemas(xi,xf,x,y,z,h,f1,f2):
    s = RK2(xi,xf,x,y,z,f1,f2,h)
    h /= 2
    s1 = RK2(xi,xf,x,y,z,f1,f2,h)
    h /= 2
    s2 = RK2(xi,xf,x,y,z,f1,f2,h)
    print((round(s[0],5),round(s[1],5)), (round(s1[0],5),round(s1[1],5)), (round(s2[0],5),round(s2[1],5)), round(QC(s[0],s1[0],s2[0]),5), round(QC(s[1],s1[1],s2[1]),5), round(s1[0] - s2[0],5), round(s1[1] - s2[1],5))

#Euler_sistemas(0,0.1,0,1,1,0.05,h1,h2)
#Euler_sistemas(0,0.5,0,1,1,0.05,h1,h2)
#RK2_sistemas(0,0.1,0,1,1,0.05,h1,h2)
#RK2_sistemas(0,0.5,0,1,1,0.05,h1,h2)

