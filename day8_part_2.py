from math import lcm

file = open('day8.txt', 'r')
lines = file.readlines()

nodes = {}
start_nodes = []
end_nodes = []

directions = lines[0].strip()

for line in lines[2:]:
    split = line.strip().split(' = ')

    node = split[0]
    elements = split[1].split(', ')
    left = elements[0][1:]
    right = elements[1][:len(elements[1]) - 1]

    nodes[node] = (left, right)

    if node[2] == 'A':
        start_nodes.append(node)

    if node[2] == 'Z':
        end_nodes.append(node)

final = []

for start in start_nodes:
    for end in end_nodes:
        found = False
        moves = 0
        cur_node = start
        seen = set()

        while not found:
            cur_d = directions[moves % len(directions)]

            n = nodes[cur_node]
            s = (n, moves % len(directions))

            if s in seen:
                break

            seen.add(s)

            new_node = None
            if cur_d == 'R':
                new_node = n[1]
            if cur_d == 'L':
                new_node = n[0]

            if new_node == end:
                found = True
                
            cur_node = new_node
            moves += 1

        if found:
            final.append(moves)


print(lcm(*final))