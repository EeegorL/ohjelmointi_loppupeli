import pygame as pg;
from random import randint;

pg.init();
#                           17  x  11
main = pg.display.set_mode((1088, 640));

wallHor = [[3 for _ in range(0, 200)] for _ in range(0, 5)];
wallVert = [3 for _ in range(0,8)];
map = wallHor + [wallVert + [randint(1,2) for _ in range(0,200)] + wallVert for _ in range(0,150)] + wallHor;

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
        case _:
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

    for i, c in enumerate(map[y-5:y+6]):
        for j, r in enumerate(c[x-8:x+9]):
            pg.draw.rect(main, v(r), pg.Rect(j*64, i*64, 64, 64));
    
    pg.draw.rect(main, (140, 50, 77), pg.Rect(8*64, 5*64, 64, 64));

    pg.display.flip();