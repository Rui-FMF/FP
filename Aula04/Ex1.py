def IMC(x, y):
	imc = x/(y**2)
	return imc
peso = float(input("Insira o peso em Kg "))
altura = float(input("Insira a altura em metros "))
print("O seu IMC é",IMC(peso,altura))

