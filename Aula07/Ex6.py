def compareFiles(file1, file2):
	pos = 1024
	with open(file1, "rb") as f1:
		with open(file2, "rb") as f2:
			for x in range(len(f1.read())):
				if not(f1.read(pos) == f2.read(pos)):
					print("diferentes")
					break;
				else:
					pos += 1024
			print("iguais")



compareFiles("coiso1.txt", "coiso2.txt")
			
			
