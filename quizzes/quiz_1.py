# Cual es el resultado de este codigo?

def fun1(x = 0):
    x = x + 2
    y = fun2(x)
    return y

def fun2(x):
	a = x ** 2
	return a

resultado = fun1(5)

print (resultado)