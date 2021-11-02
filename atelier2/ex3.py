list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

def count_each(list):
    dictionary = {}
    for element in list:
        if element not in dictionary :  
            dictionary[element] = 1
        else : 
            dictionary[element] += 1

    return dictionary

print(count_each(list))