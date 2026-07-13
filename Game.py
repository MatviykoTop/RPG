from pygame import *
init()
screen = display.set_mode((800, 600))
clock = time.Clock()
while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
    screen.fill((0, 0, 0))
    display.flip()
    clock.tick(60)