with open('data6.txt', 'r') as file:
    data = file.read().splitlines()

time = ""
distance = ""

for i in data:
    if 'Time' in i:
        i = i.split(':')
        for n in i[1].split():
            time += n
    elif 'Distance' in i:
        i = i.split(':')
        for n in i[1].split():
            distance += n

time = int(time)
distance = int(distance) 
#print(time)
#print(distance)

winList = []

timeCheck = 0
wins = 0

while timeCheck <= time:
    if timeCheck * (time - timeCheck) > distance:
        #print(f"{timeCheck} times {i - timeCheck} = {timeCheck * (i - timeCheck)}")
        wins += 1
        timeCheck += 1

    else:
        #print('no')
        timeCheck += 1
print(wins)

#print(winList)

