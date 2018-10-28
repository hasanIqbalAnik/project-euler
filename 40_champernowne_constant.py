large_list = [str(i) for i in xrange(1, 1000001)]
s = ''.join(large_list)

print s[0], s[9], s[99], s[999], s[9999], s[99999], s[999999]
#print int(s[0])*int(s[9])*int(s[99])*int(s[999])*int(s[9999])*int(s[99999])* int(s[999999])
