from pygame import *
from Class import *
from levels import *
init()
clock = time.Clock()
player = Player(100, 100)
objects = [obj for obj in levels[1].values()]
while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.jump()
    player.move(objects)
        
    player.update(objects)

    screen.fill((30, 30, 30))

    player.draw(screen)
    for obj in objects:
        obj.draw(screen)
    display.update()
    clock.tick(60)