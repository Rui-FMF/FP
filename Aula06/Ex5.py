def countdigits(word):
	word = str(word)
	conta = 0
	for x in word:
		if x.isdigit():
			conta += 1
	return conta

stuff = "fwbwyeu6329fwebu1 23 jf"
print(countdigits(stuff))
		
