total = 0
while True:
    num=input("Enter a number")
    if not num:
        break
    if num.isnumeric():
        total = total + int(num)
    print(f"Total => {total}")

