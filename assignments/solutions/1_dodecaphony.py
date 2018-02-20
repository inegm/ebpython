import random
import math


def transpose_row(row, semitones):
    """Transpose a tone row

    :param row: a tone row
    :row: list of midi note ints
    :param semitones: number of semitones by which to transpose
    :type semitones: int

    :returns: the transposed tone row
    :rtype: list of midi note ints
    """
    return [semitones + tone for tone in row]

def generate_tone_row(root=0):
    """Generate a random tone row

    :param root: a midi note root value for the tone row
    :type root: int

    :returns: a random tone row
    :rtype: list of midi note ints
    """
    row = transpose_row(range(12), root)
    random.shuffle(row)

    return row

def retrograde_tone_row(row):
    """Retrograde a tone row

    :param row: a tone row
    :row: list of midi note ints

    :returns: the retrograde tone row
    :rtype: list of midi note ints
    """
    retrograde = row.copy()
    retrograde.reverse()

    return retrograde

def invert_tone_row(row):
    """Invert a tone row

    :param row: a tone row
    :row: list of midi note ints

    :returns: the inverted tone row
    :rtype: list of midi note ints
    """
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
