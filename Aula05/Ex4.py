lista = [0,1]
def fibonacci(n):
	for x in range(2,n+1):
		lista.append(lista[x-1] + lista[x-2])
	return lista[n]

n = int(input("Insira um numero "))
print("O",n,"numero de fibonacci é:",fibonacci(n))

	
