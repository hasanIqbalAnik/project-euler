from sympy.ntheory import factorint

largeDic = {}

for i in xrange(2, 20, 1):
	for k in factorint(i).keys():
		if(k in largeDic):
			if(largeDic[k] <= factorint(i)[k]):
				largeDic[k] = factorint(i)[k]
		else:
			largeDic[k] = factorint(i)[k]			

product = 1
for k in largeDic.keys():
	product = product * pow(k, largeDic[k])

print product	
