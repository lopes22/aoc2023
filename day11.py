
file = open('day11.txt', 'r')
lines = file.readlines()

rows = []
galaxies = []
pairs = []
total = 0

for line in lines:
    rows.append(list(line.strip()))

r_counter = 0
while r_counter < len(rows):
    g_found = False
    for c in range(len(rows[r_counter])):
        if rows[r_counter][c] == '#':
            g_found = True
    if not g_found:
        rows.insert(r_counter, ['.' for x in range(len(rows[r_counter]))])
        r_counter += 2
    else:
        r_counter += 1

c_counter = 0
while c_counter < len(rows[0]):
    g_found = False
    for r in range(len(rows)):
        if rows[r][c_counter] == '#':
            g_found = True
            break
    if not g_found:
        for r in range(len(rows)):
            rows[r].insert(c_counter, '.')
        c_counter += 2
    else:
        c_counter += 1

for r in range(len(rows)):
    for c in range(len(rows[r])):
        if rows[r][c] == '#':
            galaxies.append((r, c))

for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        pairs.append((galaxies[i], galaxies[j]))

for pair in pairs:
    start = pair[0]
    end = pair[1]

    total += abs(start[0] - end[0]) + abs(start[1] - end[1])

print(total)
