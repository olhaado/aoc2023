with open('data6.txt', 'r') as file:
    data = file.read().splitlines()

time = []
distance = []

for i in data:
    if 'Time' in i:
        i = i.split(':') #split string into 'Time:' and numbers
        for n in i[1].split(): #numbers are in index one of the list. split those by spaces
            time.append(int(n)) #add to time list
    elif 'Distance' in i:
        i = i.split(':')
        for n in i[1].split():
            distance.append(int(n))

#print(time)
#print(distance)

winList = []

for num, i in enumerate(time): #enumerate to provide index to look up relative distance
    timeCheck = 0 #time to hold
    distanceCheck = distance[num] #using enumerate to define the matching distance
    wins = 0
    #print(i)
    #print(distanceCheck)

    while timeCheck <= i: #checks if the time to hold the button exceeds total time
        if timeCheck * (i - timeCheck) > distanceCheck:
            #print(f"{timeCheck} times {i - timeCheck} = {timeCheck * (i - timeCheck)}")
            wins += 1
            timeCheck += 1 #continues the loop
        else:
            timeCheck += 1
    winList.append(int(wins)) #add total number of winning options to a list for each race


winMultiplier = 1 #variable to use in for loop to multiply the races
                  #start at 1 so the first number = itself when multiplied

for i in winList:
    winMultiplier = winMultiplier * i

print(winMultiplier)