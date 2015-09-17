res = 0
f1 = 1
f2 = 2
even = 0
while f2 <= 4000000:
	if even == 0:
		res = res + f2
	even = even + 1
	if even == 3:
		even = 0	
	aux = f2
	f2 = f1 + f2
	f1 = aux

print res