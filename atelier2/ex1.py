l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3 = []

i = 0
while i < len(l1):
    if not i % 2 == 0:
        l3.append(l1[i])
    i += 1

i = 0
while i < len(l2) :
    if i % 2 == 0:
        l3.append(l2[i])
    i += 1

print(l3)