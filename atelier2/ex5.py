given_list = [47, 64, 69, 37, 76, 83, 95, 97]
given_dictionary = {'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':97}
dictionary_values = list(given_dictionary.values())
i=0

while i < len(given_list):
    if given_list[i] not in dictionary_values :
        del given_list[i]
    else :
        i += 1

print(given_list)