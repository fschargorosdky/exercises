def triangleNumber(n):
	return n * (n + 1) / 2

def divisorsCount(n):
	count = 0
	for i in range(1, (n+1)/2):
		if n % i == 0:
			count += 1
	return count

n = 5
while divisorsCount(triangleNumber(n)) <= 500:
	n += 1

print n
