import sys
import math
import functools


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r = int(input())
v = int(input())
vaultsArrayOfTuples = []
for i in range(v):
    c, n = [int(j) for j in input().split()]
    vaultsArrayOfTuples.append((c, n, i))

def countCombinations(accumulator, numTuple):
    c, n, i = numTuple
    combinationsForNumbers = 10 ** n
    combinationsForVowels = 5 ** (c-n)
    totalNumberOfCombinations = combinationsForNumbers * combinationsForVowels * ( v // r + v % r)
    # accumulator += totalNumberOfCombinations
    if i % r == 0:
        accumulator.append([totalNumberOfCombinations])
    else:
        accumulator[i // r].append(totalNumberOfCombinations)
    return accumulator

def countCombinationsMap(accumulator, numTuple):
    c, n, i = numTuple
    combinationsForNumbers = 10 ** n
    combinationsForVowels = 5 ** (c-n)
    totalNumberOfCombinations = combinationsForNumbers * combinationsForVowels * ( v // r + v % r)
    return totalNumberOfCombinations


# mappedArray = list(map(countCombinationsMap,vaultsArrayOfTuples))
reducedArray = functools.reduce(countCombinations, vaultsArrayOfTuples, [])
result = functools.reduce(lambda accum, current: accum + max(current), reducedArray, 0)

# print(mappedArray)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)
print(reducedArray)
print(result)
