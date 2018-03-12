def square(g):
    return(g*g)
def doesSomething(f,x):
    return f(x)
print doesSomething(square,3)
print doesSomething(lambda x:x*x*x*x,3)
