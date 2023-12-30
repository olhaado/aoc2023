
'''with open('test.txt', 'r') as file:
    data = file.read().splitlines()
print(data)

#returns the previous line, current line and next line relative to current

previous = ""

for num, i in enumerate(data):
    print(f"last line: {previous}")
    print(f"current line: {i}")
    try:
        print(f"next line: {data[num+1]}")
    except:
        print("no next line")
    print("--------")
    previous = i

print("done")

print()'''


#separates full numbers into a list, finds their length and index in line
'''line = ".664..598..."
newline = line.split(".")
for num, i in enumerate(newline):
    if i.isdigit():
        print(len(i))
        print(line.index(newline[num]))'''

