import math

def count_digits(base, exp):
	return math.floor(exp * math.log10(base)) + 1


base = 1

ctr = 0
flag1 = True
flag2 = True
while flag1:
	exp = 1
	while flag2:		
		c = count_digits(base, exp) 
		if c == exp:
			ctr += 1
			exp += 1
		elif c < exp:
			base += 1
			break
		else:
			flag1 = False
			flag2 = False


print ctr