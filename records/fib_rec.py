@profile
def nthfib(n):
	if n <= 0:
		return 0
	elif n == 1:
		return 1
	else:
		return nthfib(n-1) + nthfib(n-2)

for i in range(1,11):
	print(nthfib(i))

