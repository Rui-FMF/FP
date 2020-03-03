# Complete the code to make the HiLo game...

import random

def main():
    # Pick a random number between 1 and 100, inclusive
	contagem = 0
	secret = random.randrange(1, 101);
	print("Can you guess my secret?")
	n = int(input("Insert a number "))
	while n != secret:
		contagem = contagem + 1
		if n < secret:
			print("LOW")
		if n > secret:
			print("HIGH")
		n = int(input("Try again "))
	print("Correct number, it only took you",contagem,"times")
    
main()

