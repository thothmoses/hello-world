def square(number):
        if number > 64:
            # when the square value is not in the acceptable range        
            raise ValueError("square must be between 1 and 64")
            quit
        if number < 1:
            # when the square value is not in the acceptable range        
            raise ValueError("square must be between 1 and 64")
            quit
        value = (2 ** number)/2
        #print("number", number)
        #print("value", value)
        return value
    
def total():
    tot = 0
    i = 3
    while i < 64:
        i += 1
        tot = tot + square(i)
    print("tot", int(tot))
    return int(tot)-1
    
