from random import randint;
from Tile import Tile;

class Map:
    def __init__(self, w, h):
        self.w = w;
        self.h = h;
        self.rows = [[Tile(32*y, 32*x, False, None) for y in range(0, w+2*15)] for x in range(10)] + \
                    [[Tile(c, r, False, None) for r in range(0, 15)] + [Tile(c, r, True, str(randint(1,2))) for r in range(0, self.w)] + [Tile(c, r, False, None) for r in range(0, 15)] for c in range(0, self.h)] + \
                    [[Tile(32*x, 32*y, False, None) for x in range(0, w+2*15)] for y in range(10)];