
file = open('day5.txt', 'r')
lines = file.readlines()

maps = []

seeds = [int(x) for x in lines[0].strip().split(': ')[1].split(' ')]

sources = []
for i in range(0, len(seeds), 2):
    sources.append((seeds[i], seeds[i + 1]))

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
    while len(sources) > 0:
        s = sources.pop(0)

        found = False
        for r in m:
            dest = r[0]
            source = r[1]
            length = r[2]

            ss = s[0]
            sl = s[1]

            min_source = source
            max_source = source + length - 1

            min_ss = ss
            max_ss = ss + sl - 1

            if (max_ss < min_source):
                continue

            if (min_ss > max_source):
                continue

            #range before
            before = min_source - min_ss
            if (before > 0):
                sources.append((min_ss, before))
                min_ss = min_source

            #range after
            after = max_ss - max_source
            if (after > 0):
                sources.append((max_source + 1, after))
                max_ss = max_source

            #range included
            offset = min_ss - min_source
            if offset >= 0:
                destinations.append(((dest + offset), max_ss - min_ss))
                found = True
                break

        if not found:
            destinations.append(s)

    sources = destinations

final = []
for s in sources:
    final.append(s[0])

print(min(final))