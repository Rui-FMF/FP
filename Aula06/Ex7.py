def ispalindrome(s):
	n = len(s)
	for i in range(n):
		if s[i] != s[(n-1) - i]:
			return False
	return True

print(ispalindrome("baab"))
			


