def f(a, b, c, x):
	y = a*(x**2)+b*x+c
	return y
a, b, c, x = input("Seja f(x)= ax^2 + bx + c insira os valores de a b c x nesta ordem ").split()
a,b,c,x = float(a),float(b),float(c),float(x)

print("f(x) =",f(a, b, c, x))
