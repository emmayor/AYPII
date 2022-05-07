def suma2(f):
    def fun(x): # DEFINE FUN, PERO NO LO LLAMA
        return f(x+2) # LLAMA A FOO
    return fun # SE DEVUELVE A SI MISMO 

def foo(x):
    print("x es " + str(x))

foo = suma2(foo) 

#AHORA FOO ES IGUAL A FUN(FOO)

foo(4)