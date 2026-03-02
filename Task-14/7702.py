from string import printable

b = set()
for y in printable[9:18]:
    for x in printable[:int(y, 18)]:
        b |= {int(f'5{x}{y}A', 18) + int(f'18{x}7', int(y, 18))}

print(len(b))