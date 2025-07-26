import pygame as pg;
from Map import Map;
from Image import Image;
from sys import exit as _exit;

Image.init();
pg.init();

w = 960;
h = 640;
size = 64;

player = {
    "x": 29,
    "y": 29,
    "coins": 0,
    "img": Image.get("p")
};

main = pg.display.set_mode((w, h));

pg.display.set_caption("lataa...");
print("Ladataan karttaa...");
map = Map(int(size * 3), int(size * 3), player);
print("Kartta ladattu");
pg.display.set_caption("Mauno-monoliitin seikkailut");

playerImg = Image.get("p");

actionPressed = False;

font1 = pg.font.SysFont("Arial", 36);

coinsSurf = font1.render(f"Kolikkeja: {player['coins']}", True, (255,255,255));
font2 = pg.font.SysFont("Arial", 16);
controlSurf = font2.render("Liikkuminen: WASD, Toimintonappi: E", True, (255, 255, 255));

while(True):
    pX = player["x"] - 8;
    pY = player["y"] - 5;
    currentTile = map.rows[pY][pX];

    for e in pg.event.get():
        if(e.type == pg.QUIT):
            _exit();

        if(e.type == pg.KEYDOWN):
            if(e.key == pg.K_w and map.rows[pY - 1][pX].passable):
                player["y"] -= 1;
            if(e.key == pg.K_a and map.rows[pY][pX - 1].passable):
                player["x"] -= 1;
            if(e.key == pg.K_s and map.rows[pY + 1][pX].passable):
                player["y"] += 1;
            if(e.key == pg.K_d and map.rows[pY][pX + 1].passable):
                player["x"] += 1;

            if(e.key == pg.K_e):
                if(not actionPressed and currentTile.event):
                    actionPressed = True;
                    currentTile.event.action();
                    currentTile.event = None;
                    coinsSurf = font1.render(f"Kolikkeja: {player['coins']}", True, (255,255,255));
                
        if(e.type == pg.KEYUP):
            if(e.key == pg.K_e):
                actionPressed = False;

    main.fill((0,0,0));
    
    for i, c in enumerate(map.rows[player["y"]-int(h/size):player["y"]+int(h/size)+1]):
        for j, r in enumerate(c[player["x"]-int(w/size):player["x"]+int(w/size+1)]):
            main.blit(r.img, (j*size, i*size));
            if(r.event):
                main.blit(r.event.img, (j*size, i*size));
    
    main.blit(coinsSurf, (main.get_width() - coinsSurf.get_width() - 15, 0));
    main.blit(playerImg, ((w/size) * size/2 - 0.5*size, (h / size) * size / 2));
    main.blit(controlSurf, (main.get_width() - controlSurf.get_width() - 15, main.get_height() - controlSurf.get_height() - 15));

    pg.display.flip();