def is_armstrong_number(number):
    # Convert the number to a string to easily get its digits and count them
    num_str = str(number)
    num_digits = len(num_str)
    
    sum_of_powers = 0
    for digit_char in num_str:
        digit = int(digit_char)
        sum_of_powers += digit ** num_digits
        
    return sum_of_powers == number