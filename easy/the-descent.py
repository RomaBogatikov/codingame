import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    arrayOfMountains = []
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        arrayOfMountains.append(mountain_h)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    # print("Debug...", file=sys.stderr)
    # The index of the mountain to fire on.
    # print(arrayOfMountains)
    maxNumber = 0
    index = None
    for i, value in enumerate(arrayOfMountains):
        if value > maxNumber:
            maxNumber = value
            index = i

    print(index)
