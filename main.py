import pygame as pg;
from Map import Map;
from Image import Image;
from sys import exit as _exit;

Image.init();
pg.init();
kello = pg.time.Clock();

w = 960;
h = 640;
size = 64;

player = {
    "x": 29,
    "y": 29,
    "coins": 0,
    "tarpeeksiKolikoita": False,
    "onLippu": False,
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
font2  = pg.font.SysFont("Arial", 24);
font3 = pg.font.SysFont("Arial", 16);
font4 = pg.font.SysFont("Arial", 14);

gameState = 0;

coinsSurf = font2.render(f"Kolikkoja: {player['coins']} / 50", True, (255,255,255));
lippuSurf = font2.render(f"Lippu: Kateissa...", True, (255,255,255));
controlSurf = font3.render("Liikkuminen: WASD, Toimintonappi: E", True, (255, 255, 255));
loppuSurf = font2.render(f"Paina välilyöntiä (SPACE) lähteäksesi matkaan!", True, (255,255,255));

name = font1.render(f"Mauno-monoliitin pulma", True, (255,255,255));
r1 = font2.render(f"Mauno-monoliitti oli matkalla Ikaalisiin sukulaistensa luo, mutta kadotti junalippunsa.", True, (255,255,255));
r2 = font2.render(f"Auta Mauno-raukkaa keräämään tarpeeksi kolikoita uuteen (50 kolikkoa).", True, (255,255,255));
r3 = font2.render(f"Tai mahtaisiko lippu lojua vielä jossain...?", True, (255,255,255));
r4 = font3.render(f"Paina jotain nappia aloittaaksesi (näppäimistöllä, älä koneen sammutusnappia)", True, (255,255,255));

while(True):
    if(gameState == 0): # alkuruutu
        for e in pg.event.get():
            if(e.type == pg.QUIT):
                _exit();
            if(e.type == pg.KEYDOWN):
                gameState = 1;
    
            main.fill((130, 130, 130));
            main.blit(name, (main.get_width()/2 - name.get_width()/2, 50));
            main.blit(r1, (main.get_width()/2 - r1.get_width()/2, 150));
            main.blit(r2, (main.get_width()/2 - r1.get_width()/2, 200));
            main.blit(r3, (main.get_width()/2 - r1.get_width()/2, 250));
            main.blit(r4, (main.get_width()/2 - r1.get_width()/2, 350));

    elif(gameState == 1): # varsinainen peli
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
                if(e.key == pg.K_SPACE and (player["tarpeeksiKolikoita"] or player["onLippu"])):
                    l1 = font1.render(f"Voitit!", True, (255,255,255));
                    l2 = font2.render(f"{"Löysit lipun!" if player['onLippu'] else "Sait ostettua Maunolle uuden lipun!"}", True, (255,255,255));
                    l3 = font3.render("Mauno pääsee nyt turvallisesti kotiinsa perheen luo. Kiitos avusta!", True, (255,255,255));
                    l4 = font3.render("Voit sulkea pelin painamalla ESCAPE-näppäintä", True, (255,255,255));

                    if((player["onLippu"] and player["coins"] > 0) or (player["coins"] > 50)):
                        ex = player["coins"] if player["onLippu"] else player["coins"] - 50;
                        if(ex < 10): l3 = font3.render("Keräsit pari lanttia ylimääräistä, Mauno saa ostettua vaikkapa sipsejä matkalle!", True, (255,255,255));
                        elif(10 < ex < 25): l3 = font3.render("Keräsit kohtalaisen summan ylimääräistäkin, riittää varmaan Maunon junalounaaseen?", True, (255,255,255));
                        elif(25 <= ex < 30): l3 = font3.render("Noukit maasta aikamoisen summan, Mauno voisi ostaa vaikkapa tuliaisia!", True, (255,255,255));
                        else: l3 = font4.render("Keräsit... noin ison summan? Keskityitkö lipun hankkimiseen vai muuten vain kiiltäviin kolikoihin? Joka tapauksessa, Mauno palaa kotiin rikkaana!", True, (255,255,255));
                    
                    gameState = 2;
            
                if(e.key == pg.K_e):
                    if(not actionPressed and currentTile.event):
                        actionPressed = True;
                        currentTile.event.action();
                        currentTile.event = None;
                        
                        coinsSurf = font2.render(f"Kolikkoja: {player['coins']} / 50", True, (255,255,255));
                        lippuSurf = font2.render(f"Lippu: {"Löytynyt!" if player["onLippu"] else "Kateissa..."}", True, (255,255,255));

                        if(player["coins"] >= 50):
                            player["tarpeeksiKolikoita"] = True;
                                    
                if(e.key == pg.K_e):
                    actionPressed = False;

        main.fill((0,0,0));
        
        for i, c in enumerate(map.rows[player["y"]-int(h/size):player["y"]+int(h/size)+1]):
            for j, r in enumerate(c[player["x"]-int(w/size):player["x"]+int(w/size+1)]):
                main.blit(r.img, (j*size, i*size));
                if(r.event):
                    main.blit(r.event.img, (j*size, i*size));
        
        main.blit(coinsSurf, (0, main.get_height()/ 2 - lippuSurf.get_height() - 50));
        main.blit(lippuSurf, (0, main.get_height()/ 2 - lippuSurf.get_height()));
        main.blit(playerImg, ((w/size) * size/2 - 0.5*size, (h / size) * size / 2));
        main.blit(controlSurf, (main.get_width() - controlSurf.get_width() - 15, main.get_height() - controlSurf.get_height() - 15));
        if((player["tarpeeksiKolikoita"] or player["onLippu"])):
            main.blit(loppuSurf, (0, main.get_height()/ 2 - lippuSurf.get_height() + 50))

    elif(gameState == 2): # loppu
        for e in pg.event.get():
            if(e.type == pg.QUIT):
                _exit();
            if(e.type == pg.KEYDOWN):
                if(e.key == pg.K_ESCAPE):
                    _exit();

        main.fill((191, 175, 33));
        main.blit(l1, (main.get_width()/2 - l1.get_width()/2, 50));
        main.blit(l2, (main.get_width()/2 - l2.get_width()/2, 100));
        main.blit(l3, (main.get_width()/2 - l3.get_width()/2, 150));
        main.blit(l4, (main.get_width()/2 - l4.get_width()/2, 250));

    pg.display.flip();
    kello.tick(30);