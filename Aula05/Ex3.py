def factorial(n):
	y = 1
	fac = 1
	while y <=n:
		fac = fac*y
		y = y + 1
	return fac
n = int(input("Insira um número "))
print(factorial(n))
