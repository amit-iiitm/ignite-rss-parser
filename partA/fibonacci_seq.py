def main():
	prev=0
	curr=1
	fib_sum=0
	while True:
		prev,curr=curr,prev+curr
		if curr>=4000000:
			break
		if curr%2==0:
			fib_sum=fib_sum+curr
	print "The sum of even fibonacci numbers upto 4 million is", fib_sum

if __name__=='__main__':
	main()
