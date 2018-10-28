from num2words import num2words

Sum = 0
for i in xrange(1, 1001, 1):
	Sum += len(num2words(i).replace(' ','').replace('-',''))

print Sum	