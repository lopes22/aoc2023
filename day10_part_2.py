
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
#q.append(((start[0] + 1, start[1]), [(start[0] + 1, start[1])]))
#q.append(((start[0], start[1] + 1), [(start[0], start[1] + 1)]))
#q.append(((start[0], start[1] - 1), [(start[0], start[1] - 1)]))

end = (start[0] - 1, start[1])
#end = (start[0], start[1] + 1)
#end = (start[0] + 1, start[1])
#end = (start[0] + 1, start[1])

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

final_path_set = set(found_path + [start])


cur_p = start
tiles = set()
for p in found_path:
    # south
    if p[0] == cur_p[0] + 1 and p[1] == cur_p[1]:
        if p[1] != len(rows[0]) - 1 and (p[0], p[1] + 1) not in final_path_set:
            tiles.add((p[0], p[1] + 1))

        if rows[p[0]][p[1]] == 'J':
          if p[0] != len(rows) - 1 and (p[0] + 1, p[1]) not in final_path_set:
            tiles.add((p[0] + 1, p[1]))    

        cur_p = p
        continue

    # north
    if p[0] == cur_p[0] - 1 and p[1] == cur_p[1]:
        if p[1] != 0 and (p[0], p[1] - 1) not in final_path_set:
            tiles.add((p[0], p[1] - 1))

        if rows[p[0]][p[1]] == 'F':
          if p[0] != 0 and (p[0] - 1, p[1]) not in final_path_set:
            tiles.add((p[0] - 1, p[1]))    

        cur_p = p
        continue

    # east
    if p[0] == cur_p[0] and p[1] == cur_p[1] + 1:
        if p[0] != 0  and (p[0] - 1, p[1]) not in final_path_set:
            tiles.add((p[0] - 1, p[1]))

        if rows[p[0]][p[1]] == '7':
            if p[1] != len(rows[0]) - 1  and (p[0], p[1] + 1) not in final_path_set:
                tiles.add((p[0], p[1] + 1))

        cur_p = p
        continue

    # west
    if p[0] == cur_p[0] and p[1] == cur_p[1] - 1:
        if p[0] != len(rows) - 1 and (p[0] + 1, p[1]) not in final_path_set:
            tiles.add((p[0] + 1, p[1]))

        if rows[p[0]][p[1]] == 'L':
            if p[1] != 0  and (p[0], p[1] - 1) not in final_path_set:
                tiles.add((p[0], p[1] - 1))   

        cur_p = p
        continue

print(len(tiles))

final = set()
for a in tiles:
    qq = []
    seenn = set()
    qq.append(a)
    seenn.add(a)
    while len(qq) > 0:
        cur_el = qq.pop(0)

        top = (cur_el[0] - 1, cur_el[1])
        bottom = (cur_el[0] + 1, cur_el[1])
        right = (cur_el[0], cur_el[1] + 1)
        left = (cur_el[0], cur_el[1] - 1)
        if top not in final_path_set and top not in seenn:
            seenn.add(top)
            qq.append(top)
        if bottom not in final_path_set and bottom not in seenn:
            seenn.add(bottom)
            qq.append(bottom)
        if right not in final_path_set and right not in seenn:
            seenn.add(right)
            qq.append(right)
        if left not in final_path_set and left not in seenn:
            seenn.add(left)
            qq.append(left)
    final = final.union(seenn)

print(len(final))
