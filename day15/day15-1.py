with open("data15.txt", 'r') as file:
    data = file.read().split(",")
    
asciiDict = {}

for num, i in enumerate(range(32, 127)):
    j = chr(i)
    asciiDict[j] = num + 32

spicyList = []
for item in data:
    spicyNum = 0
    for char in item:
        spicyNum += asciiDict[char]
        spicyNum = spicyNum * 17
        spicyNum = spicyNum % 256
    spicyList.append(int(spicyNum))
    
print(sum(spicyList))