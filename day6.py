
file = open('day6.txt', 'r')
lines = file.readlines()

total = 1

times = [int(x) for x in lines[0].strip().split('Time:      ')[1].split(' ') if x != '']
distances = [int(x) for x in lines[1].strip().split('Distance:  ')[1].split(' ') if x != '']

for i in range(len(times)):
    t = times[i]
    d = distances[i]

    wins = 0
    found = False
    for time in range(1, t):
        dist = time * (t - time)

        if dist > d:
            found = True
            wins += 1
        elif found:
            break 
        
    total *= wins

print(total)