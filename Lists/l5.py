#WAP to take 10 float or integer numbers from the user and store them in a list

x = []
for i in range (10):
    data = input ('Enter a float or integer value: ')
    if '.' in data and data.count('.') == 1:
        p1,p2 = data.split('.')
        if p1.isnumeric() and p2.isnumeric():
            x.append(float(data))
    if data.isnumeric():
        x.append(int(data))

print(x)
