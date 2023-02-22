import random 
names = []

string = list(input("Word: "))
variations = 0

def factor(n):
    bruh = 1
    for i in map(abs, list(range(-n, 0))): bruh *= i # what?
    return bruh    

start_factor_counter = factor(len(string))
start_divisor_counter = 1

repeats = { letter: string.count(letter) for letter in string if string.count(letter) > 1 } # dictionary comprehension
for i in repeats.values(): start_divisor_counter *= factor(i)

variations = start_factor_counter / start_divisor_counter 

while True:
    if not len(names) == variations:
        random.shuffle(string)
        if string not in names:
            names.append(''.join(string))
    else:
        print('>', ', '.join(sorted(names)))
        print('>', len(names), '/', variations)
        break 
