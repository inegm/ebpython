import random


class Row():
    def __init__(self, root=0, prime=None):
        """Initialize a Twelve-Tone Row.

        :param root: The row's first note
        :type root: int, a valid MIDI note number in the range of 0 to 115.
            115 is the upper limit for a root if the octave is to be a valid
            MIDI note (127).
        :param prime: A Twelve-Tone Row. If a prime row is not provided, a
            random row will be generated.
        :type prime: list
        """
        if type(root) != int:
            raise ValueError(
                'Root must be an integer MIDI note number. ' +
                'Got: {}'.format(root))
        if (root < 0) or (root > 115):
            raise ValueError(
                'Root must be a valid MIDI note in the range of 0 to 115. ' +
                'Got: {}'.format(root))

        self._transposition = 0

        if prime is not None:
            self._prime = prime
        else:
            self._generate_prime(root)

        self._apply_transformations()

    def _generate_prime(self, root):
        """Generate a random prime form row."""
        self._prime = [tone + root for tone in list(range(12))]
        random.shuffle(self._prime)

    def _apply_inversion(self):
        """Inversion transformation form."""
        intervals = list()
        for index, tone in enumerate(self._prime):
            try:
                interval = self._prime[index + 1] - tone
                inverted = -1 * interval
                intervals.append(inverted)
            except IndexError:
                continue
        inversion = [self._prime[0]]
        for interval in intervals:
            inversion.append(inversion[-1] + interval)

        return inversion

    def _apply_retrograde(self, row):
        """Retrograde transformation form."""
        retrograde = row.copy()
        retrograde.reverse()

        return retrograde

    def _apply_retrograde_inversion(self):
        """Retrograde-inversion transformation form."""
        inversion = self._apply_inversion()

        return self._apply_retrograde(inversion)

    def _apply_transformations(self):
        """Apply all transformations."""
        self._inversion = self._apply_inversion()
        self._retrograde = self._apply_retrograde(self._prime)
        self._retrograde_inversion = self._apply_retrograde_inversion()

    def transpose(self, transposition=0):
        """Apply transposition to all forms."""
        if type(transposition) != int:
            raise ValueError(
                'Transposition must be an integer. ' +
                'Got: {}'.format(transposition))
        if (transposition < 0) or (transposition > 11):
            raise ValueError(
                'Transposition must be in the range of 0 to 11. ' +
                'Got: {}'.format(transposition))

        self._transposition = transposition

    @property
    def P(self):
        return [
            tone + self._transposition
            for tone in self._prime]

    @property
    def P_hexachords(self):
        return [self.P[:6], self.P[6:]]

    @property
    def P_tetrachords(self):
        return [self.P[:4], self.P[4:8], self.P[8:]]

    @property
    def P_trichords(self):
        return [self.P[:3], self.P[3:6], self.P[6:9], self.P[9:]]

    @property
    def I(self):
        return [
            tone + self._transposition
            for tone in self._inversion]

    @property
    def I_hexachords(self):
        return [self.I[:6], self.I[6:]]

    @property
    def I_tetrachords(self):
        return [self.I[:4], self.I[4:8], self.I[8:]]

    @property
    def I_trichords(self):
        return [self.I[:3], self.I[3:6], self.I[6:9], self.I[9:]]

    @property
    def R(self):
        return [
            tone + self._transposition
            for tone in self._retrograde]

    @property
    def R_hexachords(self):
        return [self.R[:6], self.R[6:]]

    @property
    def R_tetrachords(self):
        return [self.R[:4], self.R[4:8], self.R[8:]]

    @property
    def R_trichords(self):
        return [self.R[:3], self.R[3:6], self.R[6:9], self.R[9:]]

    @property
    def RI(self):
        return [
            tone + self._transposition
            for tone in self._retrograde_inversion]

    @property
    def RI_hexachords(self):
        return [self.RI[:6], self.RI[6:]]

    @property
    def RI_tetrachords(self):
        return [self.RI[:4], self.RI[4:8], self.RI[8:]]

    @property
    def RI_trichords(self):
        return [self.RI[:3], self.RI[3:6], self.RI[6:9], self.RI[9:]]
