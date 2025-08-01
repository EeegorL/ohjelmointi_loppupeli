from Image import Image;

class Event:
    def __init__(self, tile, code, player=None):
        self.tile = tile;
        self.code = code;
        self.player = player;
    
    @property
    def img(self):
        return Image.get(self.code);

    def action(self):
        match(self.code):
            case "kolikko":
                self.player["coins"] += 1;
            case "lippu":
                self.player["onLippu"] = True;