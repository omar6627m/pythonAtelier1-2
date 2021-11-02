def inverse(word):
    if len(word) < 2 : return word
    
    return word[-1] + inverse(word[:-1])

print(inverse('string to be reversed'))