#Clean a list of a duplicate values

x = [1,1,2,2,3,3,5,5,1,1,2,2,3,3,5,5,8]
print(x, 'Duplicated values')
x = list(set(x)) #removes duplicates
print(x, 'Cleaned List')


#Interconversion of data-structure
x = [1,2,3,4,5,5,4,3,2,1]
print(x, 'List')

x = tuple(x) #convert list to tuple
print (x, 'Tuple')

x = set(x) #convert tuple to set
print(x, 'set')

x = list(x) # convert set to list
print(x, 'list')


