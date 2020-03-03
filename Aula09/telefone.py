# Complete este programa como pedido no guião da aula.

def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {:^24} : {:s}".format("Numero", "Nome", "Morada"))
    for x, y in dic.items():
        print("{:>12s} : {:^24} : {:s}".format(x, y[0], y[1]))

def filterPartName(dic):
	part = input("Insira parte de um nome ")
	ndic = dict()
	for x, y in dic.items():
		if part in y[0]:
			ndic[x] = y
	if ndic == {}:
		print("Não foram encontrados contactos que contenham:",part)
	else:
		for x, y in ndic.items():
			print(x,":",y[0],":",y[1])

def addContact(dic):
	num = input("Numero? ")
	while not(num.isdigit()) or (len(num)<9):
		print("Insira um numero válido")
		num = input("Numero? ")
	name = str(input("Nome? "))
	mor = str(input("Morada? "))
	if (num in dic):
		sel = input("Numero já existe, pretende atualizar os dados? (s/n) ")
		while sel!="n" and sel!="s":
			sel = input("Opção inválida, pretende atualizar os dados? (s/n) ")
		if sel == "s":
			dic[num] = (name, mor)
			print("Contacto atualizado" )
	else:
		dic[num] = (name, mor)
		print("Contacto adicionado")
		
def removeContact(dic):
	num = input("Numero a remover? ")
	while not(num.isdigit()) or (len(num)<9):
		print("Insira um numero válido") 
		num = input("Numero a remover? ")
	if not(num in dic):
		print("Não existe contacto com este numero ")
	else:
		sel = input("Tem a certeza que quer remover o contacto? (s/n) ")
		while sel!="n" and sel!="s":
			sel = input("Opção inválida, quer remover o contacto? (s/n) ")
		if sel == "s":
			del dic[num]
			print("Numero eliminado ")

def findContact(dic):
	num = input("Numero? ")
	while not(num.isdigit()) or (len(num)<9):
		print("Insira um numero válido") 
		num = input("Numero? ")
	f = dic.get(num)
	if f == None:
		print(num)
		print("Numero não consta na lista")
	else:
		print("O numero",num,"corresponde ao contacto:",f[0],":",f[1])
		
	

def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op


def main():
	"""This is the main function containing the main loop."""

	# The list of contacts (it's actually a dictionary!):
	contactos = {"234370200": ("Universidade de Aveiro", "Santiago, Aveiro"), "727392822": ("Cristiano Aveiro", "Madeira"), "387719992": ("Maria Matos", "Porto"), "887555987": ("Marta Maia", "Lisboa"), "876111333": ("Carlos Martins", "Algarve"), "433162999": ("Ana Bacalhau", "Alentejo")}
	op = ""
	while op != "T":
		op = menu()
		if op == "T":
			print("Fim")
		elif op == "L":
			print("Contactos:")
			listContacts(contactos)
		elif op == "A":
			addContact(contactos)
		elif op == "R":
			removeContact(contactos)
		elif op == "N":
			findContact(contactos)
		elif op == "P":
			filterPartName(contactos)	
		else:
			print("Não é uma opção")
    

# O programa começa aqui
main()

