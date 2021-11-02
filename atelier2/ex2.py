given_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
length = len(given_list)
part1 = []
part2 = []
part3 = []

if( length % 3 == 0) :
    part1 = list(reversed( given_list[:length//3]))
    part2 = list(reversed(given_list[length//3:2*(length//3)]))
    part3 = list(reversed(given_list[2*(length//3):]))

print(part1,part2,part3)