def is_leap_year(year):
	if year % 100 == 0:
		if year % 400 == 0:
			return True
		else:
			return False
	elif year % 4 == 0:
		return True
	else:
		return False



days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_in_months_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# sundays_in_1900 = [True if  x % 7 == 0 else False for x in xrange(1, 365+1, 1)]
# print sundays_in_1900

long_list = [False for x in xrange(100*365 + 25)]
long_list_months = [False for x in xrange(100*365 + 25)]


for i in xrange(5, len(long_list), 7):
	long_list[i] = True

ctr = 0

for i in xrange(1901, 2001, 1):	
	if is_leap_year(i):
		for item in days_in_months_leap:
			long_list_months[ctr] = True
			ctr += item
	else:
		for item in days_in_months:
			long_list_months[ctr] = True
			ctr += item


#print sum(long_list and long_list_months)
print sum([a and b for a, b in zip(long_list, long_list_months)])
