data = open('13-data', 'r')
stringNumbers = []
for line in data:
	stringNumbers.append(line)

result = range(0, 50)
carry = 0

def getDigit(stringNumbers, digit):
	global carry
	sum = carry % 10
	carry = carry / 10
	for stringNumber in stringNumbers:
		sum = int(stringNumber[digit]) + sum
		if sum >= 10:
			carry += 1
			sum %= 10
	return sum


for i in range(0, 50)[::-1]:
	result[i] = getDigit(stringNumbers, i)

str(carry)

print carry
print result
