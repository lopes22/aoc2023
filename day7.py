
file = open('day7.txt', 'r')
lines = file.readlines()

def card_sort(c):
    t = ''
    for s in c:
        if s == 'A':
            t += 'e'
        elif s == 'K':
            t += 'd'
        elif s == 'Q':
            t += 'c'
        elif s == 'J':
            t += 'b'
        elif s == 'T':
            t += 'a'
        else:
            t += s
    return t

hands = {}

for line in lines:
    s = line.strip().split(' ')
    hands[s[0]] = int(s[1])

card_types = []

for h in hands.keys():
    cards = {}
    for c in h:
        if c in cards:
            cards[c] += 1
        else:
            cards[c] = 1

    #5 of a kind
    if len(cards) == 1:
        card_types.append((7, h))
        continue

    #4 of a kind
    if len(cards) == 2 and 4 in cards.values():
        card_types.append((6, h))
        continue

    # full house
    if len(cards) == 2 and 3 in cards.values():
        card_types.append((5, h))
        continue

    # three of a kind
    if len(cards) == 3 and 3 in cards.values():
        card_types.append((4, h))
        continue
    
    # two  pair
    if len(cards) == 3 and 1 in cards.values():
        card_types.append((3, h))
        continue

    # one pair
    if len(cards) == 4:
        card_types.append((2, h))
        continue

    # high card
    if len(cards) == 5:
        card_types.append((1, h))
        continue

sorted_hands = sorted(card_types, key=lambda x: (x[0], card_sort(x[1])))

total = 0
for i in range(len(sorted_hands)):
    sh = sorted_hands[i][1]
    total += hands[sh] * (i + 1)

print(total)