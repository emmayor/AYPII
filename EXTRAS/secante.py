def f(x):
    return x**2-4
    print(x)

def secante(x1, x2, epsilon=1e-5, maxv=1000):
    xnew = x2 - f(x2)*(x2-x1)/(f(x2) - f(x1))
    i = 0
    while abs(f(xnew))>epsilon and abs(f(xnew)-f(x2)) > epsilon and i<=maxv:
        i += 1
        x1, x2 = x2, xnew
        xnew = x2 - f(x2)*(x2-x1)/(f(x2) - f(x1))
        #print(i, x1, x2, xnew)
    return xnew, i
        
    
    
raiz = secante(0,100)
print(raiz)
