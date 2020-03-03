def shorten(word):
	word = str(word)
	abrev = ""
	for x in word:
		if x.isupper():
			abrev += x
	return abrev


print(shorten("United Nations"))
print("x".isupper())
