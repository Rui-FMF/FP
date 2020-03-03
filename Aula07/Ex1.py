soma = 0
fich = open('nums.txt')

for line in fich:
	soma += float(line)
fich.close()

print(soma)
