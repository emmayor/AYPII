def f(x):
    return x**2-4
    print(x)

def regula_falsi(a, b, epsilon=1e-5):
    """Calcula una raíz de f(x) en el intervalo a, b"""
    c = b-(f(b)*(b-a))/(f(b)-f(a))
    i = 0
    while abs(f(c))>epsilon and abs(b - a) > epsilon:
        i += 1
        if f(a) * f(c) > 0:
            a = c
        elif f(b)* f(c)>0:
            b = c
        c = b-(f(b)*(b-a))/(f(b)-f(a))
    return c, i
    
    
raiz = regula_falsi(0,100)
print(raiz)
