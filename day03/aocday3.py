#----------------------AoC Day 3----------------------
import re

with open("test.txt") as file:
    data = file.read().split('\n')#split data at new lines and create list
    new_data = []
    replace_dict= {"~" : "x", "`" : "x", "!" : "x", "@" : "x", "#" : "x", "$" : "x", "%" : "x", "^" : "x", "&" : "x", "*" : "x",\
                   "/" : "x", "?" : "x", ";" : "x", ":" : "x", ">" : "x", "<" : "x"} #symbols to replace with x to use isalpha()
    
    for i in data:
        for j, k in replace_dict.items():
            i = i.replace(j, k)
        new_data.append(i) #replaced all symbols with 'x' from replace_dict

adjacent_numbers = []

for i in range(len(new_data)):
    for j in range(len(new_data[i])):
        if new_data[i][j] == 'x':
            #left of x
            if j - 1 >= 0 and new_data[i][j - 1].isdigit():
                adjacent_numbers.append(int(new_data[i][j - 1]))

            #right of x
            if j + 1 < len(new_data[i]) and new_data[i][j + 1].isdigit():
                adjacent_numbers.append(int(new_data[i][j + 1]))

            #above x
            if i - 1 >= 0 and new_data[i - 1][j].isdigit():
                adjacent_numbers.append(int(new_data[i - 1][j]))

            #below x
            if i + 1 < len(new_data) and new_data[i + 1][j].isdigit():
                adjacent_numbers.append(int(new_data[i + 1][j]))

            #above left x
            if i - 1 >= 0 and j - 1 >= 0 and new_data[i - 1][j - 1].isdigit():
                adjacent_numbers.append(int(new_data[i - 1][j - 1]))

            #above right x
            if i - 1 >= 0 and j + 1 >= 0 and new_data[i - 1][j + 1].isdigit():
                adjacent_numbers.append(int(new_data[i - 1][j + 1]))

            #below left x
            if i + 1 >= 0 and j - 1 >= 0 and new_data[i + 1][j-1].isdigit():
                adjacent_numbers.append(int(new_data[i + 1][j-1]))

            #below right x
            if i + 1 >= 0 and j + 1 >= 0 and new_data[i + 1][j + 1].isdigit():
                adjacent_numbers.append(int(new_data[i + 1][j + 1]))

print(adjacent_numbers)