
def load(fname):
    with open(fname) as f:
        lst = []
        for line in f:
            word = line.strip()
            lst.append(word)
    return lst


def filterPattern(lst, pattern):
	lstf= []
	for x in lst:
		if matchesPattern(x, pattern):
			lstf.append(x)
	return lstf
	


def matchesPattern(s, pattern):
	if len(s) != len(pattern):
		return False
	for x in range(len(s)):
		if pattern[x] != "?":
			if pattern[x].lower() != s[x].lower():
				return False
	return True


# Tests:
assert matchesPattern("secret", "s?c??t") == True
assert matchesPattern("socket", "s?c??t") == True
assert matchesPattern("soccer", "s?c??t") == False
assert matchesPattern("secret", "?ECR?T") == True  # "should be case-insensitive"

englishWords = load("/usr/share/dict/words")

lst = filterPattern(englishWords, "s?c??t")
print(lst)

#assert isinstance(lst, list),  "result lst should be a list"
#assert "secret" in lst,  "result should contain 'secret'"

# Solution to "?YS???Y"
lst = filterPattern(englishWords, "?ys???y")
print(lst)

