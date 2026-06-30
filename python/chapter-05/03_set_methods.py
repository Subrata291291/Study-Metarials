#Add Method (Adds a single element to the set.)
numbers = {10, 20, 30}
numbers.add(40)
print(numbers) #Output {40, 10, 20, 30}

#Update Method (Adds multiple elements.)
numbers = {10, 20, 30}
numbers.update([40, 50, 60])
print(numbers) #Output {10, 20, 30, 40, 50, 60}

#Remove Methods (Removes an element.)
numbers = {10, 20, 30}
numbers.remove(20)
print(numbers)

#If the element doesn't exist:
numbers.remove(50)
print(numbers) #Output KeyError

#discard Method (Removes an element without raising an error if it doesn't exist.)
numbers = {10, 20, 30}
numbers.discard(50)
print(numbers) #Output {10, 20, 30}

#Pop Method (Removes and returns a random element.)
numbers = {10, 20, 30}
value = numbers.pop()
print(value)
print(numbers)

#Clear Method (Removes all elements.)
numbers = {10, 20, 30}
numbers.clear()
print(numbers) #Output set()

#Copy Method (creates a copy of the set.)
numbers = {10, 20, 30}
new_set = numbers.copy()
print(new_set) #Output {10, 20, 30}

#Union Method (Combines two sets.)
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b)) #Output {1, 2, 3, 4, 5}

#Intersection Method (Returns common elements.)
a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))