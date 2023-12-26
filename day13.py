
file = open('day13.txt', 'r')
lines = file.readlines()

puzzles = []
total = 0

cur_puzzle = []
for line in lines:
    if line.strip() == '':
        puzzles.append(cur_puzzle)
        cur_puzzle = []
    else:
        cur_puzzle.append(list(line.strip()))

if len(cur_puzzle) > 0:
    puzzles.append(cur_puzzle)

for p in puzzles:
    found = False
    for r in range(len(p) - 1):
        no = False
        for c in range(len(p[r])):
            if p[r][c] != p[r + 1][c]:
                   no = True
                   break 
        if no:
            continue
        else:
            left = r - 1
            right = r + 2
            verified = True
            while left >= 0 and right < len(p) and verified:
                for c in range(len(p[r])):
                    if p[left][c] != p[right][c]:
                        verified = False
                        break

                left = left - 1
                right = right + 1

            
            if verified:
                found = True
                break

    if found:
        total += 100 * (r + 1)
        continue
    
    for c in range(len(p[0]) - 1):
        no = False
        for r in range(len(p)):
            if p[r][c] != p[r][c + 1]:
                   no = True
                   break 
        if no:
            continue
        else:
            left = c - 1
            right = c + 2
            verified = True
            while left >= 0 and right < len(p[0]) and verified:
                for r in range(len(p)):
                    if p[r][left] != p[r][right]:
                        verified = False
                        break

                left = left - 1
                right = right + 1

            
            if verified:
                found = True
                break

    if found:
        total += c + 1
        continue

print(total)