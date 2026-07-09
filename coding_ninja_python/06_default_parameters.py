def payment_through(payment_mode="Cash"):
    print(f"Payment through {payment_mode}")

payment_through("Credit Card") #if user provides the value for the parameter, then that value will be used. In this case, "Credit Card" is passed as an argument, so it will be printed.
payment_through()#if user does not provide the value for the parameter, then the default value will be used. In this case, no argument is passed, so the default value "Cash" will be printed.



def payment_through(payment_mode="Cash", date_of_payment="Today"):
    print(f"Payment through {payment_mode}", "on", date_of_payment)

payment_through("Credit Card" , "2023-01-01") #if user provides the value for the parameter, then that value will be used. In this case, "Credit Card" and "2023-01-01" are passed as arguments, so they will be printed.
payment_through() #if user does not provide the value for the parameter, then the default value will be used. In this case, no argument is passed, so the default value "Cash" and "Today" will be printed.