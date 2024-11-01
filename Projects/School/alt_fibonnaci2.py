# this code uses a temporary variable in order to avoid using two deferrals that wait on each other 
# eg fib(n-1) + fib(n-2)

def fib2( n ):

	def helper ( m, mth, prev ):
		if m == n:
			return mth
		else:
			return helper(m + 1, m + prev, mth)
		

	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return helper( 1, 1, 0)
		
print  (fib2(7))
