import sys
import math
import functools

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

b = input()

array = [(index,int(bit)) for index,bit in enumerate(b)]

def findLongestSequence(array):
    def reducerFunction (accumulator, current):
        if current[1] == 1:
            accumulator['current'] += 1
        if current[1] == 0 or current[0] == len(array) - 1:
            if accumulator['longest'] < accumulator['current']:
                accumulator['longest'] = accumulator['current']
            accumulator['current'] = 0
        if current[0] == len(array) - 1:
            accumulator = accumulator['longest']
            return accumulator
        return accumulator

    longestSequence = functools.reduce(reducerFunction, array, {'longest': 0, 'current': 0})

    return longestSequence

longestSequencesArray = []
indexesOfZeroesArray = []

for index, bit in array:
    if bit == 0 and index not in indexesOfZeroesArray:
        indexesOfZeroesArray.append(index)
        savedElement = array[index]
        array[index] = (index, 1)
        longestSequence = findLongestSequence(array)
        longestSequencesArray.append(longestSequence)
        array[index] = savedElement

print(max(longestSequencesArray))
