n = 600851475143
d = 2
counter = 0

while True:
	if(n % d == 0):
		n = n/d
	else:
		d += 1
	counter += 1		
	if(n == 1):
		break

print d
