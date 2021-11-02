set1 = {23, 42, 65, 57, 78, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}


def intersect_delete(first_set,second_set):
    intersection = first_set.intersection(second_set)
    first_set = first_set.difference(second_set)

    return {'first_set':first_set,'intersection':intersection}

result = intersect_delete(set1,set2)

print(f"Intersection: {result['intersection']}")
print(f"Set 1 apres suppression: {result['first_set']}")