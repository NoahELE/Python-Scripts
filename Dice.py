import random
import re


command = input("Dice Command: ")
pattern = "(\d*)d(\d*)"
regexMatch = re.match(pattern, command)
total = 0
if regexMatch != None:
    for i in range(int((regexMatch).group(1))):
        a = random.randint(0, int(regexMatch.group(2)))
        print(a)
        total += a
    print("------")
    print(total)
    print("END")
else:
    print("Unrecognized Input")
