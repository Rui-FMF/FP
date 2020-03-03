
def setup() :
	fich = open("school.csv")
	lista = []
	fich.readline()
	while True:
		line = fich.readline()
		if line == "": break
		linha = line.strip().split("\t")
		del linha[2:5]
		linha[0] = int(linha[0])
		linha[2] = float(linha[2])
		linha[3] = float(linha[3])
		linha[4] = float(linha[4])
		linha = tuple(linha)
		lista.append(linha)
	fich.close()
	return lista

def notaFinal(x):
	return round((x[2]+x[3]+x[4])/3, 2)


with open("coiso", "w", encoding="utf-8") as cenas:
	lista = setup()
	cenas.write("{:} {:^50} {:>}".format("Numero", "Nome", "Nota\n"))
	for x in lista:
		cenas.write("{:} {:^50} {:>}".format(x[0], x[1], notaFinal(x))+"\n")
	

