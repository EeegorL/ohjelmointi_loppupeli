import pygame as pg;
from Map import Map;
from Image import Image;

Image.init();
pg.init();

w = 960;
h = 640;
size = 64;

main = pg.display.set_mode((w, h));

pg.display.set_caption("lataa...");
print("Ladataan karttaa...");
map = Map(int(size * 3), int(size * 3));
print("Kartta ladattu");
pg.display.set_caption("Mauno-monoliitin seikkailut");

x = 29;
y = 29;

playerImg = Image.get("p");
dirtImg1 = Image.get("1");
dirtImg2 = Image.get("2");

while(True):
    pX = x - 8;
    pY = y - 5;

    for e in pg.event.get():
        if(e.type == pg.QUIT):
            exit();

        if(e.type == pg.KEYDOWN):
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
            main.blit(r.img, (j*size, i*size));
    

    main.blit(playerImg, ((w/size) * size/2 - 0.5*size, (h / size) * size / 2));

    pg.display.flip();