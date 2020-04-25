import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()
# function to convert binary string to 7-bit string
def formatToSevenBits(binary):
    string = str(binary)
    while len(string) != 7:
        string = '0' + string
    return string

# format each char as a 7-bit binary string and join them in a string
binaryString = ''.join(formatToSevenBits(format(ord(char), 'b')) for char in message)

# read first digit
previousChar = binaryString[0]
if (previousChar == '0'):
    result = '00 0'
else:
    result = '0 0'

# iterate over all other digits (except the first one)
for index, digit in enumerate([i for i in binaryString]):
    if index != 0:
        if digit == previousChar:
            result += '0'
        elif digit == '0' and previousChar == '1':
            result += ' 00 0'
        elif digit == '1' and previousChar == '0':
            result += ' 0 0'
        previousChar = digit

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

print(result)
