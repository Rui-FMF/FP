def mdc(a,b):
	r = a%b
	if r ==0:
		print(b)
	elif r > 0:
		mdc(b,r)
a,b = input("Insira 2 numeros naturais ").split()
a,b = int(a), int(b)
if a > 0 or b > 0:
	mdc(a,b)
else:
	print("Não inseriu 2 numeros naturais")
