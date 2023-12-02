
file = open('day2.txt', 'r')
lines = file.readlines()

total = 0

games = []

for line in lines:
    line = line.strip()
    split_1 = line.split(': ')
    
    id = int(split_1[0].split(' ')[1])
    rounds_part = split_1[1].split('; ')

    rounds = []
    for round_part in rounds_part:
        colors = {}
        for color_part in round_part.split(', '):
            color_split = color_part.split(' ')
            colors[color_split[1]] = int(color_split[0])

        rounds.append(colors)

    games.append((id, rounds))

for game in games:

    max_red = -1
    max_green = -1
    max_blue = -1
    
    for round in game[1]:
        for color in round.keys():
            if color == 'red' and round[color] > max_red:
                max_red = round[color]

            if color == 'green' and round[color] > max_green:
                max_green = round[color]

            if color == 'blue' and round[color] > max_blue:
                max_blue = round[color]

    total += max_blue * max_red * max_green

print(total)