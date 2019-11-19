'''
Considere a função F(x) 5*x**2+6*x-2

Determine,recorrendo aos 2 métodos intervalares, o nº de iterações necessárias
para calcular o zero em [-2,-1], utilizando diferentes critérios de precisão = 10**(-4)

Met Bisseção:  |a-b| = 15    |(a-b)/a| = 14    |Xn+1 - Xn| = 14     |(Xn+1-Xn)/Xn+1| = 13
Met Corda:     |a-b| = 26    |(a-b)/a| = 26    |Xn+1 - Xn| = 7     |(Xn+1-Xn)/Xn+1| = 7
'''

def f(x):
    return 5*x**2+6*x-2


def bissecao(a,b,erro):
    temp = 0
    x = (a+b)/2
    contador = 1
    print(str(contador) + '\t' + str(x))
    while (abs(a-b) > erro):
        if (f(a) * f(x) > 0):
            temp = x
            a = x
            x = (a+b)/2
            contador += 1
        elif (f(a) * f(x) < 0):
            temp = x
            b = x
            x = (a+b)/2
            contador += 1
        print(str(contador) + '\t' + str(x))

    print ("Zero: " + str(x) + "\t Iterções: " + str(contador) + '\n')


def corda(a,b,erro):
    temp = 0
    x = (a*f(b) - b*f(a))/(f(b) - f(a))
    contador = 1
    print(str(contador) + '\t' + str(x))
    while (abs(x-temp) > erro):
        if (f(a) * f(x) < 0):
            temp = x
            b = x
            x = (a*f(b) - b*f(a))/(f(b) - f(a))
            contador += 1
        else:
            temp = x
            a = x
            x = (a*f(b) - b*f(a))/(f(b) - f(a))
            contador += 1
        print(str(contador) + '\t' + str(x))
    print ("Zero: " + str(x) + "\t Iterções: " + str(contador) + '\n')


a = -2
b = -1
erro = 10**(-4)
#bissecao(a,b,erro)
corda(a,b,erro)



'''
f(x) = x**2 - x - 12
Aplique os métodos a)Picardi-Peano e b)Newton para calcular 1 zero da função pretendida
Preencha a tabela com 3 casas decimais

a) x        g(x)   nº iteração
   *4.0	    2.280	  1
   2.280	1.865     2
   1.865	1.750	  3
   1.750	1.717	  4
   1.717	1.708     5
   1.708	1.705	  6
   1.705	1.704	  7
   1.705	1.704  	  8
   1.704	1.704  	  9

   0.0002

b)
   x     g(x)       g'(x)  nº iteração
2.457	2.380	    3.914	  1
1.849	0.369	    2.698	  2
1.711	0.018       2.423	  3
1.704	6.008e-05	2.408	  4
1.704	6.224e-10	2.408	  5

c)Considerando a solução 1.70416 calcule o erro absoluto e relativo da ultima iteração
absoluto = 0.00016  relativo = 0,000093888
'''

def g(x):
    return x**2-x-1.2

def g1(x):
    return (x+1.2)**(1/2)

def g2(x):
    return 2*x-1


def Picard(x):
    temp = x
    x = g1(x)
    contador = 1
    print(str(temp) + '\t' + str(x) + '\t' + str(contador))
    while (abs(x-temp) > 10**(-4)):
        temp = x
        x = g1(x)
        contador += 1
        print(str(temp) + '\t' + str(x) + '\t' + str(contador))

    print ("Zero: " + str(x) + "\t Iterções: " + str(contador) + '\n')


def Newton(x):
    temp = x
    x = x-(g(x)/g2(x))
    contador = 1
    print(str(x) +'\t' + str(g(x)) + '\t'+ str (g2(x))+ '\t' + str(contador))
    while(abs(x-temp) > 10**(-4)):
        temp = x
        x = x-(g(x)/g2(x))
        contador += 1
        print(str(x) +'\t' + str(g(x)) + '\t'+ str (g2(x))+ '\t' + str(contador))

    print ("Zero: " + str(x) + "\t Iterções: " + str(contador) + '\n')

x = 4.0
#Picard(x)
#Newton(x)


'''
x**2 + x*y - 10 = 0
y + 3*x*y**2 - 57 = 0

Resolva o sistema com x0 = 0.5 e y0 = 3.0
Precisão absoluta = 10**(-4)
a) Newton           4	(2.000000544009009, 2.9999999999999107)
b) Picard-peano     11	(2.000022721969491, 2.999981451354)

'''

def hx(x,y):
    return (10-x*y)**(1/2)

def hy(x,y):
    return ((57-y)/(3*x))**(1/2)

def h(x,y):
    return x**2 + x*y - 10

def i(x,y):
    return y + 3*x*y**2 - 57

def h1x(x,y):
    return y+2*x

def h1y(x,y):
    return x

def i1x(x,y):
    return 3*y**2

def i1y(x,y):
    return 6*x*y + 1


def Newton_sistemas(x,y,erro):
    xtmp = x
    ytmp = y
    x = x - (h(x,y)*i1y(x,y) - i(x,y)*h1y(x,y))/(h1x(x,y)*i1y(x,y) - h1y(x,y)*i1x(x,y))
    y = y - (i(xtmp,ytmp)*h1x(xtmp,ytmp) - h(xtmp,ytmp)*i1x(xtmp,ytmp))/(h1x(xtmp,ytmp)*i1y(xtmp,ytmp) - h1y(xtmp,ytmp)*i1x(xtmp,ytmp))
    contador = 1
    print(str(contador) + '\t' + str((x,y)))
    while(abs(x-xtmp) > erro or abs(y - ytmp) > erro):
        xtmp = x
        ytmp = y
        x = x - (h(x,y)*i1y(x,y) - i(x,y)*h1y(x,y))/(h1x(x,y)*i1y(x,y) - h1y(x,y)*i1x(x,y))
        y = y - (i(xtmp,ytmp)*h1x(xtmp,ytmp) - h(xtmp,ytmp)*i1x(xtmp,ytmp))/(h1x(xtmp,ytmp)*i1y(xtmp,ytmp) - h1y(xtmp,ytmp)*i1x(xtmp,ytmp))
        contador += 1
        print(str(contador) + '\t' + str((x,y)))
    print("Zero: " + str((x,y)))


def Picard_sistemas(x,y,erro):
    xtmp = x
    ytmp = y
    x = hx(x,y)
    y = hy(xtmp,y)
    contador = 1
    print(str(contador) + '\t' + str((x,y)))
    while(abs(x-xtmp) > erro or abs(y-ytmp) > erro):
        xtmp = x
        ytmp = y
        x = hx(x,y)
        y = hy(xtmp,ytmp)
        contador += 1
        print(str(contador) + '\t' + str((x,y)))
    print("Zero: " + str((x,y)))

x = 3
y = 3
erro = 10**(-4)
#Picard_sistemas(x,y,erro)
#Newton_sistemas(x,y,erro)
