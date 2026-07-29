from pygame import *
from Class import *
from levels import *
import pygame.surfarray as surfarray
init()
clock = time.Clock()
level = 1
world = 1
objects = [obj for obj in levels[level][world].values()]
player = levels[level][0]
spikes = levels[level][world + 3]
always_objects = [Object(0, 0, 800, 20), 
                  Object(0, 580, 800, 20), 
                  Object(0, 0, 20, 600), 
                  Object(780, 0, 20, 600)]
teleporter = levels[level][3]
all_objects = always_objects + objects
label = font.Font(None, 36)
label_surface = label.render(f"Level {level}", True, (255, 255, 255))
invert = False
while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.jump()
            if e.key == K_f:
                if world == 1:
                    world = 2
                    objects = [obj for obj in levels[level][world].values()]
                    all_objects = always_objects + objects
                    invert = not invert
                    spikes = levels[level][world + 3]
                elif world == 2:
                    world = 1
                    objects = [obj for obj in levels[level][world].values()]
                    all_objects = always_objects + objects
                    invert = not invert
                    spikes = levels[level][world + 3]
    player.move(all_objects)
    player.update(all_objects)
    screen.fill((0, 0, 0))
    teleporter.draw(screen)
    screen.blit(label_surface, (50, 50))
    player.draw(screen)
    for spike in spikes:
        spike.draw(screen)
        player.death(spike)
    for obj in always_objects:
        obj.draw(screen)
    for obj in objects:
        obj.draw(screen)
    if invert:
        arr = surfarray.array3d(screen)
        arr[:] = 255 - arr
        surfarray.blit_array(screen, arr)
    player.teleport(teleporter)
    if player.change_level:
        level += 1
        world = 1

        player = levels[level][0]
        teleporter = levels[level][3]
        spikes = levels[level][world + 3]

        objects = [obj for obj in levels[level][world].values()]
        all_objects = always_objects + objects

        player.change_level = False
        invert = False

        label_surface = label.render(f"Level {level}", True, (255, 255, 255))
    display.update()
    clock.tick(60)