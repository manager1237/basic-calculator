# Creating an empty list
my_list = []

# Appending elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserting 15 at the second position (index 1)
my_list.insert(1, 15)

# Extendind the list [50, 60, 70]
my_list.extend([50, 60, 70])

# Removing the last element
my_list.pop()

#ascending order
my_list.sort()

#the index of the value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

#final list to see the result
print("Final list:", my_list)
