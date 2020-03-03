def printTable(lst):
	print("{:<10}{:>4}{:>8}{:>6}".format("Nome", "Peso", "Altura", "IMC"))
	for x in range(len(lst)):
		inf = lst[x]
		print("{:<10s}{:>4.0f}{:>8.2f}{:>6.1f}".format(inf[0], inf[1], inf[2], (inf[1])/(inf[2]**2)))

def inputBetween(txt, b, t):
	lim = float(input(txt))
	while (lim<b or lim>t):
		print("value must be in [",b,"",t,"]!")
		lim = float(input(txt))
	return lim

def selectTaller(lst, lim):
	tlist=[]
	for x in range(len(lst)):
		inf = lst[x]
		if inf[2]>lim:
			tlist.append(inf)
	return tlist
			
			
		
def main():
	# Lista de pessoas com nome, peso em kg, altura em metro.
	people = [("John", 64.5, 1.757),("Berta", 64.0, 1.612),("Maria", 45.1, 1.715),("Andy", 98.3, 1.81),("Lisa", 46.8, 1.622),("Kelly", 83.2, 1.78)]

    # Imprime os dados numa tabela com 4 colunas: nome, peso, altura e IMC.
	printTable(people)
    
    # Pede e devolve um valor, mas só aceita se estiver no intervalo certo.
	limit = inputBetween("altura minima? ", 1.1, 2.5)

    # Extrai uma lista de pessoas com altura superior a limit.
	tallpeople = selectTaller(people, limit)
    
	printTable(tallpeople)


# O programa começa aqui
main()

