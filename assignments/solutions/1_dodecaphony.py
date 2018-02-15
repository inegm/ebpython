import random
import math


def transpose_row(row, semitones):
    return [semitones + tone for tone in row]

def generate_tone_row(root=0):
    row = transpose_row(range(12), root)
    random.shuffle(row)

    return row

def retrograde_tone_row(row):
    retrograde = row.copy()
    retrograde.reverse()

    return retrograde

def invert_tone_row(row):
    intervals = list()
    for index, tone in enumerate(row):
        try:
            interval = row[index + 1] - tone
            inverted = -1 * interval
            intervals.append(inverted)
        except IndexError:
            continue
    inversion = [row[0]]
    for interval in intervals:
        inversion.append(inversion[-1] + interval)

    return inversion
