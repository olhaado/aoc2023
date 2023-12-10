with open('data4.txt', 'r') as file:
    data = file.read().splitlines()

print(data)

pointTotal = 0

for i in data:
    i = i.split(':')
    i= i[1].split('|')
    print(i)

    winNums = []
    yourNums = []
    wins = 0

    for x in i[0].split():
        winNums.append(int(x))
    for x in i[1].split():
        yourNums.append(int(x))
    print(winNums)
    print(yourNums)
    for n in winNums:
        if n in yourNums:
            if wins == 0:
                wins += 1
            else:
                wins = wins*2
    print(wins)
    pointTotal += wins

print(pointTotal)


