#Getting a list slice

l = [10,20,30,40,50,60,70,80,90,100]
slice1 = l[3:-2]
print(slice1)


#Append function-
fruits = []
fruits.append('apple')
fruits.append('banana')
fruits.append('cherry')
fruits.append('guava')
fruits
print(fruits)
noble_metals = ['Gold', 'Silver', 'Platinum']
fruits.append(noble_metals)
print(fruits)


#Insert Function-
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, 'orange')
fruits.insert(50000, 'lemon') #As the list is not so big hence, the fruit is put at the last
print(fruits)


#Extend function-
fruits = ['apple', 'banana', 'cherry', 'walnut']
dry_fruits = ['almond', 'cashew', 'walnut']
fruits.extend(dry_fruits)
fruits
print(fruits)



#Sort function-
fruits = ['apple', 'banana', 'orange', 'pear', 'grape']
fruits.sort()
fruits
print(fruits)



#Remove function-
fruits = ['Cherry', 'Guava', 'Apple', 'Banana']
fruits.remove('Cherry')
fruits
print(fruits)


#Pop function-
fruits = ['Cherry', 'Guava', 'Apple', 'Banana']
fruits.pop(3)#remove element by index
fruits.pop()#remove last element(default, if address is not given)
print(fruits)


#Reverse function-
fruits = ['Cherry', 'Guava', 'Apple', 'Banana']
fruits.reverse()
print(fruits)
