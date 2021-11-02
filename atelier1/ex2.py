def to_binary(num):
    rest = []

    i= 1
    number = num; 
    
    while  (not number == 0) :
        if number%2 == 1:
            rest.insert(0,1)
        else :
             rest.insert(0,0)
        number = int(number / 2)

    binary_value_in_string = '' 
    for element in rest :
        binary_value_in_string += str(element)
    
    return(binary_value_in_string)


print(to_binary(77)) # prints: 1001101