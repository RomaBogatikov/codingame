import sys
import math
from functools import reduce

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
inputArray = []
for i in range(n):
    pi = int(input())
    inputArray.append(pi)

sortedArray = sorted(inputArray)

sortedArrayWithIndex = [{'horses': int(horses), 'index': int(index)} for index, horses  in enumerate(sortedArray)]

# define a reducer function
def reducerFunc(accumulator, currentValue):
    # if it is the last element in array, return accumulator
    if currentValue['index'] == sortedArrayWithIndex[-1]['index']:
        return accumulator
    # define delta between horses' strengths
    deltaHorsesStrength = sortedArrayWithIndex[currentValue['index'] + 1]['horses'] - currentValue['horses']
    # if it is the first element in array, return delta
    if currentValue['index'] == 0:
        accumulator = deltaHorsesStrength
    # otherwise, compare current delta with accumulator
    if currentValue['index'] != 0:
            if deltaHorsesStrength < accumulator:
                accumulator = deltaHorsesStrength
    return accumulator

result = reduce(reducerFunc, sortedArrayWithIndex, 0)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

print(result)
