def get_multiples():
	term=3
	multiples=set()
	multiples.add(term)
	while term<1000:
		term+=3
		if term<1000:
			multiples.add(term)
	term=5
	multiples.add(term)
	while term<1000:
		term+=5
		if term<1000:
			multiples.add(term)
	
	print multiples
	print "Sum of all multiples of 3 or 5 is", sum(multiples)

if __name__=='__main__':
	get_multiples()
