
file = open('day9.txt', 'r')
lines = file.readlines()

rows = []

for line in lines:
    rows.append([int(x) for x in line.strip().split(' ')])

total = 0
for r in rows:
    histories = [r]
    cur_sequence = r

    while not all(x == 0 for x in cur_sequence):
        new_sequence = []
        for i in range(1, len(cur_sequence)):
            new_sequence.append(cur_sequence[i] - cur_sequence[i - 1])

        histories.append(new_sequence)
        cur_sequence = new_sequence 
    
    cur_element = 0
    for hi in range(len(histories) - 2, -1, -1):
        cur_element = histories[hi][-1] + cur_element
    
    total += cur_element

print(total)

