api = float(input("Insira a sua nota API "))
atp = float(input("Insira a sua nota ATP "))
ep = float(input("Insira a sua nota EP "))
nota = 0.3*api + 0.3*atp +0.4*ep
if nota>=10:
	print("A sua nota é ",nota," você está aprovado")
else:
	print("A sua nota é ",nota," você está reprovado em epoca normal")
	etpr = float(input("Insira a sua nota ETPR "))
	epr = float(input("Insira a sua nota EPR "))
	nota_r = 0.3*etpr + 0.7*epr
	if nota_r>=10:
		print("Você está aprovado com a nota de {:.2f} valores".format(nota_r))
	else:
		print("Você está reprovado com a nota de {:.2f} valores".format(nota_r))
