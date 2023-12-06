
file = open('day5.txt', 'r')
lines = file.readlines()

maps = []

sources = [int(x) for x in lines[0].strip().split(': ')[1].split(' ')]

cur_map = None
for line in lines[1:]:
    line = line.strip()

    if line == '':
        continue

    if line[0].isnumeric():
        cur_map.append([int(x) for x in line.split(' ')])
    else:
        cur_map = []
        maps.append(cur_map)

for m in maps:
    destinations = []
    for s in sources:
        found = False
        for r in m:
            dest = r[0]
            source = r[1]
            length = r[2]

            if s >= source and s <= (source + length):
                offset = s - source
                destinations.append(dest + offset)
                found = True
                break

        if not found:
            destinations.append(s)

    sources = destinations

print(min(sources))