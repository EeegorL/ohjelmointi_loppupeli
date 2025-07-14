from random import randint;
from Tile import Tile;

class Map:
    def __init__(self, w, h):
        self.w = w;
        self.h = h;
        self.rows = [[Tile(32*x, 32*y, False, 1) for x in range(0, 2*w)] for y in range(10)] + \
                    [[Tile(c, r, 1, 1) for r in range(0, 20)] + [Tile(c, r, 1, randint(1,6)) for r in range(0, self.w)] + [Tile(c, r, 1, 1) for r in range(0, 20)] for c in range(0, self.h)] + \
                    [[Tile(32*x, 32*y, False, 1) for x in range(0, 2*w)] for y in range(10)]