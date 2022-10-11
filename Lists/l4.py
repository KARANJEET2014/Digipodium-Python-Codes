#WAP to add 10 numbers in a list by the user input

num = []
for i in range(10):
    data = input("Enter a number:  ")
    if data.isnumeric():
        num.append(int(data))

print("Your data => ", num)