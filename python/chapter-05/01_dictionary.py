marks = {
    "Subrata": 100,
    "Rakesh": 89,
    "Roni": 45
}
print(marks,type(marks))
print(marks["Subrata"])
print(marks.items())
print(marks.keys())
print(marks.values())

#Update Method
print(marks.update({"Subrata": 99}))
print(marks)

#Get Method
print(marks.get("Subrata"))

#Remove Method
marks.pop("Subrata")
print(marks)

#Removes the last inserted key-value pair.
marks.popitem()
print(marks)

#Removes all items.
marks.clear()
print(marks)

#Returns the value if the key exists; otherwise, inserts the key with the default value.
student = {
    "name": "Subrata",
    # "age": 35
}
student.setdefault("age", 25)
print(student)

#Creates a new dictionary with specified keys and a common value.
keys = ("name", "age", "city")
student = dict.fromkeys(keys, "Not Available")
print(student)

#Check if a key exists
student = {
    "name": "Subrata",
    "age": 25
}
print("name" in student)
print("city" in student)

#Loop through keys
student = {
    "name": "Subrata",
    "age": 25
}
for key in student:
    print(key)

#Loop through values
for value in student.values():
    print(value)

#Loop through key-value pairs
for key, value in student.items():
    print(key, ":", value)