def isPrime(number):
	i = 3
	while i < number:		
		if number % i == 0:
			return False
		i = i + 2
	return True


i = 3
primes = 2
while primes < 10001:
	i = i + 2
	if isPrime(i):
		primes = primes + 1
print str(i)