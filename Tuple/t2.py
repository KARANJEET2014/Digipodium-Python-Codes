x = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print (x)
print(type(x))

#assigning the variables in Python
a, b = 10, 20 # 2 values are stored in 2 variables
print(a, b)
a = 10, 20 # 2 values are packed in 1 variable as a tuple
print (a, type(a))

#special cases of assigning the variables
x, *y = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 #1 value is stored in x and rest is stored in y as a list
print (x,y)
print (type(x), type (y))

#Concatenation
print((1, 2, 3) + (4, 5, 6))

#Repeat
print(("Repeat",) * 3)

my_tuple = ('a', 'p', 'p', 'l', 'e')
print(my_tuple.count('p'))
print(my_tuple.index('l'))

