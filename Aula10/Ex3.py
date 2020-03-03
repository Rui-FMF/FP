d= {}
with open("names.txt", "r") as fich:
    fich.readline()
    for line in fich:
        line = line.split()
        fname = line[0]
        lname = line[-1]
        if lname not in d:
            d[lname] = set()
        d[lname].add(fname)

for x, y in d.items():
    print(x,":",y)
            
        
        
