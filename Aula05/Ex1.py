total = 0
contagem = 0
n = input("Insira um numero ")
if n != "":
	minimo = maximo = float(n)
while n != "":
	n = float(n)
	if n < minimo:
		minimo = n
	if n > maximo:
		maximo = n
	total = total + n
	contagem = contagem + 1
	n = input("Insira um numero ") 
media = total/contagem
print("O máximo é: ",maximo," O minimo é: ",minimo," A média é: ",media)
	
