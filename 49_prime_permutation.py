import collections

def sieve(n):
    "Return all primes <= n."
    np1 = n + 1
    s = list(range(np1)) # leave off `list()` in Python 2
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1): # use `xrange()` in Python 2
        if s[i]:
            # next line:  use `xrange()` in Python 2
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)

primes = sieve(9999)


four_lst_int = [int(''.join(list(str(x)))) for x in primes if len(list(str(x))) == 4]

str_list = [list(str(x)) for x in four_lst_int]
sorted_str_lst = sorted(str_list)

d = {}
for item in sorted_str_lst:
    k =int(''.join(sorted(item)))
    if k in d:
        if sorted(item) == sorted(list(str(k))):
            d[k].append(int(''.join(item)))
    else:
        d[k] = []            

od = collections.OrderedDict(sorted(d.items()))
odc = od


for item in od.items():
    if len(item[1]) < 3:
        del odc[item[0]]

for item in odc.items():
    lst = item[1]
    if(lst[1] - lst[0] == 3330 and lst[2] - lst[1] == 3330):
        print item