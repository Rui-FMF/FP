def countdown(n):
	if n > 0:
		print(n)
		countdown(n-1)

n = int(input("Insira n "))
countdown(n)
