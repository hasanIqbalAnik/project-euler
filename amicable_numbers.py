import math

fact_dic = {}

def factors(n):
	if n in fact_dic:
		return fact_dic[n]
	else:
		lst_factors = []
		for i in xrange(1, n , 1):
			if(n%i == 0):
				lst_factors.append(i)
		fact_dic[n] = lst_factors				
	return fact_dic[n]


def is_amicable(m, n):
	if(sum(factors(m)) == n and sum(factors(n)) == m):
		return True
	else:
		return False		

Sum = 0
for i in xrange(10000):
	if sum(factors(i)) > i:
		for j in xrange(i, 10000, 1):
			if(is_amicable(i,j)):
				print i, j
				Sum += i + j


print Sum