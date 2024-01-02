with open("data15.txt", 'r') as file:
    data = file.read().split(",")
    
#build a dictionary to look up the number based on a given value
asciiDict = {}

for num, i in enumerate(range(32, 127)):
    j = chr(i)
    asciiDict[j] = num + 32
print(asciiDict)


spicyList = []
for item in data:
    spicyNum = 0
    for char in item:
        spicyNum += asciiDict[char]
        spicyNum = spicyNum * 17
        spicyNum = spicyNum % 256
    #print(f"{item} = {spicyNum}")
    spicyList.append(int(spicyNum))
print(sum(spicyList))