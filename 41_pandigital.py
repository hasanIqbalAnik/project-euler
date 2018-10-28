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


primes = sieve(9999999)

four_dig = ['1', '2', '3', '4']
five_dig = ['1', '2', '3', '4', '5']
six_dig = ['1', '2', '3', '4', '5', '6']
seven_dig = ['1', '2', '3', '4', '5', '6', '7']



for item in reversed(primes):
    if sorted(list(str(item))) == seven_dig:
        print item
        break
    elif sorted(list(str(item))) == four_dig:        
        print item
