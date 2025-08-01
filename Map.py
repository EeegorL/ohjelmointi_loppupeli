from random import randint;
from Tile import Tile;



    

class Map:
    def __init__(self, w, h, player):
        self.w = w;
        self.h = h;
        self.lippuAsetettu = False;

        def randEvt(m):
            if(randint(1, 1000) == 1 and not m.lippuAsetettu):
                m.lippuAsetettu = True;
                return "lippu";

            rand = randint(1,10);
            if(rand == 10):
                return "kolikko";
            else:
                return None;
    
        def getMap():
            vertEdge = [[Tile(32*y, 32*x, False, None) for y in range(0, w+2*15)] for x in range(10)];

            while(not self.lippuAsetettu): # uudelleenluo karttan kunnes luodaan sellainen jossa on lippu lojumassa. Voisi tehdä paljon nätimmin, mutta päätä särkee...
                middlePart = [[Tile(c, r, False, None) for r in range(0, 15)] + [Tile(c, r, True, str(randint(1,2)), randEvt(self), player) for r in range(0, self.w)] + [Tile(c, r, False, None) for r in range(0, 15)] for c in range(0, self.h)];
            
            map = vertEdge + \
                 middlePart + \
                vertEdge;
            return map;
        
        self.rows = getMap();
