with open('test.txt', 'r') as file:
    data = file.read().splitlines()

lines = [i.split(' ') for i in data]
newLines = []
for x in lines:
    tempList = []
    for y in x:
        tempList.append(int(y))
    newLines.append(tempList)

print(newLines)

def difSequence(subList):
    tempList = []
    for num, j in enumerate(subList):
        try:
            if subList[num+1]:
                tempList.append(subList[num+1] - subList[num])
        except:
            break
    return tempList

for i in newLines:
    lineChecks = []
    lineChecks.append(difSequence(i))
    tempoList = difSequence(i)
    temporList = difSequence(tempoList)
    print(sum(lineChecks[0]))
    print(sum(tempoList))
    print(sum(temporList))