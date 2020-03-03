MENU = """
1) Registar Chamada
2) Ler Ficheiro
3) Listar clientes
4) Fatura
5) Terminar
Escolha uma opção """

def isphone(s):
	valid = (len(s)>=3 and s.isdigit()) or (len(s)>=4 and s[0]=="+" and s[1:].isdigit())
	return valid
	
def inputCall():
	
	
def main():
	chamadas = {}
	while True:
		op = input(MENU)
		
		if op == "1":
			chamada = inputCall()
			AddCall()
		elif op == "2":
			print("Não implementado")
		elif op == "3":
			print("Não implementado")
		elif op == "4":
			print("Não implementado")
		elif op == "5":
			print("PROGRAMA TERMINADO")
			break
		else:
			print("Opção inválida!")
			
	return
	
	
main()
