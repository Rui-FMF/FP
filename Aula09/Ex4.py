import random
def gameSetup():
	clubes = []
	jogos = []
	tabela = dict()
	nequipas = int(input("Quantas equipas quer no campeonato? "))
	for x in range(1, (nequipas+1)):
		print(x,"ª equipa?")
		y = input()
		clubes.append(y)
		tabela[y] = (0, 0, 0, 0, 0, 0)
	for x in clubes:
		for y in clubes:
			if y != x:
				jogos.append((x,y))
	return jogos, tabela

def campeao(dic):
	pnts = -1
	camp = ""
	for x, y in dic.items():
		if y[5] > pnts:
			camp = x
			pnts = y[5]
	return camp

def main(jogos, tabela):
	resultado = dict()
	for x in jogos:
		eq1 = x[0]
		eq2 = x[1]
		rec1 = list(tabela[eq1])
		rec2 = list(tabela[eq2])
		g1 = random.randrange(0, 4)
		g2 = random.randrange(0, 3)
		resultado[x] = (g1, g2)
		if g1 > g2:
			rec1[0] += 1
			rec1[3] += g1
			rec1[4] += g2
			rec1[5] += 3
			rec2[2] += 1
			rec2[3] += g2
			rec2[4] += g1
			rec2[5] += 0
		elif g1 < g2:
			rec2[0] += 1
			rec2[3] += g2
			rec2[4] += g1
			rec2[5] += 3
			rec1[2] += 1
			rec1[3] += g1
			rec1[4] += g2
			rec1[5] += 0
		else:
			rec1[1] += 1
			rec2[1] += 1
			rec1[3] += g1
			rec1[4] += g2
			rec2[3] += g2
			rec2[4] += g1
			rec1[5] += 1
			rec2[5] += 1
			
		tabela[eq1] = tuple(rec1)
		tabela[eq2] = tuple(rec2)
	for x, y in resultado.items():
		print(x[0],"-",x[1],":",y[0],"-",y[1])
	print("------------------------------------------------------------")
	print("{:<7} {:<7} {:<7} {:<7} {:<7} {:<7} {:<7}".format("EQUIPA","V", "E", "D", "GM", "GS", "P"))
	for k, z in tabela.items():
		print("{:<7} {:<7} {:<7} {:<7} {:<7} {:<7} {:<7}".format(k, z[0], z[1], z[2], z[3], z[4], z[5]))
	print("------------------------------------------------------------")
	print("O CAMPEÃO DESTE CAMPEONATO É:",campeao(tabela))
	
		
		
			
jogos, tabela = gameSetup()
main(jogos, tabela)


