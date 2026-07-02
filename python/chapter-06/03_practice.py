# number = int(input("Enter the number: "))

# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")


# price = int(input("Enter the price: "))
# discount = int(input("Enter the discount: "))


# # final_price = price - discount
# price -= discount
# print(f"The final price after discount is: {price}")


is_logged_in = True
is_address_verified = True
# print(is_logged_in and is_address_verified)
print("You can make a purchase") if is_logged_in and is_address_verified else print("You cannot make a purchase")

#Bitwise operators
print(5 & 3)  # Bitwise AND (if both value are same then it will return 1 otherwise 0)
print(5 | 3)  # Bitwise OR (if both value are same then it will return 1 otherwise 0)
print(5 ^ 3)  # Bitwise XOR (if both value are same then it will return 0 otherwise 1)

# Bitwise operators, the numbers are represented in binary format, and the operations are performed on each corresponding bit of the numbers.

num1 = 5
num2 = 6
num3 = 7

result = (num1 + num2 + num3) / 4 - 10 * 2 #it will be evaluated from left to right, so the result will be -11.75
print(result)
print((2 ** 3 + 4) / 2) #it will be evaluated from left to right, so the result will be 6.0
print(5 + 4 - 2 + 7 + 3) # it will be evaluated from left to right, so the result will be 17
print( 10 - 5 + 3 * 2) # it will be evaluated from right to left, so the result will be 11
print(2 ** 3 * 4) # it will be evaluated from right to left, so the result will be 32