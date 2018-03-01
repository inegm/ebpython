import mido
import twelvetone as tt


PPQN = 96

def main():
    row = tt.Row(root=60)

    fullrow = mido.MidiFile(ticks_per_beat=PPQN)

    prime = mido.MidiTrack()
    prime.name = 'Prime'
    fullrow.tracks.append(prime)
    for note in row.P:
        prime.append(mido.Message('note_on', note=note))
        prime.append(mido.Message('note_off', note=note, time=PPQN))

    inversion = mido.MidiTrack()
    inversion.name = 'Inversion'
    fullrow.tracks.append(inversion)
    for note in row.I:
        inversion.append(mido.Message('note_on', note=note))
        inversion.append(mido.Message('note_off', note=note, time=PPQN))

    retrograde = mido.MidiTrack()
    retrograde.name = 'Retrograde'
    fullrow.tracks.append(retrograde)
    for note in row.R:
        retrograde.append(mido.Message('note_on', note=note))
        retrograde.append(mido.Message('note_off', note=note, time=PPQN))

    retroinv = mido.MidiTrack()
    retroinv.name = 'RetroInversion'
    fullrow.tracks.append(retroinv)
    for note in row.RI:
        retroinv.append(mido.Message('note_on', note=note))
        retroinv.append(mido.Message('note_off', note=note, time=PPQN))

    fullrow.save('/Users/daedalus/code/ebpython/pycompose/midi/ttfullrow.mid')

    tetrarow = mido.MidiFile(ticks_per_beat=PPQN)

    prime = mido.MidiTrack()
    prime.name = 'Prime'
    tetrarow.tracks.append(prime)
    for i in range(4):
        for chord in row.P_tetrachords:
            prime.append(mido.Message('note_on', note=chord[i]))
        for chord in row.P_tetrachords:
            prime.append(mido.Message('note_off', note=chord[i], time=PPQN))

    tetrarow.save('/Users/daedalus/code/ebpython/pycompose/midi/tttetra.mid')

if __name__ == '__main__':
    main()
