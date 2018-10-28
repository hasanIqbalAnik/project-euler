
def collatz(n):
	counter = 1
	while(n!=1):
		if(n%2 == 0):
			n /= 2
			counter += 1
		else:
			n = 3*n + 1
			counter += 1
	return counter			

max_length = -99999
max_num = 0
for i in xrange(1000000, 1, -1):
	cl = collatz(i)
	if(cl > max_length):
		max_length = cl
		max_num = i

print max_num
print max_length		



