
file = open('day12.txt', 'r')
lines = file.readlines()

rows = []
total = 0

for line in lines:
    line_grouping = line.strip().split(' ')
    rows.append((line_grouping[0], [int(x) for x in line_grouping[1].split(',')]))

def is_match(possible, config):
    groupings = []
    cur_group = ''
    for s in possible:
        if s == '?' or s == '#':
            cur_group += s
        else:
            if cur_group != '':
                groupings.append(cur_group)
                cur_group = ''

    if cur_group != '':
        groupings.append(cur_group)
    
    if len(groupings) != len(config):
        return False
    
    for gi in range(len(groupings)):
        if len(groupings[gi]) != config[gi]:
            return False
        
    return True

for r in rows:
    stk = [r[0]]
    while len(stk) > 0:
        str = stk.pop()

        if all(x != '?' for x in str):
            if is_match(str, r[1]):
                total += 1
            else:
                continue

        for i in range(len(str)):
            if str[i] == '?':
                left = str[:i]
                right = str[i + 1:]

                stk.append(left + '.' + right)
                stk.append(left + '#' + right)
                break
        
print(total)