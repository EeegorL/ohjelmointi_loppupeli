import pygame as pg;

from Map import Map;

pg.init();

w = 960;
h = 640;
size = 32;

main = pg.display.set_mode((w, h));
map = Map(int(size * 3), int(size * 3));

x = 50;
y = 50;

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
    # marg 16 10
    for i, c in enumerate(map.rows[y-int(h/size):y+int(h/size)+1]):
        for j, r in enumerate(c[x-int(w/size):x+int(w/size+1)]):
            pg.draw.rect(main, r.c, pg.Rect(j*size, i*size, size, size));
    
    pg.draw.rect(main, (140, 50, 77), pg.Rect((w/size)/2*size, (h/size)/2*size, size, size));

    pg.display.flip();