import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
closestPositive = float("inf")
closestNegative = float("-inf")
result = 0
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    if t == 0:
        result = t
        break
    elif t > 0 and t < closestPositive:
        closestPositive = t

    elif t < 0 and t > closestNegative:
        closestNegative = t
if math.isinf(closestPositive) and math.isinf(closestNegative):
    result = 0
elif abs(closestNegative) == abs(closestPositive):
    result = closestPositive
elif abs(closestNegative) > abs(closestPositive):
    result = closestPositive
else:
    result = closestNegative





# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

print(result)
