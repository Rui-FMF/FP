#coding=utf-8
ano = int(input("Insira o ano "))
mes = int(input("Insira o mês "))
dia = int(input("Insira o dia "))
if mes==12:
	if dia==31:
		ano_s = ano+1
		mes_s = 1
		dia_s = 1
		dia_a = 30
		print("A data do dia seguinte é:")
		print(dia_s,mes_s,ano_s, sep="/")
		print("A data do dia anterior é:")
		print(dia_a,mes,ano, sep="/")
	elif dia==1:
		dia_s = 2
		dia_a = 30
		mes_a = 11
		print("A data do dia seguinte é:")
		print(dia_s,mes,ano, sep="/")
		print("A data do dia anterior é:")
		print(dia_a,mes_a,ano, sep="/")
elif mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10:
	print("O mês tem 31 dias")
elif mes==4 or mes==6 or mes==9 or mes==11:
	print("O mês tem 30 dias")
elif mes==2:
	if ano%4==0:
		if ano%100==0:
			if ano%400==0:
				print("O mês tem 29 dias")
			else:
				print("O mês tem 28 dias")
		else:
			print("O mês tem 29 dias")
	else:
		print("O mês tem 28 dias")
else:
	print("Não inseriu um mês válido")
