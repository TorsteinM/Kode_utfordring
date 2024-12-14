import pygame as pg
pg.init()
screen = pg.display.set_mode((800, 600))
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit(),quit()
    for y in range(600):
        pg.draw.line(screen, (255, 255, (y*255)//800), (0, y), (800, y), 1)
    pg.display.flip()