import math

def f(x):
	return x - 2*math.log(x)- 5

def f1(x):
	return 1 - 2/x

def V(h):
	return (math.pi * h**2 * (9-h)/3) - 30

def V1(h):
	return (2*math.pi*(9-h)*h - math.pi * h**2)/3


def tangente(x,erro, func, func1):
	temp = x + 10**10 * erro
	contador = 0
	while (abs(temp - x) > erro):
		temp = x
		x -= func(x)/func1(x)
		contador += 1
		print(str(contador) + '\t x = ' + str(x))
	print ("\nZero: " + str(x) + '\n')

def bissecao(a,b,erro, func):
    temp = 0
    x = (a+b)/2
    contador = 1
    while (abs(temp - x) > erro):
        print(str(contador) + '\t' + str(x))
        if (func(a)* func(x) > 0):
            a = x
            temp = x
            x = (a+b)/2
            contador += 1

        elif (func(a)*func(x) < 0):
            b = x
            temp = x
            x = (a+b)/2
            contador += 1

    print (str(contador) + '\t' + str(x) + '\n')
    print ("Zero: " + str(x) + '\n')


def corda(a,b,erro, func):
    temp = 0
    x = (a*func(b) - b*func(a))/(func(b)-func(a))
    contador = 1
    while (abs(temp - x) > erro):
        print(str(contador) + '\t' + str(x))
        if (func(a) * func(x) > 0):
            a = x
            temp = x
            x = (a*func(b) - b*func(a))/(func(b)-func(a))
            contador += 1
        
        elif (func(a) * func(x) < 0):
            b = x
            temp = x
            x = (a*func(b) - b*func(a))/(func(b)-func(a))
            contador += 1

    print(str(contador) + '\t' + str(x) + '\n')
    print ("Zero: " + str(x) + '\n')






x1 = 1.9
x2 = 2.5
erro = 10**(-5)

'''
tangente(x1,erro, f, f1)
print ();
tangente(x2,erro, f, f1)
'''


tangente(x1,erro,V,V1)
print()
corda(x1,x2,erro,V)
print()
bissecao(x1,x2,erro,V)


