def is_palindrome(n):
	return str(n) == str(n)[::-1]

largest = -9999
for i in xrange(999, 0, -1):
	for j in xrange(999, 0, -1):
		if(is_palindrome(i*j)):
			if(i*j >= largest):
				largest = i*j
			break
print largest			