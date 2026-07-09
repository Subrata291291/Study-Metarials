import array

# Creating an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])

print(f"Original array: {arr}")  # Output: array('i', [1, 2, 3, 4, 5])
print(f"Original array: {arr[1:4]}")  # Output: array('i', [2, 3, 4])

arr.append(6)  # Adding an element to the end of the array
print(f"Array after appending 6: {arr}")  # Output: array('i', [1, 2, 3, 4, 5, 6])

arr.insert(2, 10)  # Inserting an element at index 2
print(f"Array after inserting 10 at index 2: {arr}")  # Output: array('i', [1, 2, 10, 3, 4, 5, 6])

arr.remove(3)  # Removing the first occurrence of the value 3
print(f"Array after removing 3: {arr}")  # Output: array('i', [1, 2, 10, 4, 5, 6])

arr.pop()  # Removing the last element
print(f"Array after popping the last element: {arr}")  # Output: array('i', [1, 2, 10, 4, 5])

arr.pop(1)  # Removing the element at index 1
print(f"Array after popping the element at index 1: {arr}")  # Output: array('i', [1, 10, 4, 5])

arr.sort()  # Sorting the array
print(f"Array after sorting: {arr}")  # Output: array('i', [1, 4, 5, 10])

arr.reverse()  # Reversing the array
print(f"Array after reversing: {arr}")  # Output: array('i', [10, 5, 4, 2, 1])

arr.extend([7, 8, 9])  # Extending the array with another list
print(f"Array after extending with [7, 8, 9]: {arr}")  # Output: array('i', [10, 5, 4, 2, 1, 7, 8, 9])

arr.index(10)  # Finding the index of the first occurrence of the value 10
print(f"Index of 10 in the array: {arr.index(10)}")  # Output: 0

arr.count(4)  # Counting the occurrences of the value 4
print(f"Count of 4 in the array: {arr.count(4)}")  # Output: 1

arr.typecode  # Getting the type code of the array
print(f"Type code of the array: {arr.typecode}")  # Output: 'i'

arr.buffer_info()  # Getting the buffer information of the array
print(f"Buffer info of the array: {arr.buffer_info()}")  # Output: (address, length) where address is the memory address of the array and length is the number of elements in the array.

arr.tolist()  # Converting the array to a list
print(f"Array converted to list: {arr.tolist()}")  # Output: [5, 4, 10, 2, 1, 7, 8, 9]

arr.fromlist([11, 12, 13])  # Adding elements from a list to the array
print(f"Array after adding elements from list [11, 12, 13]: {arr}")  # Output: array('i', [5, 4, 10, 2, 1, 7, 8, 9, 11, 12, 13])

arr.tobytes()  # Converting the array to bytes
print(f"Array converted to bytes: {arr.tobytes()}")  # Output: b'\x05\x00\x00\x00\x04\x00\x00\x00\x0a\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x07\x00\x00\x00\x08\x00\x00\x00\t\x00\x00\x00'

arr.frombytes(b'\x0e\x00\x00\x00\x0f\x00\x00\x00')  # Adding elements from bytes to the array
print(f"Array after adding elements from bytes: {arr}")  # Output: array('i', [5, 4, 10, 2, 1, 7, 8, 9, 11, 12, 13, 14, 15])
