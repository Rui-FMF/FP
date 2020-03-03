def max2(a,b):
	if a>b:
		return a
	else:
		return b
def max3(a,b,c):
	d = max2(c,max2(a,b))
	return d

a,b,c = input("Insire 3 numeros ").split()
a,b,c = float(a), float(b), float(c)
print(max3(a,b,c))
