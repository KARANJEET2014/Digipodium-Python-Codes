my_set = {1, 3}
print(my_set)

#add an element
#Output: {1, 2, 3}
my_set.add(2)
print(my_set)

#add multiple eleements
#Output: {1, 2, 3, 4}
my_set.update([2, 3, 4])
print(my_set)

#add list and set
#Output: {1, 2, 3, 4, 5, 6, 7, 8}
my_set.update([4,5], {1,6,7,8})
print(my_set)