import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
n = int(input())
result = []
for i in range(l):
    result.append(False)

for i in range(n):
    st, ed = [int(j) for j in input().split()]
    for i in range(st, ed):
        result[i] = True

# print(result)

if False in result:
    start = 0
    for index, section in enumerate(result):
        if index == 0:
            prevSection = section
            if section == False:
                start = 0
        if index != 0:
            if section == False and prevSection == False:
                continue
            if section == False and prevSection == True:
                start = index
            if (section == True and prevSection == False) or (index == len(result) - 1 and start <= index):
                print(start, index)
            prevSection = section
else:
    print('All painted')
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)
