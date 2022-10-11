colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown', 'black', 'white', 'grey', 'pink', 'violet']

colors_with_a = []
colors_ending_with_n = []
colors_starting_with_b = []

for color in colors:
    if'a' in color:
        colors_with_a.append(color)
    if color.endswith('n'):
        colors_ending_with_n.append(color)
    if color.startswith('b'):
        colors_starting_with_b.append(color)

print(colors_with_a)
print(colors_ending_with_n)
print(colors_starting_with_b)
