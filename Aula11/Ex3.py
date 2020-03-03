def getMediana(lst):
	slst = sorted(lst)
	print(slst)
	if len(slst)%2==0:
		n = int(len(slst)/2)
		med = (slst[n] + slst[n-1])/2 
	else:
		n = int(len(slst)/2)
		med = slst[n]
	return med
		
		
print(getMediana([10, 7, 8, 3, 5]))
print(getMediana([3, 26, 6, 25, 10, 1]))
