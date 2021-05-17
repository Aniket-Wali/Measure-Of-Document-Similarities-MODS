def sum_list(lst):
	sum = 0
	for i in lst:
		sum += i 
	return sum

def perfect_number(num):
	lst = []
	for i in range(1, num):
		if num % i == 0:
			lst.append(i)
	print("Factors are : ",lst)
	return sum_list(lst)

def main():
	num = int(input("Enter a Number : "))
	temp = perfect_number(num)

	if num == temp:
		print("perfect number\n\n")
	else:
		print("Not a perfect number\n\n")

if __name__ == "__main__":
	import profile
	profile.run("main()")