import pygame as pg;
from random import randint;

pg.init();

main = pg.display.set_mode((1280, 960));


wallLayerVert = [[3 for _ in range(0, 200)] for _ in range(0, 7)];
wallLayerHor = [3 for _ in range(0,7)];
map = wallLayerVert + [wallLayerHor + [randint(1,2) for _ in range(0,200)] + wallLayerHor for _ in range(0,150)] + wallLayerVert;

x = 50;
y = 50;


def v(code):
    match(code):
        case 1:
            return (66,66,66);
        case 2:
            return (33,33,33);
        case 3:
            return (0,0,0);

while(True):
    for e in pg.event.get():
        if(e.type == pg.QUIT):
            exit();

        if(e.type == pg.KEYDOWN):
            if(e.key == pg.K_w):
                y -= 1;
            if(e.key == pg.K_a):
                x -= 1;
            if(e.key == pg.K_s):
                y += 1;
            if(e.key == pg.K_d):
                x += 1;

    main.fill((0,0,0));

    for i, c in enumerate(map[y-7:y+8]):
        for j, r in enumerate(c[x-10:x+10]):
            pg.draw.rect(main, v(r), pg.Rect(j*64, i*64, 64, 64));
    
    pg.draw.rect(main, (140, 50, 77), pg.Rect(10*64, 7*64, 64, 64));

    pg.display.flip();