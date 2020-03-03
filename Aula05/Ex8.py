def divisor(n):
	total = 0
	for x in range (1, n):
		if n%x == 0:
			print(x)
			total += x
	if total < n:
			return "Deficiente"
	elif total == n:
		return "Perfeito"
	else:
		return "Abundante"
		

n = int(input("Insira um numero "))
print(divisor(n))
