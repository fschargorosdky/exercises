def collatz(n):
	if n % 2 == 0:
		return n / 2
	else:
		return 3 * n + 1

def collatzLength(n):
	length = 0
	while collatz(n) != 1:
		n = collatz(n)
		length += 1
	return length

maxLength = 0
maxNumber = 0
limit = 1000000
for i in range(1, limit):
	length = collatzLength(i)
	print i
	if length > maxLength:
		maxLength = length
		maxNumber = i

print maxNumber
print maxLength
