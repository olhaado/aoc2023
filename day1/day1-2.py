with open ('data1.txt', 'r') as file:
    data = file.read().splitlines()

    print(data)

words_to_numbers = {
    'one': 'on1ne',
    'two': 'tw2wo',
    'three': 'th3ree',
    'four': 'fo4ur',
    'five': 'fi5ve',
    'six': 'si6ix',
    'seven': 'se7en',
    'eight': 'ei8ht',
    'nine': 'ni9ne',
}

calues = []

for i in data:
    #two methods of replacing that also worked
    """i = i.replace('one', 'on1ne').replace('two', 'tw2wo').replace('three', 'th3ree')\
     .replace('four', 'fo4ur').replace('five', 'fi5ve').replace('six', 'si6ix')\
     .replace('seven', 'sev7ven').replace('eight', ei8ht').replace('nine', 'ni9ne')"""

    """for char in words_to_numbers.keys():
        i = i.replace(char, words_to_numbers[char])"""
    
    for key, value in words_to_numbers.items():
        i = i.replace(key, value)
    print(i)
    numsInString = []
    stringCals = ""
    for j in i:
        if j.isdigit():
            numsInString.append(j)
    print(numsInString)
    stringCals = numsInString[0] + numsInString[-1]
    calues.append(int(stringCals))

print(sum(calues))