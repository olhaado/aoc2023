with open('data9.txt', 'r') as file:
    data = file.read().splitlines()

lines = [i.split(' ') for i in data]
newLines = []
for x in lines:
    tempList = []
    for y in x:
        tempList.append(int(y))
    newLines.append(tempList)


def difSequence(subList):
    tempList = []
    for num, j in enumerate(subList):
        try:
            if subList[num+1] or subList[num+1] == 0:
                tempList.append(subList[num+1] - subList[num])
        except:
            break
    return tempList

lastNums = []

for i in newLines:
    lineChecks = [i]
    lineChecks.append(difSequence(i))
    while sum(lineChecks[-1]) != 0:
        lineChecks.append(difSequence(lineChecks[-1]))

    revIndex = -1
    appendNum = 0
    for num, j in enumerate(reversed(lineChecks)):
        try:
            lineChecks[revIndex-1].insert(0, lineChecks[revIndex-1][0] -\
                                        lineChecks[revIndex][0])
            revIndex = revIndex - 1
        
        except:
            revIndex = -1
            continue
        appendNum = lineChecks[revIndex][0]
    lastNums.append(appendNum)
print(sum(lastNums))