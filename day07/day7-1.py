#goal: assign point values to each hand in a game. 
#hands with same value then get ranked based on highest card
#once ordered, cards get rank from 1-x (total games),1 as last place, multiplying their bet by their rank.
#find total winnings by adding each hands winnings together
with open("test.txt") as file:
    data = file.read().split('\n')

lines = [i.split(' ') for i in data]

handCounts = []

for i in lines:
    charCountList = []

    for j in i[0]:
        charCountList.append(int(i[0].count(j)))
    handCounts.append(charCountList)

print(handCounts)

for num, h in enumerate(handCounts):
    if max(h) == 5:
        print('5kind')
        lines[num].append(1)
    elif max(h) == 4:
        print('4kind')
        lines[num].append(2)
    elif max(h) == 3 and 2 in h:
        print('FullHouse')
        lines[num].append(3)
    elif max(h) == 3 and 2 not in h:
        print('3kind')
        lines[num].append(4)
    elif max(h) == 2 and h.count(2) == 4:
        print('twopair')
        lines[num].append(5)
    elif max(h) == 2 and h.count(2) == 2:
        print('onepair')
        lines[num].append(6)
    else:
        print('nomatch')
        lines[num].append(7)

#assign value to each card
card_dict = {'A': 14, 'K' : 13, 'Q' : 12, 'J' : 11, 'T' : 10, '9': 9, '8' : 8, '7' : 7, '6' : 6, '5' : 5, '4' : 4, '3' : 3, '2' : 2, '0' : 0}

print(lines)

rank = 4

for i in lines:
    bestOfHand = "00000"
    if i[2] == rank:
        for j in i[0]:
            j = card_dict[j]
            print(j)
            if j > card_dict[bestOfHand[0]]:
                print('yes')
                bestOfHand = i[0]
                break
            #elif:
            else:
                print('no')
    #rank += 1



        



