fact_dic = {}
abundant_dic = []
others = []


def detect_type(n):
	s = sum(factors(n))
	if s == n:
		return 0
	elif s < n:
		return -1
	else:
		return 1			



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


# for i in xrange(28123):
# 	if(detect_type(i) == 1):
# 		abundant_dic.append(i)

# f = open('abun.txt', 'w+')
# for item in abundant_dic:
# 	f.write(str(item) + " ")

# f.close()	


l = []
with open('abun.txt', 'r') as f:
	l = [int(x) for x in f.readlines()[0].split(" ")]

		


		

def can_be(l, number):
	for i1 in (x for x in l if x <= number):
		for i2 in (y for y in l if y <= number):
			if i1 + i2 > number:
				break
			elif(i1 + i2 == number):
				print number
				return True
	return False				



Sum = 0
can_be_lst = []
others = [x for x in xrange(28123)]
for item in others:
	if(can_be(l, item)):
		can_be_lst.append(item)


cant_be = [x for x in others if x not in can_be_lst]

print sum(cant_be)