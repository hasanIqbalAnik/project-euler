options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 1
try:	
	for i1 in options:
		for i2 in (x for x in options if x not in [i1]):
			for i3 in (x for x in options if x not in [i1, i2]):
				for i4 in (x for x in options if x not in [i1, i2, i3]):
					for i5 in (x for x in options if x not in [i1, i2, i3, i4]):
						for i6 in (x for x in options if x not in [i1, i2, i3, i4, i5]):
							for i7 in (x for x in options if x not in [i1, i2, i3, i4, i5, i6]):
								for i8 in (x for x in options if x not in [i1, i2, i3, i4, i5, i6, i7]):
									for i9 in (x for x in options if x not in [i1, i2, i3, i4, i5, i6, i7, i8]):
										for i10 in (x for x in options if x not in [i1, i2, i3, i4, i5, i6, i7, i8, i9]):
											if counter == 1000000:
												print i1, i2, i3, i4, i5, i6, i7, i8, i9, i10
												raise ValueError																
											else:
											 	counter += 1


except ValueError:
	print 'done'									