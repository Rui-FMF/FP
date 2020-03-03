def leibnizPi4(n):
	total = 0
	for x in range(0, n+1):
		total = total + (((-1)**x)/(2*x + 1))
	return total

n = int(input("Insira n "))
print("A soma dos",n,"primeiros termos da sequência de Leibniz é:",leibnizPi4(n))
