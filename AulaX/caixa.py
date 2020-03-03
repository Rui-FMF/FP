MENU = """
(I)nserir Item
(F)acturar
(S)air
"""

def getData():
	dic = {}
	with open("hipermercado.txt", "r") as fich:
		for line in fich:
			item = line.strip().split(";")
			dic[item[0]] = [item[1], item[2], item[3], item[4], 0]
	print(dic)
	return dic

	
def getItems(dados):
	ndic = dados
	while True:
		cod = input("Insira o codigo do produto ")
		if cod in ndic:
			print("-->", ndic[cod][0],"preço:",ndic[cod][2])
			ndic[cod][4] += 1
		elif cod == "0":
			break
		else:
			print("codigo inválido")
	return ndic
			
			
def main():
	dados = getData()
	ndados = {}
	total = 0.0
	while True:
		op = input(MENU)
		
		if op == "I":
			ndados = getItems(dados)
			print(ndados)
		elif op == "F":
			print("cenas")
		elif op == "S":
			print("Programa Terminado")
			break
		else:
			print("opção inválida")
			
main()
		
			
