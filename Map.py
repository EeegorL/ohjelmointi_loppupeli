from random import randint;
from Tile import Tile;

class Map:
    def __init__(self, w, h):
        self.w = w;
        self.h = h;
        # self.rows = [[Tile(32*x, 32*y, False, 1) for x in range(0, w+2*15)] for y in range(10)] + \
        #             [[Tile(c, r, False, 1) for r in range(0, 15)] + [Tile(c, r, True, randint(1,6)) for r in range(0, self.w)] + [Tile(c, r, False, 1) for r in range(0, 15)] for c in range(0, self.h)] + \
        #             [[Tile(32*x, 32*y, False, 1) for x in range(0, w+2*15)] for y in range(10)];
        self.rows = [[Tile(32 * x, 32 * y, True if randint(1,10) > 2 else False, randint(1,3)) for y in range(0, self.h)] for x in range(0, self.w)];
