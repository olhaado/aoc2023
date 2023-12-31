
with open('data3.txt', 'r') as file:
    data = file.read().splitlines()

newdata = []

#symbols to replace with x
replace_dict= {"+" : "x", "~" : "x", "`" : "x", "!" : "x", "@" : "x",\
                "#" : "x", "$" : "x", "%" : "x", "^" : "x", "&" : "x",\
                "*" : "x", "/" : "x", "?" : "x", ";" : "x", ":" : "x",\
                ">" : "x", "<" : "x", "-" : "x", "=" : "x"}

#use replace_dict to make all special characters "x" in data list   
for i in data:
    for j, k in replace_dict.items():
        i = i.replace(j, k)
    newdata.append(i)
print(newdata)

#returns the previous line, current line and next line relative to current

previous = ""
partsList = []
for num, line in enumerate(newdata):
    #newline = line.split(".") #creates a list of non "." character
    print(line)

    delimiters = [".", "x"]

    for delimiter in delimiters:
        line = " ".join(line.split(delimiter))
    newline = line.split()

    #newline = line.replace('.', ' ').replace('x', ' ').split()
    print(newline)
    for numb, i in enumerate(newline):
        if i.isdigit():
            length = len(i)
            indexStart = line.find(i) - 1
            indexEnd = indexStart + length + 2
            if indexStart < 0:
                indexStart = 0
            if indexEnd > len(line):
                indexEnd = len(line) + 1
            xinslice1 = newdata[num-1][indexStart:indexEnd].find("x")
            xinslice2 = newdata[num][indexStart:indexEnd].find("x")
            xinslice3 = ""
            try:
                xinslice3 = newdata[num+1][indexStart:indexEnd].find("x")
            except:
                xinslice3 = -1
            if xinslice1 != -1 or xinslice2 != -1 or xinslice3 != -1:
                partsList.append(int(i))
                print(f"added part {i}")
    print(f"-------end-line-{num+1}-------")
    previous = newdata[num-1]
print(partsList)
print(sum(partsList))


### testing individual aspects before integrating ###

#separates full numbers into a list, finds their length and index in line
'''line = ".664..598..."
newline = line.split(".")
for num, i in enumerate(newline):
    if i.isdigit():
        print(len(i))
        print(line.index(newline[num]))'''

#finds the index of a slice of a string relative to the number
'''line1 = "...*..*."
line2 = "467..114"
line3 = "...*.*.."

if "114" in line2:
    length = len("114")
    indexStart = line2.index("114") - 1
    indexEnd = indexStart + length + 2
    if indexStart < 0:
        indexStart = 0
    if indexEnd > len(line2):
        indexEnd = len(line2) + 1
    xinslice1 = line1[indexStart:indexEnd].find("*")
    xinslice2 = line2[indexStart:indexEnd].find("*")
    xinslice3 = line3[indexStart:indexEnd].find("*")
    if xinslice1 != -1 or xinslice2 != -1 or xinslice3 != -1:
        print('yes')'''


