import math

def f(x):
    return x-2*math.log(x) - 5

def erro_absoluto_bissecao(a,b,erro):
    x = (a+b)/2
    contador = 1
    temp = 0
    while(abs(temp - x) > erro):
        print(str(contador) + '\t x = ' + str(x))
        contador += 1
        if (f(a) * f(x) < 0):
            b = x

        else:
            a = x

        temp = x
        x = (a+b)/2

    print(str(contador) + '\t x = ' + str(x) + '\n')
    return x

def erro_absoluto_corda(a,b,erro):
    x= (f(a)*b - f(b)*a) / (f(a)-f(b))
    contador = 1
    temp = 0
    while (abs(temp - x) > erro):
        print(str(contador) + '\t x = ' + str(x))
        contador += 1
        if (f(a) * f(x) < 0):
            b = x

        else:
            a = x

        temp = x
        x= (f(a)*b - f(b)*a) / (f(a)-f(b))

    print(str(contador) + '\t x = ' + str(x) + '\n')
    return x


erro = 10**(-3)

erro_absoluto_bissecao(0.05,2,erro)
erro_absoluto_bissecao(8,10,erro)

erro_absoluto_corda(0.05,2,erro)
erro_absoluto_corda(8,10,erro)
