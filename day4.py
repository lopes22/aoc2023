
file = open('day4.txt', 'r')
lines = file.readlines()

total = 0

cards = []

for line in lines:
    line = line.strip()
    split1 = line.split(': ')
    nums_section = split1[1]

    nums = nums_section.split(' | ')

    winning_nums = nums[0].split(' ')
    player_nums = nums[1].split(' ')

    cards.append((set([x for x in winning_nums if x != '']), [x for x in player_nums if x != '']))

for card in cards:
    wins = -1
    for n in card[1]:
        if n in card[0]:
            wins += 1

    if wins > -1:
        total += 2**wins

print(total)