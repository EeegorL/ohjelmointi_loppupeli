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
    pX = x - 15;
    pY = y - 10;
    for e in pg.event.get():
        if(e.type == pg.QUIT):
            exit();

        if(e.type == pg.KEYDOWN):
            print(map.rows[y][x])
            if(e.key == pg.K_w and map.rows[pY - 1][pX].passable):
                y -= 1;
            if(e.key == pg.K_a and map.rows[pY][pX - 1].passable):
                x -= 1;
            if(e.key == pg.K_s and map.rows[pY + 1][pX].passable):
                y += 1;
            if(e.key == pg.K_d and map.rows[pY][pX + 1].passable):
                x += 1;

    main.fill((0,0,0));
    map.rows[pY][pX].c = (255,255,0);
    
    for i, c in enumerate(map.rows[y-int(h/size):y+int(h/size)+1]):
        for j, r in enumerate(c[x-int(w/size):x+int(w/size+1)]):
            pg.draw.rect(main, r.c, pg.Rect(j*size, i*size, size, size));
    
    pg.draw.rect(main, (140, 50, 77), pg.Rect((w/size)/2*size, (h/size)/2*size, size, size));

    pg.display.flip();