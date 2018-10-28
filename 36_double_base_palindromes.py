def is_palindrome_in_both(n):
	st = str(n)
	rev = st[::-1]
	binst = bin(n)[2:] 
	return st == rev and binst == binst[::-1]
	
	
S = 0
for i in xrange(1000000):
	if is_palindrome_in_both(i):
		S += i

print S		