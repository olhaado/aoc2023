with open ('data2.txt', 'r') as file:
    data = file.read().splitlines()


redCubes = 12
greenCubes = 13
blueCubes = 14

gameSum = 0

for num, i in enumerate(data): #iterates on each game
    gameCheck = True
    i = i.split(':')
    idata = i[1].split(';')
    print(num+1)
    print(idata)

    for j in idata: #iterates on each round
        j = j.split(',')
        roundCheck = True

        for k in j: #iterates on each color in round
            if 'red' in k:
                k = k.strip().split(' ')
                if int(k[0]) > redCubes:
                    roundCheck = False
            elif 'blue' in k:
                k = k.strip().split(' ')
                if int(k[0]) > blueCubes:
                    roundCheck = False
            elif 'green' in k:
                k = k.strip().split(' ')
                if int(k[0]) > greenCubes:
                    roundCheck = False
        if roundCheck == False:
            gameCheck = False
    print(f"game was {gameCheck}")
    if gameCheck == True:
        gameSum += num + 1
    print(f"current total is {gameSum}")
print(gameSum)

