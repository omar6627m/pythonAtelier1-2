matrix = [[1,2,3],[4,5,6],[7,8,9]]

position = ''
i = 0
j = 0

target= int(input('enter the number you\'re looking for: '))

while i < len(matrix) :
    j=0
    while j < len(matrix[i]):
        if matrix[i][j] == target :
            position = str(i) + ',' + str(j) 
            break
        j += 1
    i += 1

print(f'target position in the matrix is {position}')