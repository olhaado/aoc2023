with open ('map.txt') as file: #opens map data as file
    map = file.read().split() #split data at newlines

#library listing all possible movements based on pipe style
movements = {'|' : ['N', 'S'], '-' : ['E', 'W'], 'L' : ['N', 'E'], 'J' : ['N', 'W'], '7' : ['S' , 'W'], 'F' : ['S', 'E']}

#function finds the location of S (animal) within the map
def find_animal(map):
    for i, sublist in enumerate(map):
        for j, item in enumerate(sublist):
            if item == 'S':
                start_line = i
                start_num = j
                return start_line, start_num #returns the index coordinates

s_start = find_animal(map) #defines the animal's coordinates as a variable
search_line, search_char = s_start #splits tuple from s_start into two variables

#define what each direction means, not sure if I need this yet
North = map[search_line - 1][search_char]
South = map[search_line + 1][search_char]
West = map[search_line][search_char - 1]
East = map[search_line][search_char + 1]
char_find = map[search_line][search_char]

#using e as an example, e is known to exist
def east_track(map, search_line, search_char):
    going_east = map[search_line][search_char +1]
    return(going_east)

eastward = east_track(map, search_line, search_char) #starts path after finding the animal (s)
#print(eastward), gives the correct response

def start_path(search_line, search_char, map):
    east = map[search_line][search_char + 1]
    stop_character = '.'
    counter = 0
    current_line = search_line #2
    current_char = search_char #0
    while east in movements:
        if east != stop_character:
            counter += 1
            if east == 'L':
                if current_line > 0 and current_char > 0:
                    current_line 
                    #east = east[current_line - 1][current_char - 1]
                else:
                    print("not possible")
            elif east == '-':
                print() # replace
                #east = east[current_char + 1]
            elif east == 'J':
                if current_line > 0 and current_char < 5:
                    print(current_line, current_char)
                    current_line = current_line - 1
                    current_char = current_char + 1
                    print(current_line, current_char)
                    #east = east[current_line - 1][current_char + 1]
                else:
                    print("not possible")
            elif east == '7':
                if current_char < 5 and current_line < 5:
                    print() # replace
                    #east = east[current_line + 1][current_char + 1]
                else:
                    print("not possible")
            elif east == '|':
                if current_line > 0:
                    print() # replace
                    #east = east[current_line - 1]
                else:
                    print("not possible")
            else:
                if current_char > 0:
                    east = east[current_char - 1]
                else:
                    print("not possible")
            east = map[current_line][current_char + 1]

    print(counter)

start_path(search_line, search_char, map)