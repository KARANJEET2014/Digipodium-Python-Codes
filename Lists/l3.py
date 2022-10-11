x = [2,2,2,2,2,3,3,3,3,3,1,1,1,1,1]

print(x.count(3)) #to count the number of times following number is present in the list
print(x.count(2))
print(x.count(22))

print(x.index(3)) #to check the index of the first occurrence of the element
print(x.index(2))
#print(x.index(22)) #Value error: number is not in the list

z = x # does not copy a list, if x is changed z get changed as well. This list will be a problem in future.
y = x.copy() # to copy a list
z.append(10)
y.append(20)
print (z)
print (x is y)
print (x is z)
print(x)
print(y)
print(z)