def isPalindrome(number):
	wordNumber = str(number)
	return wordNumber == wordNumber[::-1]

i = 999
maxPalindrome = 0
while i >= 1:
	j = i
	while j >= 1:
		candidate = i * j
		if isPalindrome(candidate) and candidate > maxPalindrome:
			maxPalindrome = candidate
		j = j - 1
	i = i - 1
print str(maxPalindrome)