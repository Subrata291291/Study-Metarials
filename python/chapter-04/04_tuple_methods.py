data = ("Subrata", 75, 512.25, " ")

print(data)

count_75 = data.count(75)
print("Count of 75:", count_75)

index_512 = data.index(512.25)
print("Index of 512.25:", index_512)


#tuple length
data = (1,2,3,4,5)
print(len(data))

#Membership Operators
fruits = ("Apple","Banana","Orange")
print("Apple" in fruits)
print("Mango" in fruits)

#Concatenation
a = (1,2,3)
b = (4,5,6)
print(a+b)

#Repetition
a = (10,20)
print(a*3)

#Nested Tuple
student = (
    ("Subrata",75),
    ("Rahul",80),
    ("Ankit",90)
)
print(student[1])
print(student[1][0])
print(student[1][1])


#Tuple Packing
student = "Subrata",25,"India"
print(student)

#Tuple Unpacking
name, age, country = ("Subrata",25,"India")
print(name)
print(age)
print(country)

#Swapping Variables
a = 10
b = 20
a, b = b, a
print(a)
print(b)

#Built-in Functions
numbers = (10,20,30,40,50)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#Converting List to Tuple
mylist = [10,20,30]
mytuple = tuple(mylist)
print(mytuple)

#Converting Tuple to List
mytuple = (10,20,30)
mylist = list(mytuple)
print(mylist)

#Deleting a Tuple
data = (10,20,30)
del data
print(data)