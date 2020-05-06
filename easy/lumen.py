import sys
import math
import functools

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
l = int(input())
matrix = []
for i in range(n):
    line = input()
    lineArray = line.split(' ')
    matrix.append(lineArray)


for index_row, row in enumerate(matrix):
    for index_column, spot in enumerate(row):
        if spot == 'C':

            for level in range(1, l+1):
                # print('level=', level)
                # upper row
                if index_row - level >= 0:
                    for column in range(index_column - level, index_column + level + 1):
                        if column >= 0 and column <= n-1:
                            if isinstance(matrix[index_row - level][column], int):
                                matrix[index_row - level][column] = max(l-level, matrix[index_row - level][column])
                            elif matrix[index_row - level][column] != 'C':
                                matrix[index_row - level][column] = l - level

                # bottom row
                if index_row + level <= n-1:
                    for column in range(index_column - level, index_column + level + 1):
                        # print('bottom row', index_row + level, column)
                        if column >= 0 and column <= n-1:
                            if isinstance(matrix[index_row + level][column], int):
                                matrix[index_row + level][column] = max(l-level, matrix[index_row + level][column])
                            elif matrix[index_row + level][column] != 'C':
                                matrix[index_row + level][column] = l - level

                # left column
                if index_column - level >= 0:
                    for row in range(index_row - level, index_row + level + 1):
                        if row >= 0 and row <= n-1:
                            if isinstance(matrix[row][index_column - level], int):
                                matrix[row][index_column - level] = max(l-level, matrix[row][index_column - level])
                            elif matrix[row][index_column - level] != 'C':
                                matrix[row][index_column - level] = l - level

                # right column
                if index_column + level <= n-1:
                    for row in range(index_row - level, index_row + level + 1):
                        if row >= 0 and row <= n-1:
                            if isinstance(matrix[row][index_column + level], int):
                                matrix[row][index_column + level] = max(l - level, matrix[row][index_column + level])
                            elif matrix[row][index_column + level] != 'C':
                                matrix[row][index_column + level] = l - level

flattenedMatrix = [element for sublist in matrix for element in sublist]

def reducerFunction(accumulator, currentElement):
    if currentElement == 0 or currentElement == 'X':
        accumulator += 1
    return accumulator

result = functools.reduce(reducerFunction, flattenedMatrix, 0)


# for row in matrix:
#     print(row)

print(result)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

# print(flattenedMatrix)
