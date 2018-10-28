def all_rotation(n):
    lst = list(str(n))
    r = []
    for i in xrange(len(lst)):
        num = int(''.join(lst[1:]+[lst[0]]))
        r.append(num)
        lst = lst[1:]+[lst[0]]
    return r        



print all_rotation(1234)


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


primes = sieve(1000000)
xs = ['0', '2', '4', '5', '6', '8']

managable_primes = [x for x in primes if set(list(str(x))) & set(xs) == set([])] + [2, 5]
managable_primes.sort()

bad = []

for item1 in managable_primes:
    lst_perm = all_rotation(item1)
    for item in lst_perm:
        if item not in primes:
            bad.append(item1)


print len([x for x in managable_primes if x not in bad])
print [x for x in managable_primes if x not in bad]


