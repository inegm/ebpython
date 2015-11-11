import csv
from collections import namedtuple
import time
import subprocess


Bar = namedtuple('Bar', ['tempo', 'numerator', 'denominator', 'upbeat'])


def csv_to_playlist(path, d_tempo=120, d_num=4, d_den=4, d_upbeat=3):
    '''
    Parses a CSV rhythm file into a list of rhythm bars.

    Parameters
    ----------
    path: str, path to the rhythm csv file with headers 'tempo', 'numerator',
        'denominator', 'upbeat', and 'repeat'.

    Returns
    -------
    playlist: list of Bar namedtuples with fields 'tempo', 'numerator',
        'denominator', and 'upbeat'.
    '''
    playlist = list()
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            for repeat in range(int(row.get('repeat', 1))):
                bar = Bar(
                    tempo=int(row.get('tempo', d_tempo)),
                    numerator=int(row.get('numerator', d_num)),
                    denominator=int(row.get('denominator', d_den)),
                    upbeat=int(row.get('upbeat', d_upbeat))
                )
                playlist.append(bar)
    return playlist


def play(playlist, samples):
    '''
    Plays a rhythm playlist.

    Parameters
    ----------
    playlist: list of Bar namedtuples with fields 'tempo', 'numerator',
        'denominator', and 'upbeat'.
    samples: dictionary, Filepaths for audio samples in dictionary with keys
        and values:
            'downbeat': full filepath,
            'beat': full filepath,
            'upbeat': full filepath

    Returns
    -------
    none
    '''
    for bar in playlist:
        # Calculate quarter note duration in milliseconds
        quarter_ms = 1000.0 * 60.0 / bar.tempo
        # Calculate the note duration of one beat in this bar's context
        relative_ms = quarter_ms / (bar.denominator / 4)
        # Play the bar
        print bar
        print '1 - play downbeat'
        subprocess.call(["afplay", samples.get('downbeat')])
        time.sleep(relative_ms / 1000.0)
        for beat in range(2, bar.numerator + 1):
            if beat != bar.upbeat:
                print '{} - play beat'.format(beat)
                subprocess.call(["afplay", samples.get('beat')])
            else:
                print '{} - play upbeat'.format(beat)
                subprocess.call(["afplay", samples.get('upbeat')])
            time.sleep(relative_ms / 1000.0)


if __name__ == '__main__':
    path = 'opus_testatio.csv'
    samples = {
        'downbeat': '/Users/daedalus/Dropbox/Code/ebpython/metronome/tic.wav',
        'beat': '/Users/daedalus/Dropbox/Code/ebpython/metronome/toc.wav',
        'upbeat': '/Users/daedalus/Dropbox/Code/ebpython/metronome/tac.wav'
    }
    playlist = csv_to_playlist(path)
    play(playlist, samples)
