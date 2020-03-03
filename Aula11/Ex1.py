import sys

def cont(fich):
	d= dict()
	with open(fich, "r", encoding="utf-8") as f:
		for line in f:
			for c in line:
				c = c.lower()
				if c.isalpha():
					if c not in d:
						d[c] = 1
					else:
						d[c] += 1
	return d

if len(sys.argv) < 2:
	print("Sintaxe: python3 {} nome_do_ficheiro".format(sys.argv[0]))
	exit(1)

d = cont(sys.argv[1])
d = sorted(d.items(), key= lambda n: n[1], reverse=True)

for x in d:
	print(x)
