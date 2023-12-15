
file = open('day11.txt', 'r')
lines = file.readlines()

rows = []
galaxies = []
pairs = []
total = 0

for line in lines:
    rows.append(list(line.strip()))

rows_to_expand = []
for r in range(len(rows)):
    g_found = False
    for c in range(len(rows[r])):
        if rows[r][c] == '#':
            g_found = True
            break
    if not g_found:
        rows_to_expand.append(r)

cols_to_expand = []
for c in range(len(rows[0])):
    g_found = False
    for r in range(len(rows)):
        if rows[r][c] == '#':
            g_found = True
            break
    if not g_found:
        cols_to_expand.append(c)

for r in range(len(rows)):
    for c in range(len(rows[r])):
        if rows[r][c] == '#':
            er = sum(1 for i in rows_to_expand if i < r)
            ec = sum(1 for i in cols_to_expand if i < c)
            galaxies.append((r + (er * 999999), c + (ec * 999999)))

for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        pairs.append((galaxies[i], galaxies[j]))

for pair in pairs:
    start = pair[0]
    end = pair[1]

    total += abs(start[0] - end[0]) + abs(start[1] - end[1])

print(total)
