print ('SIMPLE INTEREST CALCULATOR')

p = int (input('Principle=>     '))
r = float(input('Rate of Interest=>     '))
t = int(input('Duration=>       '))

si = p * r * t / 100
print ('The calculated Simple Interest is=> ', si)