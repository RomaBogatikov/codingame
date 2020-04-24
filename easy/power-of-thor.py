import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    move = None
    # in the first quadrant

    # use for _ in range(1) to
    # (1) Better communicate intention of a single iteration loop and
    # (2) no last break statement to exit the loop (might be removed by accident later on)
    # https://stackoverflow.com/questions/2069662/how-to-exit-an-if-clause
    # while True:
    for _ in range(1):
        if initial_tx > light_x and initial_ty < light_y:
            move = "SW"
            initial_tx -= 1
            initial_ty += 1
            break
        # in the second quadrant
        if initial_tx < light_x and initial_ty < light_y:
            move = "SE"
            initial_tx += 1
            initial_ty += 1
            break
        # in the third quadrant
        if initial_tx < light_x and initial_ty > light_y:
            move = "NE"
            initial_tx += 1
            initial_ty -=1
            break
        # in the fourth quadrant
        if initial_tx > light_x and initial_ty > light_y:
            move = "NW"
            initial_tx -= 1
            initial_ty -= 1
            break
        # on the positive x-axis
        if initial_tx > light_x and initial_ty == light_y:
            move = "W"
            initial_tx -= 1
            break
        # on the positive y-axis
        if initial_tx == light_x and initial_ty < light_y:
            move = "S"
            initial_ty += 1
            break
        # on the negative x-axis
        if initial_tx < light_x and initial_ty == light_y:
            move = "E"
            initial_tx += 1
            break
        # on the negative y-axis
        if initial_tx == light_x and initial_ty > light_y:
            move = "N"
            initial_ty -= 1
            break
        # break

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(move)
