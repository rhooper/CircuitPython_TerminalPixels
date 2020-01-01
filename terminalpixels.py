
import sys

class TerminalPixels:

    def __init__(self, n=80, x=1, y=1, rows=1, auto_write=True):
        self.n = n
        self.bpp = 3
        self._x = x
        self._y = y
        self._rows = rows
        self._chars_per_row = ceil(n / rows)
        self.pixels = [(0, 0, 0)] * n
        self.auto_write = auto_write
        sys.stdout.write('%c[2J' % 27)

    def show(self):
        sys.stdout.write('%c[s%c[%d;%dH' % (27, 27, self._x, self._y))
        sys.stdout.write(
            ''.join(['%c[48;2;%d;%d;%dm ' % (27, item[0], item[1], item[2]) for item in self.pixels]))
        sys.stdout.write('%c[u' % 27)
        sys.stdout.flush()

    def __setitem__(self, key, value):
        if isinstance(value, int):
            value = (value >> 16 & 255, value >> 8 & 255, value & 255)
        self.pixels[key] = value
        if self.auto_write:
            self.show()

    def __getitem__(self, item):
        return self.pixels[item]

    def __len__(self):
        return len(self.pixels)

    def fill(self, color):
        for n in range(self.n):
            self.__setitem__(n, color)
