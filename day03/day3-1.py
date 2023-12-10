with open('test.txt', 'r') as file:
    data = file.read().splitlines()
print(data)

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

print()