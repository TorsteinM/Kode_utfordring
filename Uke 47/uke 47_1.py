import pygame as pg, sys
screen, _ = (pg.display.set_mode([800, 600]), pg.init())
while True:
    for event in pg.event.get(): 
        if event.type == pg.QUIT: sys.exit()
    screen.fill((255,255,255))
    pg.display.flip()