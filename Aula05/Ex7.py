import math
def isprime(n):
	if n == 1:
		return "Unidade"
	else:
		for x in range(2, n):
			if n%x == 0:
				return False
		return True
			
for x in range(1,101):
	print(x, isprime(x))
