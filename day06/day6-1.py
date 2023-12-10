with open('data6.txt', 'r') as file:
    data = file.read().splitlines()

time = []
distance = []

for i in data:
    if 'Time' in i:
        i = i.split(':')
        for n in i[1].split():
            time.append(int(n))
    elif 'Distance' in i:
        i = i.split(':')
        for n in i[1].split():
            distance.append(int(n))

#print(time)
#print(distance)

winList = []

for num, i in enumerate(time):
    timeCheck = 0
    distanceCheck = distance[num]
    wins = 0
    #print(i)
    #print(distanceCheck)

    while timeCheck <= i:
        if timeCheck * (i - timeCheck) > distanceCheck:
            #print(f"{timeCheck} times {i - timeCheck} = {timeCheck * (i - timeCheck)}")
            wins += 1
            timeCheck += 1

        else:
            #print('no')
            timeCheck += 1
    winList.append(int(wins))
    #print(wins)

#print(winList)

winMultiplier = 1

for i in winList:
    winMultiplier = winMultiplier * i

print(winMultiplier)