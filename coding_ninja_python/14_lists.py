# num = [1, 2, 3, 4, 5]
# print(num)
# print(type(num))


# #Slice Method
# print(num[1:4])  # Output: [2, 3, 4]
# print(num[::2])  # Output: [1, 3, 5]
# print(num[::-1])  # Output: [5, 4, 3, 2, 1]
# print(num[1: -1])  # Output: [2, 3, 4]
# print(num[1: -1: 2])  # Output: [2, 4]


# #max value show
# number = list(map(int, input("Enter the number of elements in the list: ").split()))
# max_value = max(number)
# print(f"Maximum value in the list: {max_value}")


# #palindrome check
# def is_palindrome(s):
#     return s == s[::-1]
# # Example usage
# input_string = input("Enter a string to check if it's a palindrome: ")
# if is_palindrome(input_string):
#     print(f"'{input_string}' is a palindrome.")
# else:
#     print(f"'{input_string}' is not a palindrome.")


# #Print the list in a specific order from 1 to n, where odd numbers are printed in ascending order and even numbers are printed in descending order.
# def arrange(arr, n):

#     index = 0

#     # Fill odd numbers
#     for i in range(1, n + 1, 2):
#         arr[index] = i
#         index += 1

#     # Fill even numbers in reverse
#     if n % 2 == 0:
#         start = n
#     else:
#         start = n - 1

#     for i in range(start, 1, -2):
#         arr[index] = i
#         index += 1

#Linear Search Function
# def linearsearch(arr, n, key):
#     for i in range(n):
#         if arr[i] == key:
#             return i
#     return -1

# arr = [5, 7, 2, 8, 4]
# n = len(arr)
# x = int(input("Enter the element to search: "))

# result = linearsearch(arr, n, x)
# print(result)

#Find the second largest element in an array
def secondLargestElement(arr, n):

    if n < 2:
        return -1

    largest = float('-inf')
    second = float('-inf')

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num != largest and num > second:
            second = num

    if second == float('-inf'):
        return -1

    return second


n = int(input("Enter size: "))

arr = list(map(int, input("Enter elements: ").split()))

print(secondLargestElement(arr, n))