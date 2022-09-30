m = 'This is a String'
print(len(m))
for i, v in enumerate(m):
    print (f'{i} ---> {v}')

#slicing
print(m[:7])
print(m[8:15])
print(m[-11:])


amt = '$3000'
print(int(amt[1:]))

rr = '1,143 ratings | 347 answered questions'
print("No. of answered questions---->", rr[16:])
print('No. of Ratings---->', rr[:13])

