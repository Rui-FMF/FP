def max2(a,b):
	if a>b:
		return a
	elif b>a:
		return b
	else:
		return "iguais"
a, b = input("Insira dois numeros ").split()
a, b = float(a), float(b)
print(max2(a,b))
