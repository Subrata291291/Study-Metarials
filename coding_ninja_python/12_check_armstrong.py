def check_armstrong(num):
    # Convert the number to string to easily iterate over digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the sum of the digits raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum of powers is equal to the original number
    return sum_of_powers == num