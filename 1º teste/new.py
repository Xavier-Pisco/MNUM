import math


def f(x):
    return (x-3.6)+(math.cos(x+1.2))**3

def f1(x):
    return 1 - 3*(math.cos(x+1.2))**2*math.sin(x+1.2)

def Newton(x):
    return x - f(x)/f1(x)
    temp = x + 10
    while(abs(x-temp) > 10**(-6)):
        temp = x
        x = x - f(x)/f1(x)
        print(str(x))

print(Newton(0.5))
