#coding=utf-8
ano = int(input("Insira o ano "))
mes = int(input("Insira o mês "))
if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
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
