import bisect
def load(fname):
    with open(fname) as f:
        lst = []
        for line in f:
            word = line.strip()
            lst.append(word)
    return lst
    
words = load("/usr/share/dict/words")

prefixo = ""
carac = input("insira um caracter ")
while (carac != ""):
	prox = prefixo+(chr(ord(carac)+1))
	prefixo += carac
	pos1 = bisect.bisect_left(words, prefixo, 0, len(words))
	pos2 = bisect.bisect_left(words, prox, 0, len(words))
	lwords = words[pos1:pos2]
	if lwords==[]:
		print("Não existem palavras com esse prefixo, recomece o programa ")
		break
	if len(lwords)==1:
		print("Palavra encontrada:",lwords[0])
		break
	print(lwords)
	print("Prefixo atual:",prefixo)
	carac = input("Insira um novo caracter ")
	
print("Fim de programa")
	
