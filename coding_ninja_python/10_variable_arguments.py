def sum_of_numbers(*numbers): #This function takes variable number of arguments (args as *)
    print("The sum of the numbers is:",(numbers))

sum_of_numbers(10, 20, 30)



def sum_of_numbers(*numbers): #This function takes variable number of arguments
    print("The sum of the numbers is:",sum(numbers))#sum() function is used to calculate the sum of the numbers

sum_of_numbers(10, 20, 30)


def print_student_details(**details): #This function takes variable number of keyword arguments (kwargs as **)
    print("Student Details:" , details)

print_student_details(name="Alice", age=20, grade="A")