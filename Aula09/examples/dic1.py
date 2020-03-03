# Example: a simple translator

d = {"as": "the", "os": "the", "e": "and", "praia": "beach"}

# Try: as armas e os barões assinalados que da ocidental praia lusitana
s = input("Texto? ")
t = ""
for w in s.split():
    if w in d:
        w = d[w]
    t = t + " " + w

print(t)
