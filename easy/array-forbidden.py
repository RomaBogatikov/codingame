import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
n = int(input())

# /////////////////////////////////
# ///////MY SOLUTION///////////////
# /////////////////////////////////

# mergeSections()
def mergeSections(previousSection, currentSection):
    # if st of a currentSection is within previousSection
    if currentSection[0] <= previousSection[1]:
        # if ed of currentSection is less than ed of previousSection
        if currentSection[1] <= previousSection[1]:
            # currentSection is within previousSection
            return [(previousSection[0], previousSection[1])]
        # if ed of currentSection is greater than ed of previousSection
        elif currentSection[1] > previousSection[1]:
            # take st from previousSection, and ed from currentSection
            return [(previousSection[0], currentSection[1])]
    # otherwrise, arrays do not intersect
    else:
        return [previousSection, currentSection]

# read input and append to inputList array
inputList = []
for i in range(n):
    st, ed = [int(j) for j in input().split()]
    inputList.append((st, ed))

# sort inputList array of tuples by first element in tuple (st)
sortedInputList = sorted(inputList, key = lambda key: key[0])

# declare finalResult array
finalResult = [sortedInputList[0]]
for index in range(len(sortedInputList)):
    if index != 0:
        mergeResult = mergeSections(finalResult[-1], sortedInputList[index])
        finalResult.pop()
        finalResult.extend(mergeResult)

# print final result
# see if start and end values will change (assume the fence is fully painted)
start = 0
end = l

# if first element in a first section is greater than 0
if finalResult[0][0] > 0:
    # the unpainted section is from 0 to st of a first section
    print(0, finalResult[0][0])
    # change start
    start = finalResult[0][0]

# print the rest of unpainted sections
for index in range(len(finalResult)):
    # if it is not the last section in finalResult array
    if index != len(finalResult) - 1:
        print(finalResult[index][1], finalResult[index+1][0])
    # if it is the last section and ed in the last section is less than l
    elif index == len(finalResult) - 1 and finalResult[index][1] < l:
        print(finalResult[index][1], l)
        # change end
        end = finalResult[index][1]

# check if all sections are painted
if len(finalResult) == 1 and start == 0 and end == l:
    print('All painted')


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)


# /////////////////////////////////
# ///////BEST SOLUTION/////////////
# /////////////////////////////////

painted = sorted([[int(j) for j in input().split()] for _ in range(n)], key=lambda x: x[0])
print(painted)
outp = []
ce = 0
for s, e in painted + [[l, l]]:
    print(s, e)
    if s > ce:
        outp.append(f"{ce} {s}")
        ce = e
    else:
        ce = max(ce, e)
if len(outp) == 0:
    outp = ["All painted"]
print(*outp, sep="\n")
