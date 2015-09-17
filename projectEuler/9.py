def makeC(a, b):
	return 1000 - a - b

def isPythagoreanTriplet(a, b, c):
	return a ** 2 + b ** 2 == c ** 2

a = 1
b = 2
c = makeC(a, b)

while not(isPythagoreanTriplet(a, b, c) and a + b + c == 1000):
	b += 1
	c = makeC(a, b)
	if c <= b:
		a += 1
		b = a + 1
		c = makeC(a, b)

print a
print b
print c
print a * b * c
