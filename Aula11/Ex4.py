import bisect
def load(fname):
    with open(fname) as f:
        lst = []
        for line in f:
            word = line.strip()
            lst.append(word)
    return lst
    
words = load("/usr/share/dict/words")

n = bisect.bisect_left(words, "ea")
m = bisect.bisect_left(words, "eb")
z = bisect.bisect_left(words, "tp")
print(m-n,"words that start with 'ea'")
for x in range(n, m):
	print(words[x])
	
print(z)
print(words[z])
	

