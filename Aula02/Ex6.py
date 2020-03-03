import math
a = float(input("Insira a medida do cateto adjacente "))
b = float(input("Insira a medida do cateto oposto "))
c = math.sqrt((a**2)+(b**2))
ang_r = math.acos(a/c)
ang_c = math.degrees(ang_r)
print("A hipotenusa do triângulo é: ",c," o angulo entre o cateto adjacente e a hipotenusa é: ",ang_c)

