
file = open('day12.txt', 'r')
lines = file.readlines()

rows = []
total = 0

for line in lines:
    line_grouping = line.strip().split(' ')
    rows.append((line_grouping[0], [int(x) for x in line_grouping[1].split(',')]))

for r in rows:
    str = r[0]
    config = r[1]

    stk = [(str, 0, 0, 0)]
    while len(stk) > 0:
        cur = stk.pop()

        cur_el = cur[0]
        cur_gi = cur[1]
        cur_i = cur[2]
        cur_contig = cur[3]

        dead = False
        for i in range(cur_i, len(cur_el)):
            if cur_gi == len(config) - 1 and cur_contig == config[cur_gi] and all([x != '#' for x in cur_el[i:]]):
                break

            if cur_el[i] == '.':

                if cur_contig > 0:         
                    if cur_contig != config[cur_gi]:
                        dead = True
                        break

                    if cur_gi + 1 < len(config):
                        cur_gi += 1
                        cur_contig = 0

                continue

            if cur_el[i] == '#':
                cur_contig += 1

                if cur_contig > config[cur_gi]:
                    dead = True
                    break

                continue

            if cur_el[i] == '?':
                left = cur_el[:i]
                right = cur_el[i + 1:]

                withsep = left + '.' + right
                withgear = left + '#' + right

                if cur_contig == config[cur_gi] and cur_gi + 1 < len(config):
                    stk.append((withsep, cur_gi + 1, i + 1, 0))
                elif cur_contig == 0:
                    stk.append((withsep, cur_gi, i + 1, 0))

                if cur_contig < config[cur_gi]:
                    stk.append((withgear, cur_gi, i + 1, cur_contig + 1))

                dead = True
                break

        if not dead and cur_contig == config[cur_gi] and cur_gi == len(config) - 1:
            total += 1

print(total)