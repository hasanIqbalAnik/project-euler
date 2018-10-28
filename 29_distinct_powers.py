#brute force
st = set()
for i in xrange(2, 101, 1):
	for j in xrange(2, 101, 1):
		st.add(i**j)

		
print len(st)