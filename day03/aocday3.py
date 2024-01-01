'''#----------------------AoC Day 3----------------------
with open("test.txt") as file:
    data = file.read().split('\n')#split data at new lines and create list
    new_data = []
    #symbols to replace with x for ease of use
    replace_dict= {"~" : "x", "`" : "x", "!" : "x", "@" : "x", "#" : "x", "$" : "x", "%" : "x", "^" : "x", "&" : "x", "*" : "x",\
                   "/" : "x", "?" : "x", ";" : "x", ":" : "x", ">" : "x", "<" : "x", "+" : "x", "=" : "x", "-" : "x", "_" : "x"}
   
    for i in data:
        for j, k in replace_dict.items():
            i = i.replace(j, k)
        new_data.append(i) #replaced all symbols with 'x' from replace_dict

#new list to append found numbers to
adjacent_numbers = []

for i in range(len(new_data)):
    print(f"Checking line {i}")
    for j in range(len(new_data[i])):
        whole_num = ''
        if new_data[i][j] == 'x':
            a, b = i, j
            #left of x
            while b - 1 >= 0 and new_data[a][b - 1].isdigit():
                whole_num = new_data[a][b - 1] + whole_num
                print(f"{whole_num} found left")
                b -= 1
            if whole_num:
                adjacent_numbers.append(int(whole_num))
                print(f"{int(whole_num)} added")
                whole_num = ''
        #if new_data[i][j] == 'x':        
            #right of x
            b = j
            while b + 1 < len(new_data[a]) and new_data[a][b + 1].isdigit():
                whole_num = new_data[a][b + 1] + whole_num
                print(f"{whole_num} found right")
                b += 1
            if whole_num:
                adjacent_numbers.append(int(whole_num))
                print(f"{int(whole_num)} added")
                whole_num = ''
            #above x HELP ME
            a = i
            while a - 1 >= 0 and new_data[a - 1][b].isdigit():
                whole_num = new_data[a - 1][b] + whole_num
                print(f"{whole_num} found above")
                a -= 1
            if whole_num:
                adjacent_numbers.append(int(whole_num))
                print(f"{int(whole_num)} added")
                whole_num = ''
            #below x HELP ME
            a = i
            while a + 1 < len(new_data) and new_data[a + 1][b].isdigit():
                whole_num = new_data[a + 1][b] + whole_num
                print(f"{whole_num} found below")
                a += 1
            if whole_num:
                adjacent_numbers.append(int(whole_num))
                print(f"{int(whole_num)} added")
                whole_num = ''
            #above left x
            a, b = i, j
            while a - 1 >= 0 and b - 1 >= 0 and new_data[a - 1][b - 1].isdigit():
                whole_num = new_data[a - 1][b - 1] + whole_num
                print(f"{whole_num} found above left")
                a -= 1
                b -= 1
            if whole_num:
                adjacent_numbers.append(int(whole_num))
                print(f"{int(whole_num)} added")
                whole_num = ''
            #above right x
            a, b = i, j
            while a - 1 >= 0 and b + 1 < len(new_data[i]) and new_data[a - 1][b + 1].isdigit():
                whole_num = new_data[a - 1][b + 1] + whole_num
                print(f"{whole_num} found above right")
                a -= 1
                b += 1
            if whole_num:
                adjacent_numbers.append(int(whole_num))
                print(f"{int(whole_num)} added")
                whole_num = ''
        #below left x
            a, b = i, j
            while a + 1 < len(new_data) and b - 1 >= 0 and new_data[a + 1][b - 1].isdigit():
                whole_num = new_data[a + 1][b - 1] + whole_num
                print(f"{whole_num} found below left")
                a += 1
                b -= 1
            if whole_num:
                adjacent_numbers.append(int(whole_num))
                print(f"{int(whole_num)} added")
                whole_num = ''
            #below right x
            a, b = i, j
            while a + 1  < len(new_data) and b + 1 < len(new_data[i]) and new_data[a + 1][b + 1].isdigit():
                whole_num = new_data[a + 1][b + 1] + whole_num
                print(f"{whole_num} found below right")
                a += 1
                b += 1
            if whole_num:
                adjacent_numbers.append(int(whole_num))
                print(f"{int(whole_num)} added")
                whole_num = ''
print(adjacent_numbers)'''

whole_num = ''
new_num = '2'

whole_num = new_num
new_num = '9'
whole_num = new_num + whole_num
new_num = '5'
whole_num = new_num + whole_num
print(whole_num)