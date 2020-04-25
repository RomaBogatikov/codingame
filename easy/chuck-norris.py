import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()
# print(format(ord(message), 'b'))
binary = ''.join(format(ord(char), 'b') for char in message)
binaryString = str(binary)
output = ''
# print(binaryString)
previousChar = binaryString[0]
if (previousChar == '0'):
    result = '00 0'
else:
    result = '0 0'

for index, digit in enumerate([i for i in str(binary)]):
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
