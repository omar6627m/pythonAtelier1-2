given_list = [1,4.2,45,2,-32,0.435,4,99,0,2]
print('unsorted list',given_list)
print('==================')


def swap(list,i,j) :
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def bubble_sort(list):
    i=0

    while i < len(list) - 1:
        j= i + 1
        while j < len(list):
            if list[i] > list[j]:
                swap(list,i,j)
            j += 1
        i += 1

# bubble_sort(given_list)
# print(given_list)

def selection_sort(list):
    i=0
    while i <= len(list) - 2:
        temp_minimum = i;
        j = i+1
        while j <= len(list) -1:
            if list[temp_minimum] > list[j]:
                temp_minimum = j
            j += 1
        swap(list,i,temp_minimum)
        i += 1

# selection_sort(given_list)
# print(given_list)

def compare(list,current_index):
    if current_index == 0 : 
        return 0
    if list[current_index] < list[current_index -1]:
        swap(list,current_index,current_index -1)
        compare(list,current_index-1)
    else : return 0


def insertion_sort(list):
    i=0

    while i <= len(list) - 1:
        compare(list,i)
        i += 1

insertion_sort(given_list)
print(given_list)