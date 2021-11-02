def count_digit(num,initial_counter=0):
    if num == 0 : return initial_counter

    return count_digit(int(num/10),initial_counter+1) 

print(count_digit(123456)) # prints: 6