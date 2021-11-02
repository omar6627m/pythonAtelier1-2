def fibo(num):
    if num == 0 : return 0
    if num == 1 : return 1

    return fibo(num -1) + fibo(num-2)


term = int(input('enter the last term: '))

i=0

while i <= term :
    print(f'{fibo(i)} ')
    i+= 1
