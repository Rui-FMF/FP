
# Define the function containsDoubles here,
# so that it passes all the tests below.
def containsDoubles(word):
	for x in range(len(word)-1):
		if word[x]==word[x+1]:
			return True
	return False


# Test function
assert containsDoubles("pool") == True
assert containsDoubles("polo") == False
assert containsDoubles("erro") == True
assert containsDoubles("coooiso") == True
assert containsDoubles("banana") == False
# Add a few more tests below
...

# If the program reaches this point...
print("All tests passed!")


# This function should read lines from the given file
# and return a list of lines that contain doubles (consecutive repeated chars).
def findLinesWithDoubles(fname):
	# You may need to open the file with the encoding="latin1" argument
	lst=[]
	with open(fname, "r", encoding="utf-8") as f:
		for line in f:
			if containsDoubles(line):
				lst.append(line.strip())
	return lst
		

# This should show a list of all English words with double letters.
lst = findLinesWithDoubles("/usr/share/dict/words")
print(lst)

# Same thing for Portuguese words (if file available)
#lst = findLinesWithDoubles("/usr/share/dict/portuguese")
#print(lst)

