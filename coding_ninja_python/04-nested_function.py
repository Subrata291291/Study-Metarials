def user_billing_details(name, address, city):
	print("Name is :" , name , "Address is :" , address, "City is :" , city)


def user_payment_details(name, address, city):
	user_billing_details(name, address, city)
	return("Credit Card", "UPI")

user_details = user_payment_details("Subrata" , "Kestoppur , baguihati", "Kolkata")

print(user_details)