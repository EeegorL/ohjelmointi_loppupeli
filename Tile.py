def v(code):
    match(code):
        case 1:
            return (66,66,66);
        case 2:
            return (33,33,33);
        case 3:
            return (0,0,0);
        case _:
            return (0,0,0);

class Tile:
    def __init__(self, x, y, b, c):
        self.x = x;
        self.y = y;
        self.passable = b;
        self.c = v(c);