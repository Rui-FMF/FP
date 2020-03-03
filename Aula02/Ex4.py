total = int(input("Insira numero de segundos total "))
minutos = (total//60)%60
horas = (total//60)//60
segundos = (total%60)%60
print(horas,"h : ",minutos,"m : ",segundos,"s")
print(horas,minutos,segundos, sep=":")
