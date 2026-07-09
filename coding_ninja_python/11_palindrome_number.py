#A Palindrome Number is a number that reads the same forward and backward.
def is_palindrome(num):
    str_num = str(num)# Convert the number to string to check for palindrome
    return str_num == str_num[::-1]# Check if the string is equal to its reverse

# Test the function
print(is_palindrome(int(input("Enter a number: "))))  # True
print(is_palindrome(int(input("Enter another number: "))))  # False