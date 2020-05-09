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

# function to count combinations
def countCombinations(numTuple):
    c, n, ind = numTuple
    combinationsForNumbers = 10 ** n
    combinationsForVowels = 5 ** (c-n)
    totalNumberOfCombinations = combinationsForNumbers * combinationsForVowels
    return (totalNumberOfCombinations, ind)

combinationsArray = list(map(countCombinations, vaultsArrayOfTuples))

# array of first r combinations
initialArray = [combinationsArray[i] for i in range(r)]

def reduceFinal(accumulator, currentValue):
    combinations, ind = currentValue
    if ind < r:
        return accumulator
    minValueInAccumulator = min(accumulator, key = lambda x: x[0])
    accumulator[minValueInAccumulator[1]] = (minValueInAccumulator[0] + currentValue[0], minValueInAccumulator[1])
    return accumulator

finalResult = functools.reduce(reduceFinal, combinationsArray, initialArray)

print(max(finalResult, key = lambda x: x[0])[0])
