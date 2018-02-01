"""Solutions to pitch arithmetic assigned problems"""
import math
import random


# Problem 1 - Hertz to MIDI note number
f = 440
p = int(69 + 12 * math.log(f / 440 , 2))
print(p)

# Problem 2 - MIDI note number to Hertz
m = 69
p = 440 * math.pow(2, (m - 69) / 12)
print(p)

# Problem 3 - Twelve-tone rows
row = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
random.shuffle(row)
print(row)

# Problem 4 - MIDI note twelve-tone rows
root = 60
row = [root + interval for interval in range(12)]
random.shuffle(row)
print(row)
