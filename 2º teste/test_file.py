import math

def QC(S,S1,S2):
    return abs((S1 - S)/(S2 - S1))

# RESOLUÇÃO DE SISTEMAS

def G_Jacobi(f1,f2,f3,x,y,z, erro):
    """Resolver sistemas de 3 equações usando o método Gauss-Jacobi
    f1: 1ºa equação em função de y e z
    f2: 2ºa equação em função de x e z
    f3: 3ºa equação em função de x e y
    x, y, z: X0,Y0,Z0
    erro: erro da solução
    """
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
    """Resolver sistemas de 3 equações usando o método Gauss-Seidel
    f1: 1ºa equação em função de y e z
    f2: 2ºa equação em função de x e z
    f3: 3ºa equação em função de x e y
    x, y, z: X0,Y0,Z0
    erro: erro da solução
    """
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


# RESOLUÇÃO DE INTEGRAIS

def trapezio_iteracoes(left,right,f,n):
    """Método do trapézio para integrais por iterações
    letf, right: extremos do integral
    f: função que vai ser integrada
    n: número de divisões da função no intervalo
    """
    h = (right - left)/n
    area = f(left)
    for i in range(1,n):
        area += 2*f(i*h)
    area += f(right)
    area = area * h / 2
    print("Area: " + str(area))

def trapezio_qc(left, right, f, erro):
    """Método do trapézio para integrais por QC
    letf, right: extremos do integral
    f: função que vai ser integrada
    erro: erro máximo da solução
    """
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


def simpson_iteracoes(left, right, f, n):
    """Método de Simpson para resolver integrais por iterações
    letf, right: extremos do integral
    f: função que vai ser integrada
    n: número de iterações
    """
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
    """Método de Simpson para resolver integrais por QC
    letf, right: extremos do integral
    f: função que vai ser integrada
    erro: erro máximo da solução
    """
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


def Simpson_duplo(xleft,xright,yleft,yright,f,n):
    """Método de Simpson para resolver integrais por iterações
    xletf, xright: extremos do integral de x
    yleft, yright: extremos do integral de y
    f: função que vai ser integrada
    n: número de iterações
    """
    hx = (xright - xleft) / 2
    hy = (yright - yleft) / 2
    s = 0
    s += f(0,0) + f(xright,0) + f(0, yright) + f(xright,yright)
    s += 4*(f(yleft,yleft + hy) + f(xleft + hx,yleft) + f(xleft + hx,yright) + f(xright,yleft + hy))
    s += 16*(f(xleft + hx,yleft + hy))
    s = s*hx*hy/9
    return s

# RESOLUÇÃO DE EQUAÇÕES DIFERENCIAIS

def Euler(xmin,xmax,x,y,f,h):
    """Calculo de Euler para equações diferenciais
    xmin, xmax: x menor e x maior
    x,y: X0 e Y0
    f: função para diferenciar
    h: distância entre dois pontos
    """
    for i in range(0, int((xmax - xmin)/h) + 1):
        y += h*f(x,y)
        x += h

    return y


def RK2(xmin,xmax,x,y,f,h):
    """Calculo de Runge-Kutta de 2º grau para equações diferenciais
    xmin, xmax: x menor e x maior
    x,y: X0 e Y0
    f: função para diferenciar
    h: distância entre dois pontos
    """
    for i in range(0, int((xmax - xmin)/h) + 1):
        y += h * f(x+h/2, y + h/2*f(x,y))
        x += h

    return y

def RK4(xmin,xmax,x,y,f,h):
    """Calculo de Runge-Kutta de 4º grau para equações diferenciais
    xmin, xmax: x menor e x maior
    x,y: X0 e Y0
    f: função para diferenciar
    h: distância entre dois pontos
    """
    for i in range(0, int((xmax - xmin)/h) + 1):
        dy1 = h*f(x,y)
        dy2 = h*f(x + h/2, y + dy1 / 2)
        dy3 = h*f(x + h/2, y + dy2 / 2)
        dy4 = h*f(x + h, y + dy3)
        y += 1/6*dy1 + 1/3*dy2 + 1/3*dy3 + 1/6*dy4
        x += h

    return y

def diferential(xmin,xmax,x,y,f,h, erro, Calc):
    """Cálculo de equações diferenciais de 1ª ordem
    xmin, xmax: x menor e x maior
    x,y: X0 e Y0
    f: função para diferenciar
    h: distância entre dois pontos
    erro: erro da solução
    Calc: Método para utilizar
    """
    contador = 1
    s = Calc(xmin,xmax,x,y,f,h)
    h /= 2

    s1 = Calc(xmin,xmax,x,y,f,h)
    h /= 2

    s2 = Calc(xmin,xmax,x,y,f,h)
    h /= 2
    if (Calc(x,y) == Euler):
        value = 2
    elif (Calc(x,y) == RK2(x,y)):
        value = 4
    elif (Calc(x,y) == RK4(x,y)):
        value = 16
    print(str(contador) + '\t  ' + str(round(s,5)) + '\t  ' + str(round(s1,5)) + '\t  ' + str(round(s2,5)) + '\t  ' + str(round(QC(s,s1,s2),2)))
    while(abs(QC(s,s1,s2) - value) > erro):
        contador += 1
        s = s1
        s1 = s2
        s2 = Calc(xmin,xmax,x,y,f,h)
        h /= 2
        print(str(contador) + '\t  ' + str(round(s,5)) + '\t  ' + str(round(s1,5)) + '\t  ' + str(round(s2,5)) + '\t  ' + str(round(QC(s,s1,s2),2)))

# MESMO MAS PARA SISTEMA DE 3 EQUAÇÕES DIFERENCIAIS

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
        dy4 = h*f(x + h, y + dy3, z + dz3/2)
        dz4 = h*g(x + h, y + dy3, z + dz3/2)
        y += 1/6*dy1 + 1/3*dy2 + 1/3*dy3 + 1/6*dy4
        z += 1/6*dz1 + 1/3*dz2 + 1/3*dz3 + 1/6*dz4
        x += h

    return (y,z)

def diferential_sistemas(xmin,xmax,x,y,z,f,g,h,erro, Calc):
    """Cálculo de sistemas diferenciais de 1ª ordem
    xmin, xmax: x menor e x maior
    x,y,z: X0, Y0 e Z0
    f,g: funções para diferenciar
    h: distância entre dois pontos
    erro: erro da solução
    Calc: método para utilizar
    """
    contador = 1
    s = Calc(xmin,xmax,x,y,z,f,g,h)
    h /= 2
    s1 = Calc(xmin,xmax,x,y,z,f,g,h)
    h /= 2
    s2 = Calc(xmin,xmax,x,y,z,f,g,h)
    h /= 2
    print(str(contador) + '\t  ' + str(s) + '\t  ' + str(s1) + '\t  ' + str(s2) + '\t  ' + str(round(QC(s[0],s1[0],s2[0]),5)) + '\t' + str(round(QC(s[1],s1[1],s2[1]),5)))
    if (Calc(xmin,xmax,x,y,z,f,g,h) == Euler_sistemas(xmin,xmax,x,y,z,f,g,h)):
        value = 2
    elif (Calc(xmin,xmax,x,y,z,f,g,h) == RK2_sistemas(xmin,xmax,x,y,z,f,g,h)):
        value = 4
    elif (Calc(xmin,xmax,x,y,z,f,g,h) == RK4_sistemas(xmin,xmax,x,y,z,f,g,h)):
        value = 16
    while (abs(QC(s[0],s1[0],s2[0]) - value) > erro or abs(QC(s[1],s1[1],s2[1]) - value) > erro):
        contador += 1
        s = s1
        s1 = s2
        s2 = Calc(xmin,xmax,x,y,z,f,g,h)
        h /= 2
        print(str(contador) + '\t  ' + str(s) + '\t  ' + str(s1) + '\t  ' + str(s2) + '\t  ' + str(round(QC(s[0],s1[0],s2[0]),5)) + '\t' + str(round(QC(s[1],s1[1],s2[1]),5)))


# RESOLUÇÃO DE EQUAÇÕES DE SEGUNDO GRAU

def Euler_2(xmin,xmax,x,y,z,f,g,h):
    for i in range(0, round((xmax - xmin)/h)):
        y1 = y + h*f(x,y,z)
        z += h*g(x,y,z)
        y = y1
        x += h
    return (y,z)

def RK2_2(xmin,xmax,x,y,z,f,g,h):
    for i in range(0, round((xmax - xmin)/h)):
        y1 = y + h * f(x + h/2, y + h/2 *  f(x,y,z), z + h/2 * g(x,y,z))
        z += h * g(x + h/2, y + h/2 *  f(x,y,z), z + h/2 * g(x,y,z))
        y = y1
        x += h
    return (y,z)

def RK4_2(xmin,xmax,x,y,z,f,g,h):
    for i in range(0, round((xmax - xmin)/h)):
        dy1 = h*f(x,y,z)
        dz1 = h*g(x,y,z)
        dy2 = h*f(x + h/2, y + dy1 / 2, z + dz1/2)
        dz2 = h*g(x + h/2, y + dy1 / 2, z + dz1/2)
        dy3 = h*f(x + h/2, y + dy2 / 2, z + dz2/2)
        dz3 = h*g(x + h/2, y + dy2 / 2, z + dz2/2)
        dy4 = h*f(x + h, y + dy3, z + dz3/2)
        dz4 = h*g(x + h, y + dy3, z + dz3/2)
        y += 1/6*dy1 + 1/3*dy2 + 1/3*dy3 + 1/6*dy4
        z += 1/6*dz1 + 1/3*dz2 + 1/3*dz3 + 1/6*dz4
        x += h
    return (y,z)

def diferential_2(xi,xf,x,y,z,f,g,h,Calc):
    """Cálculo de sistemas diferenciais de 1ª ordem, 3 iterações
    xmin, xmax: x menor e x maior
    x,y,z: X0, Y0 e Z0
    f,g: funções para diferenciar
    h: distância entre dois pontos
    Calc: método para utilizar
    """
    s = Calc(xi,xf,x,y,z,f1,f2,h)
    h /= 2
    s1 = Calc(xi,xf,x,y,z,f1,f2,h)
    h /= 2
    s2 = Calc(xi,xf,x,y,z,f1,f2,h)
    print((round(s[0],5),round(s[1],5)), (round(s1[0],5),round(s1[1],5)), (round(s2[0],5),round(s2[1],5)), round(QC(s[0],s1[0],s2[0]),5), round(QC(s[1],s1[1],s2[1]),5), round(s1[0] - s2[0],5), round(s1[1] - s2[1],5))

