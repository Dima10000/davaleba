'''1
arr = set(input("your information: ").split())

print("Unique arr:",arr)
'''
'''21 
arr = input("your information: ").split()
unique_arr = frozenset(arr)
print("Unique arr:",unique_arr)

'''

'''3
set1 = {1, 2, 3, 1, 4, 4, 5}
set2 = {1, 2, 6, 7, 8, 5,}
union_sets = tuple(set1.union(set2))
print("Unified sets in tuple:", union_sets)
'''
'''4
arr = input("your numbers: ")
arr1 = arr.split()
arr2 = tuple(map(int, arr1))
unique_list = list(set(arr2))
print("Unique elements :", unique_list)
'''
'''5
people = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]
for name, age in people:
    print(f"Name: {name}, Age: {age}")
'''
'''6'''
list1 = ["Irakli", "Giorgi", "Nona", "Oto"]
list2 = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]
intersection = set(list1).intersection(list2)
print("same names:", intersection)