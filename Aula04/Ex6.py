def tax(r):
	if r <= 1000:
		y = 0.1*r
		return y
	elif r<=2000:
		y = 0.2*r - 100
		return y
	else:
		y = 0.3*r - 300
		return y
r = float(input("Insira o valor de r "))
print(tax(r))
