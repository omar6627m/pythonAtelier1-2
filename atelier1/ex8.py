def char_frequency(word,char,initial_count= 0):
    if len(word) < 1 : return initial_count

    if word[0] == char : return char_frequency(word[1:],char,initial_count+1)
    return char_frequency(word[1:],char,initial_count)


print(char_frequency('ramobar','r')) # prints: 2