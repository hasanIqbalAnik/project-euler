# target number: 28433 * 2 ^ 7830457 + 1

mul = 1
exp = 7830457
m = 10000000000
for i in xrange(exp // 500):
	mul = ((mul%m) * ((2**500) % m))%m

mul =  28433 * mul * (2**(exp - (exp//500)*500))%m
print (mul + 1)%m