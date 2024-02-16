import pygame   # Laeme pygame mooduli
import random   # Laeme  juhugeneraatori mooduli

pygame.init()

screen = pygame.display.set_mode([640, 480])            # Loome akna
pygame.display.set_caption("autod - Anders Kivitar")    # Lisame aknale teksti
clock = pygame.time.Clock()                             # Määrame kella

autos = pygame.image.load("f1_blue.png")                # Laeme vajalikud pildid
autop = pygame.image.load("f1_red.png")
taust = pygame.image.load("bg_rally.jpg")
auto = pygame.transform.flip(autos, True, True)     # Pöörame sinise auto ninaga allapoole
tausty = pygame.transform.flip(taust, False, True)  # Pöörame ka taustpilti, et tekitada liikumis muljet
ya3 = 100                   # Määrame siniste autode Y-telje esmakoordinaadid, et nad ei alustaks koos ühelt kõrguselt
ya4 = 0
skoor3 = 0                  # Nullime skoori
skoor4 = 0
a = random.randint(2, 4)        # Et oleks ilusam, genereerime kiiruse muutmiseks kaks juhuarvu, et autod liiguksid
b = random.randint(2, 4)        # erinevate kiirustega, mida kasutame esimeseks liikumiseks
font = pygame.font.SysFont('Arial', 25)     # määrame teksti fondi


running = True              # Muutuja running saab väärtuseks True
while running:              # Loome tsykli akna püsimiseks

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False#


    text3 = font.render("Skoor " + str(skoor3), True, [255, 255, 255]) # renderdame teksti koos muutuva väärtusega
    text4 = font.render("Skoor " + str(skoor4), True, [255, 255, 255])
    text5 = font.render("Missed " + str(skoor3 + skoor4), True, [255, 0, 255])  # renderdame ka koguskoori teksti
    k = random.randint(100, 111)        # et oleks huvitavam genereerime juhuarvu taustpildi muutmise kiiruseks

    clock.tick(k)                           # määrame taustpild kiiruse
    screen.blit(taust, [0, 0])      # Paneme ekraanile taustpildi
    screen.blit(autop, [300, 380])  # Paneme ekraanile punase auto
    screen.blit(auto, [180, ya3])   # Paneme ekraanile üles ühe sinise auto
    screen.blit(auto, [420, ya4])   # Paneme ekraanile üles teise sinise auto
    screen.blit(text3, [20, 420])   # Paneme ekraanile vasakpoolse skoori lugemise teksti
    screen.blit(text4, [540, 420])  # Paneme ekraanile parempoolse skoori lugemise teksti
    screen.blit(text5, [275, 100])  # Paneme ekraanile keskele kogu skoori teksti
    pygame.display.flip()                   # Toome ekraani nähtavale

    if ya3 > 480:                   # kontrollime, kas vasakpoolne auto on jõudnud pildi alla äärde
        ya3 = -80                   # kui on, siis anname uue Y-kordinaadi, et ta alustaks uuesti ülevalt
        skoor3 = skoor3 + 1         # kui on, siis lisame ka skoorile ühe juurde
        a = random.randint(2, 4)    # genereerime järgmiseks üleekraani liikumiseks uue kiiruse
    else:
        ya3 = ya3 + a       # Kui auto pole veel alla jõudnud, siis liigutame teda allapoole vastavalt praegu kasutuses oleva kiirusega

    if ya4 > 480:                   # Kontrollime, kas parempoolne auto on jõudnud pildi alla äärde
        ya4 = -80                   # Kui jah, siis anname uue Y-koordinaadi, et ta alustaks uuesti ülevalt
        skoor4 = skoor4 + 1         # Lisame ka skoorile ühe juurde
        b = random.randint(2, 4)    # genereerime parempoolsele autole uue kiiruse
    else:
        ya4 = ya4 + b               # muidu liigutame autot allapoole vastavalt kasutuses oleva kiirusega

    clock.tick(k)
    screen.blit(tausty, [0, 0])     # paneme ekraanile pööratud taustpildi, et tekitada tee telgjoonte liikumine
    screen.blit(autop, [300, 380])
    screen.blit(auto, [180, ya3])
    screen.blit(auto, [420, ya4])
    screen.blit(text3, [20, 420])
    screen.blit(text4, [540, 420])
    screen.blit(text5, [275, 100])
    pygame.display.flip()                                                # Värskendame akent

pygame.quit()