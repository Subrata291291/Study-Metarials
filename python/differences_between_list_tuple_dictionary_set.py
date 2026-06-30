# 1. List ([]) Mutable

# A list is used when you want a collection of items that you can change.

# fruits = ["Apple", "Banana", "Mango"]

# print(fruits)
# print(fruits[1])

# fruits.append("Orange")

# print(fruits)

# Output

# ['Apple', 'Banana', 'Mango']
# Banana
# ['Apple', 'Banana', 'Mango', 'Orange']


# 2. Tuple (()) Immutable

# A tuple is like a list, but you cannot modify it after it's created.

# student = ("Subrata", 25, "India")

# print(student)
# print(student[0])

# Trying to modify it:

# student[1] = 30

# Output:

# TypeError: 'tuple' object does not support item assignment



# 3. Dictionary ({}) Mutable

# A dictionary stores data as key-value pairs.

# student = {
#     "name": "Subrata",
#     "age": 25,
#     "city": "Kolkata"
# }

# print(student["name"])
# print(student["age"])

# Output

# Subrata
# 25


# 4. Set ({})

# A set stores unique values only.

# numbers = {10, 20, 30, 20, 10}

# print(numbers)

# Output

# {10, 20, 30} #Notice that duplicate values are removed automatically.




