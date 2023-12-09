
file = open('day8.txt', 'r')
lines = file.readlines()

nodes = {}

directions = lines[0].strip()

for line in lines[2:]:
    split = line.strip().split(' = ')

    node = split[0]
    elements = split[1].split(', ')
    left = elements[0][1:]
    right = elements[1][:len(elements[1]) - 1]

    nodes[node] = (left, right)

found = False
moves = 0
cur_node = 'AAA'
while not found:
    cur_d = directions[moves % len(directions)]
    n = nodes[cur_node]

    new_node = None
    if cur_d == 'R':
        new_node = n[1]
    if cur_d == 'L':
        new_node = n[0]

    if new_node == 'ZZZ':
        found = True
        
    cur_node = new_node
    moves += 1

print(moves)