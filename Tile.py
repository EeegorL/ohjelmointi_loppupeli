from Event import Event;
from Image import Image;

class Tile:
    def __init__(self, x, y, passable, img, eventCode=None, player=None):
        self.x = x;
        self.y = y;
        self.passable = passable;
        self.img = Image.get(img);
        self.event = Event(self, eventCode, player) if eventCode != None else None;

    def __str__(self):
        return f"x:{self.x}, y:{self.y}, color: {self.img}, passable: {self.passable}";