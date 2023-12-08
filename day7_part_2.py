
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
            t += '1'
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
    j_count = 0
    for c in h:
        if c == 'J':
            j_count += 1
            continue

        if c in cards:
            cards[c] += 1
        else:
            cards[c] = 1

    if j_count == 5:
        card_types.append((7, h))
        continue

    max_k = ''
    max_v = -1
    for k in cards.keys():
        if cards[k] > max_v:
            max_k = k
            max_v = cards[k]

    cards[max_k] += j_count

    #5 of a kind
    if 5 in cards.values():
        card_types.append((7, h))
        continue

    #4 of a kind
    if 4 in cards.values():
        card_types.append((6, h))
        continue

    # full house
    if 2 in cards.values() and 3 in cards.values():
        card_types.append((5, h))
        continue

    # three of a kind
    if 3 in cards.values():
        card_types.append((4, h))
        continue
    
    # two  pair
    if list(cards.values()).count(2) == 2:
        card_types.append((3, h))
        continue

    # one pair
    if 2 in cards.values():
        card_types.append((2, h))
        continue

    card_types.append((1, h))

sorted_hands = sorted(card_types, key=lambda x: (x[0], card_sort(x[1])))

total = 0
for i in range(len(sorted_hands)):
    sh = sorted_hands[i][1]
    total += hands[sh] * (i + 1)

print(total)