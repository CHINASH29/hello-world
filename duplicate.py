# Checking Duplicates in list
my_list = ['a', 'a', 'b', 'c', 'd', 'd', 'e', 'e', 'e']
dupes = []

for values in my_list:
    if my_list.count(values) > 1:
        if values not in dupes:
            dupes.append(values)

print('Duplicate values are :-', dupes)
