
file = open('day10.txt', 'r')
lines = file.readlines()

rows = []

for line in lines:
    rows.append(list(line.strip()))

start = None
for r in range(len(rows)):
    for c in range(len(rows[r])):
        if rows[r][c] == 'S':
            start = (r, c)
            break
    if start != None:
        break

seen = set()

q = []
q.append(((start[0], start[1] - 1), [(start[0], start[1] - 1)]))

end = (start[0] - 1, start[1])

found_path = None
while len(q) > 0:
    cur_el = q.pop(0)
    seen.add(cur_el[0])

    if (cur_el[0] == end):
        found_path = cur_el[1]
        break

    loc = cur_el[0]
    r = loc[0]
    c = loc[1]
    path = cur_el[1]

    if rows[r][c] == '|':
        if r - 1 >= 0  and (r - 1, c) not in seen:
            q.append(((r - 1, c), path + [(r - 1, c)]))
        if r + 1 < len(rows) and (r + 1, c) not in seen:
            q.append(((r + 1, c), path + [(r + 1, c)]))
    if rows[r][c] == '-':
        if c - 1 >= 0  and (r, c - 1) not in seen:
            q.append(((r, c - 1), path + [(r, c - 1)]))
        if c + 1 < len(rows[r]) and (r, c + 1) not in seen:
            q.append(((r, c + 1), path + [(r, c + 1)]))
    if rows[r][c] == 'L':
        if r - 1 >= 0  and (r - 1, c) not in seen:
            q.append(((r - 1, c), path + [(r - 1, c)]))
        if c + 1 < len(rows[r]) and (r, c + 1) not in seen:
            q.append(((r, c + 1), path + [(r, c + 1)]))
    if rows[r][c] == 'F':
        if r + 1 < len(rows) and (r + 1, c) not in seen:
            q.append(((r + 1, c), path + [(r + 1, c)]))
        if c + 1 < len(rows[r]) and (r, c + 1) not in seen:
            q.append(((r, c + 1), path + [(r, c + 1)]))
    if rows[r][c] == 'J':
        if r - 1 >= 0  and (r - 1, c) not in seen:
            q.append(((r - 1, c), path + [(r - 1, c)]))
        if c - 1 >= 0  and (r, c - 1) not in seen:
            q.append(((r, c - 1), path + [(r, c - 1)]))
    if rows[r][c] == '7':
        if r + 1 < len(rows) and (r + 1, c) not in seen:
            q.append(((r + 1, c), path + [(r + 1, c)]))
        if c - 1 >= 0  and (r, c - 1) not in seen:
            q.append(((r, c - 1), path + [(r, c - 1)]))

print(len(found_path + [start]) // 2)


