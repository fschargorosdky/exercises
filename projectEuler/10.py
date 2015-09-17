import math

def isPrime(x):
	if x == 2:
		return True
	for i in range(2, int(math.ceil(math.sqrt(x))) + 1):
		if x % i == 0:
			return False
	return True

result = 0
top = 2 * 1000 * 1000
for i in range(2, top + 1):
	if isPrime(i):
		result += i

print result
