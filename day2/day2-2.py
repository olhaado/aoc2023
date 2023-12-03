with open ('data2.txt', 'r') as file:
    data = file.read().splitlines()

cubePower = 0

for num, i in enumerate(data): #iterates on each game
    gameCheck = True
    redCubes = 0
    greenCubes = 0
    blueCubes = 0
    i = i.split(':')
    idata = i[1].split(';')
    print(f"Game {num+1}")
    print(idata)

    for j in idata: #iterates on each round
        j = j.split(',')
        roundCheck = True

        for k in j: #iterates on each color in round
            if 'red' in k:
                k = k.strip().split(' ')
                if int(k[0]) > redCubes:
                    redCubes = int(k[0])
            elif 'blue' in k:
                k = k.strip().split(' ')
                if int(k[0]) > blueCubes:
                    blueCubes = int(k[0])
            elif 'green' in k:
                k = k.strip().split(' ')
                if int(k[0]) > greenCubes:
                    greenCubes = int(k[0])
    print(f"{redCubes} red cubes required")
    print(f"{blueCubes} blue cubes required")
    print(f"{greenCubes} green cubes required")

    cubePower += (redCubes * blueCubes * greenCubes)
    print(f"cube power is currently {cubePower}")
