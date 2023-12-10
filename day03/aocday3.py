#----------------------AoC Day 3----------------------
import numpy as np

with open("test.txt") as file:
    data = file.read().split('\n')#split data at new lines and create list
    new_data = []
    replace_dict= {"~" : "x", "`" : "x", "!" : "x", "@" : "x", "#" : "x", "$" : "x", "%" : "x", "^" : "x", "&" : "x", "*" : "x",\
                   "/" : "x", "?" : "x", ";" : "x", ":" : "x", ">" : "x", "<" : "x"} #symbols to replace with x to use isalpha()
    
    for i in data:
        for j, k in replace_dict.items():
            i = i.replace(j, k)
        new_data.append(i) #replaced all symbols with 'x' from replace_dict

#print(new_data)

'''for each line in the list:
for each item in the line:
if item in the line is a number:
and if item in the line +/- 1 is an alpha:
then append number to number_list'''

data_length = len(new_data) #length of list
number_list = []
index_counter = 0 #counter for each line

#while i < data_length

for i in new_data:
    char_counter = 0 #counter for each character in each line
    index_counter = 0 #counter for index of line
    for j in i:
        if j.isnumeric():
            if char_counter + 1 < len(i) and i[char_counter + 1].isalpha(): # if char comes after number, but within line i
                number_list.append(j)
            elif char_counter - 1 >= 0 and i[char_counter - 1].isalpha(): # if char comes before number, but within line i
                number_list.append(j)
        char_counter += 1


print(number_list)




