def fact(num):
	if num < 0:
		print("Number is negative!! Factorial can't calculate...")
	else :
		f = 1;
		while num > 0:
			f *= num
			num -= 1
		print(f)
num = int(input("Enter the Number for it's Factorial : "))
fact(num)
