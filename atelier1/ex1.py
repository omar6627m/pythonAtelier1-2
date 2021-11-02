# factorial function
def factorial(num):
    if num == 1 : return 1

    return num * factorial(num -1)

# sum of n!/n
def sum(num):
    if num == 1 : return 1

    return factorial(num)/num + sum(num-1)

print(sum(5)) #inputs 34.0