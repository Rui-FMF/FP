def listar(lst):
	item = input("Insira um numero da lista ")
	while item != "":
		lst.append(int(item))
		item = input("Insira um numero da lista ")
	return lst

def countlower(lst, v):
	conta = 0
	for x in lst:
		if x < v:
			conta += 1
	return conta

def minmax(lst):
	maxi = lst [0]
	mini = lst [0]
	for x in lst:
		if x > maxi:
			maxi = x
		if x < mini:
			mini = x
	return maxi, mini

lista = []
listar(lista)
media = ((minmax(lista)[0]) + (minmax(lista)[1]))/2
print("Existem",countlower(lista, media),"valores menores que a média entre o max e o min(",media,")")
