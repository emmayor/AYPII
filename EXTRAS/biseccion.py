def f(x):
    return x**2-4
    print(x)

def biseccion (a, b, epsilon=1e-5):
    """Calcula una raíz de f(x) en el intervalo a, b"""
    c = (a + b) /2
    i = 0
    while f(c) !=0 and abs(b - a) > epsilon:
        #print(i, c, f(c))
        i += 1
        if f(a) * f(c) > 0:
            a = c
        elif f(b)* f(c)>0:
            b = c
        c = (a + b) / 2
    return c, i
    
    
raiz = biseccion(0,100)
print(raiz)
