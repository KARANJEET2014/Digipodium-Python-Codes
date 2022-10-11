#WAP to find the sum, mean, median, mode max and min in the list of numbers.

import math, statistics
x = []
for i in range(10):
    data = input("Enter a number:  ")
    if data.isnumeric():
        x.append(int(data))

print("Your data => ", x)

total = sum(x)
mean = sum(x)/len(x)
x_max = max(x)
x_min = min(x)
median = statistics.median(x)
mode = statistics.mode(x)

print (f'Sum : {total}, Mean: {mean}, Max: {x_max}, Min: {x_min}, Median: {median}, Mode: {mode}')