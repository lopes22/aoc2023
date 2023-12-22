
file = open('day12.txt', 'r')
lines = file.readlines()

rows = []
total = 0

for line in lines:
    line_grouping = line.strip().split(' ')
    rows.append((line_grouping[0], [int(x) for x in line_grouping[1].split(',')]))

expanded_rows = []
for r in rows:
    str = r[0]
    config = r[1]

    new_str = r[0]
    new_config = [] + r[1]
    for i in range(4):
        new_str += '?' + str
        new_config += config

    expanded_rows.append((new_str, new_config))

def r(cur_el, cur_gi, cur_i, cur_contig, config, cache):
    k = (cur_gi, cur_i, cur_contig)

    if (k in cache):
        return cache[k]

    for i in range(cur_i, len(cur_el)):
        if cur_gi == len(config) - 1 and cur_contig == config[cur_gi] and all([x != '#' for x in cur_el[i:]]):
            break

        if cur_el[i] == '.':

            if cur_contig > 0:         
                if cur_contig != config[cur_gi]:
                    return 0

                if cur_gi + 1 < len(config):
                    cur_gi += 1
                    cur_contig = 0

            continue

        if cur_el[i] == '#':
            cur_contig += 1

            if cur_contig > config[cur_gi]:
                return 0

            continue

        if cur_el[i] == '?':
            left = cur_el[:i]
            right = cur_el[i + 1:]

            withsep = left + '.' + right
            withgear = left + '#' + right

            t = 0
            if cur_contig == config[cur_gi] and cur_gi + 1 < len(config):
                t += r(withsep, cur_gi + 1, i + 1, 0, config, cache)
            elif cur_contig == 0:
                t += r(withsep, cur_gi, i + 1, 0, config, cache)

            if cur_contig < config[cur_gi]:
                t += r(withgear, cur_gi, i + 1, cur_contig + 1, config, cache)

            cache[k] = t

            return t

    if cur_contig == config[cur_gi] and cur_gi == len(config) - 1:
        return 1
    else:
        return 0

for row in expanded_rows:
    str = row[0]
    config = row[1]
    cache = {}

    total += r(str, 0, 0, 0, config, cache)     

print(total)