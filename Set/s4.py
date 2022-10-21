a = {'RAM', 'SHYAM', 'HARI', 'GITA', 'SITA'}
b = {'ALEX', 'MARK', 'ELIZA', 'BENNY', 'SUNNY'}
c = {'RAM', 'ALEX', 'GITA', 'TANYA', 'SERGEI'}


#UNION
ab = a|b
print("Union=> ", ab)


#Or
ab = a.union(b)
print("Union=> ", ab)


#Intersection
ac = a & c # a.intersection(c) also works
print('Intersection =>', ac)


#or
ab = a & b
print('Intersection =>', ab) #There is nothing common, hence no answer is coming out


#Difference
ac = a - c # a.difference(c) also works
print('difference =>', ac) #This will display Unique items present in a

ca = c - a
print('Diffrence =>', ca) # This will print the unique items present in c


#Symmetric Difference
ac = a ^ c # a.symmetricdifference(c) also works here
print('Symmetric Difference =>', ac)

