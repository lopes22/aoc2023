
file = open('day6.txt', 'r')
lines = file.readlines()

time = int(''.join([ x for x in lines[0].strip().split('Time:      ')[1].split(' ') if x != '']))
distance = int(''.join([x for x in lines[1].strip().split('Distance:  ')[1].split(' ') if x != '']))

wins = 0
found = False
for t in range(1, time):
    dist = t * (time - t)

    if dist > distance:
        found = True
        wins += 1
    elif found:
        break 

print(wins)