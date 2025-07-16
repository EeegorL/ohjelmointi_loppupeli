def v(code):
    match(code):
        case 0:
            return (31, 2, 0);
        case 1:
            return (66,66,66);
        case 2:
            return (33,33,33);
        case 3:
            return (0,0,0);
        case _:
            return (0,0,0);

class Tile:
    def __init__(self, x, y, passable, c):
        self.x = x;
        self.y = y;
        self.passable = passable;
        # self.c = v(c);
        self.c = (55,55,55) if passable else (0,0,0);
        
    def __str__(self):
        return f"{self.x}:{self.y}, color: {self.c}, passable: {self.passable}";