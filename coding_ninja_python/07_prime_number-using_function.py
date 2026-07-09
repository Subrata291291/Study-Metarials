#Calculate Prime Number using Function
def calculate_prime_number(num):
	for i in range(2 , num):
		if num % i == 0:
			return False
	return True

result = calculate_prime_number(int(input("Enter Your number")))

if result == True:
	print("This is a Prime Number")
else:
	print("This is not a Prime Number")