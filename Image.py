import pygame as pg;
from utils import v;


class Image:
    size = 32;
    def __init__(self, id):
        self.id = id;

    @classmethod
    def parse(self, bits):
        p = pg.Surface((Image.size, Image.size), pg.SRCALPHA);

        rows = bits.split(" ");

        if(len(rows[0]) == 16):
            for j, r in enumerate(rows):
                for i, c in enumerate(r):
                    vari = v(c);
                    if(vari != None):
                        pg.draw.rect(p, vari, pg.Rect(i*2, j*2, 2, 2));
        else:
            for j, r in enumerate(rows):
                for i, c in enumerate(r):
                    vari = v(c);
                    if(vari != None):
                        pg.draw.rect(p, vari, pg.Rect(i, j, 1, 1));

        return pg.transform.scale(p, (64, 64));

    @classmethod
    def make(self, id):
        match(id):
            case "p": # pelaajahahmo
                bits = \
                    "................................ "+\
                    ".......llllllllllllllllll....... "+\
                    ".......leeeeeeeeeeeeeeeel....... "+\
                    ".......lepppeeeppeeepppel....... "+\
                    ".......leppepapeepapeppel....... "+\
                    ".......leppepappppappppel....... "+\
                    ".......leppepappppappppel....... "+\
                    ".......leppppppppppppppel....... "+\
                    ".......leppppppppppppppel....... "+\
                    ".......leppppppppppppppel....... "+\
                    ".......leppppppppppppppel....... "+\
                    ".....aaleppppppppppppppelaa..... "+\
                    "....aaaleppppppppppppppelaaa.... "+\
                    "....aaaleppppppppppppppelaaa.... "+\
                    "....aa.leppppppppppppppel.aa.... "+\
                    "...aaa.leppppppppppppppel.aaa... "+\
                    "...aaa.leppppppppppppppel.aaa... "+\
                    "...aaa.leppppppppppppppel.aaa... "+\
                    "...aaa.leppppppppppppppel.aaa... "+\
                    "...aaa.leppppppppppppppel.aaa... "+\
                    ".......leppppppppppppppel....... "+\
                    ".......leppppppppppppppel....... "+\
                    ".......leppppppppppppppel....... "+\
                    ".......leppppppppppppppel....... "+\
                    ".......leppppppppppppppel....... "+\
                    ".......leppppppppppppppel....... "+\
                    ".......leppppppppppppppel....... "+\
                    ".......leppppppppppppppel....... "+\
                    ".......leppppppppppppppel....... "+\
                    ".......leeeeeppppppeeeeel....... "+\
                    "......aaaaaaeeeeeeeeaaaaaa...... "+\
                    "......aaaaaallllllllaaaaaa......";
                    
        
            case "1": # hiekka 1
                bits =  \
                    "2222221121111122 "+\
                    "1221111122222221 "+\
                    "2222112221222221 "+\
                    "1112222222222222 "+\
                    "2222222221111111 "+\
                    "1222221112222221 "+\
                    "1111122222222221 "+\
                    "1112222222222111 "+\
                    "2222221221122222 "+\
                    "1222222221112211 "+\
                    "1211222122221122 "+\
                    "1112222212211112 "+\
                    "1122112222222221 "+\
                    "1222212221121111 "+\
                    "2221222222222112 "+\
                    "1122221111112222";
            case "2": # hiekka 2
                bits =  \
                    "2222121212221211 " +\
                    "1122212211122222 " +\
                    "1212222211212122 " +\
                    "2111222221112222 " +\
                    "1122222112221211 " +\
                    "2221122211122221 " +\
                    "1122221222211122 " +\
                    "1221222211222111 " +\
                    "1112222212222112 " +\
                    "2222111222212222 " +\
                    "1122222221212221 " +\
                    "2211122221221222 " +\
                    "1212222221122222 " +\
                    "2222221122211121 " +\
                    "2222222111112221 " +\
                    "1112222212222112";
            
            case "kolikko":
                bits =  \
                    "................ " +\
                    "................ " +\
                    "................ " +\
                    "....tttttttt.... " +\
                    "...tyyyyyyyyt... " +\
                    "...tytyyyytyt... " +\
                    "...tyttyytyyt... " +\
                    "...tytytyyyyt... " +\
                    "...tytytyyyyt... " +\
                    "...tyttyytyyt... " +\
                    "...tytyyyytyt... " +\
                    "...tyttttttyt... " +\
                    "....tttttttt.... " +\
                    "................ " +\
                    "................";
            case "lippu":
                bits = \
                    "....cccccccccc.. " +\
                    "...ccccccccxxcc. " +\
                    "...cuuuuuucxxcc. " +\
                    "...ccccccccccc.. " +\
                    "...cccccccccc... " +\
                    "...cuuuuuuccc... " +\
                    "...cccccccccc... " +\
                    "...cccccccccc... " +\
                    "...cuuuuccccc... " +\
                    "...cccccccccc... " +\
                    "...ccccuuuccc... " +\
                    "...ccccccuucc... " +\
                    "...cccuuccccc... " +\
                    "..cccccuuuccc... " +\
                    ".ccccccccuccc... " +\
                    ".ccccccccccc....";
                
            case "testi": # testipunainen
                bits= \
                    "................ " +\
                    "................ " +\
                    "................ " +\
                    "................ " +\
                    "................ " +\
                    "................ " +\
                    "................ " +\
                    "................ " +\
                    "................ " +\
                    "................ " +\
                    "................ " +\
                    "................ " +\
                    "................ " +\
                    "................ " +\
                    "................ " +\
                    "................";
            
            case _: # kiviseinät (mapin reunat)
                bits = \
                    "uuuuuuuuvvwvvvuw "+\
                    "uuuuuuuvwwwwwvvv "+\
                    "uuuuuuvwwuuuwwwv "+\
                    "vvvvvvwwuuuuuuww "+\
                    "wwwwwwwuuuuuuuww "+\
                    "uuuuuuuuuuuuuuuu "+\
                    "uuuuuuuuuuuuuvvv "+\
                    "uuuvvvuuuuuvvvwv "+\
                    "uuuvwvuuuvvwwwww "+\
                    "uuvwwwvvvvwwuuuu "+\
                    "vvvwwuwwwwwuuuuu "+\
                    "vwwwuuuuuuuuuuuu "+\
                    "wwvvvvvuuuuuuuuu "+\
                    "vvvwwwvvuuuuuuuu "+\
                    "vwwwwwwvvuvvvvuu "+\
                    "vwuuuuwwwvvwwvvv";
        
        return Image.parse(bits);

    @classmethod
    def init(cls):
        cls.images = {
            "p": cls.make("p"),
            "1": cls.make("1"),
            "2": cls.make("2"),
            "kolikko": cls.make("kolikko"),
            "lippu": cls.make("lippu"),
            None: cls.make(None)
        };

    @classmethod
    def get(cls, id):
        return cls.images[id];

