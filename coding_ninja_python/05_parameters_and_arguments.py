def details_of_user(name, age, city, phone): #These are parameters. Parameters are the variables that are defined in the function definition.
    print("Name :" , name , "Age :" , age , "City :" , city , "phone :" , phone)

details_of_user("Subrata", 25, "Kolkata", 1234567890) #These are positional arguments. The order of the arguments matters here. If we change the order of the arguments, then the output will be different.


#Calling the function with keyword arguments. Here, the order of the arguments does not matter. We can pass the arguments in any order.
def calculate_area(length, breadth):
    area = length * breadth
    print("Area of rectangle is :" , area)

calculate_area(length=10, breadth=5)