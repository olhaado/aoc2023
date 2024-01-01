with open('data9.txt', 'r') as file:
    data = file.read().splitlines()

lines = [i.split(' ') for i in data]
newLines = []
for x in lines:
    tempList = []
    for y in x:
        tempList.append(int(y))
    newLines.append(tempList)

#print(newLines)

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
    #print(lineChecks)

    revIndex = -1
    appendNum = 0
    for num, j in enumerate(reversed(lineChecks)):
        #print(f"the list is {j} and the last number is {j[-1]}")
        #print(f"revIndex = {revIndex}")
        try:
            lineChecks[revIndex-1].insert(0, lineChecks[revIndex-1][0]-lineChecks[revIndex][0])
            #print(lineChecks[revIndex])
            revIndex = revIndex - 1
        except:
            revIndex = -1
            #print(f"reset revIndex")
            continue
        appendNum = lineChecks[revIndex][0]
    #print(f"appending {appendNum}")
    lastNums.append(appendNum)
#print(lastNums)
print(sum(lastNums))

##### plan
# Create a list of lists for each line.
# While the sum of each line != 0, run the function again and append
# Add last index of last list to add to last index of previous list etc.
# Add the last index of each line to a list and sum 