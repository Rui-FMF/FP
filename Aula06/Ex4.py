def allMatches(lst):
	jogos = []
	for x in lst:
		for y in lst:
			if y != x:
				jogos.append((x,y))
	return jogos

def listar(lst):
	item = input("Insira um clube ")
	while item != "":
		lst.append(item)
		item = input("Insira um clube ")
	return lst

clubes = []
listar(clubes)
print(allMatches(clubes))
