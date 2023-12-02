with open ('data1.txt', 'r') as file:
    data = file.read().splitlines()

    print(data)

calues = []

for i in data:
    numsInString = []
    stringCals = ""
    for j in i:
        if j.isdigit():
            numsInString.append(j)
    print(numsInString)
    stringCals = numsInString[0] + numsInString[-1]
    calues.append(int(stringCals))

print(sum(calues))