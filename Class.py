from pygame import *
from math import floor
init()
screen = display.set_mode((800, 600))
class Player:
    def __init__(self, x, y):
        self.standing = transform.scale(image.load("Blob/Standing/pixil-frame-9.png"), (100, 100))
        self.image = self.standing
        self.frame_run_right = 0
        self.frame_run_left = 0
        self.velocity_y = 0
        self.gravity = 1
        self.on_ground = False
        self.rect = Rect(x + 25, y, 50, 100)
        self.rect.width = 50
        self.rect.centerx = x + 50
        self.walk_right = [transform.scale(image.load(f"Blob/RunningRight/pixil-frame-{i}.png"), (100, 100)) for i in range(0, 9)]
        self.walk_left = [transform.flip(img, True, False) for img in self.walk_right]
        self.change_level = False
    def update(self, objects):
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        self.on_ground = False

        for obj in objects:
            if self.rect.colliderect(obj.image):
                if self.velocity_y > 0:
                    self.rect.bottom = obj.image.top
                    self.velocity_y = 0
                    self.on_ground = True
            if self.rect.colliderect(obj.image):
                if self.velocity_y < 0:
                    self.rect.top = obj.image.bottom
                    self.velocity_y = 0

    def jump(self):
        if self.on_ground:
            self.velocity_y = -20
    def move(self, objects):
        keys = key.get_pressed()
        if keys[K_d]:
            self.rect.x += 5
            self.frame_run_right += 0.25
            self.frame_run_left = 0
            self.image = self.walk_right[floor(self.frame_run_right)]
            for obj in objects:
                if self.rect.colliderect(obj.image):
                    self.rect.right = obj.image.left

        elif keys[K_a]:
            self.rect.x -= 5
            self.frame_run_left += 0.25
            self.frame_run_right = 0
            self.image = self.walk_left[floor(self.frame_run_left)]
            for obj in objects:
                if self.rect.colliderect(obj.image):
                    self.rect.left = obj.image.right
        else:
            self.frame_run_right = 0
            self.frame_run_left = 0
            self.image = self.standing

        if self.frame_run_right >= len(self.walk_right) - 1:
            self.frame_run_right = 0
        if self.frame_run_left >= len(self.walk_left) - 1:
            self.frame_run_left = 0 
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x - 25, self.rect.y))
    def teleport(self, teleporter):
        if self.rect.colliderect(teleporter.image):
            self.change_level = True


class Object:
    def __init__(self, x, y, w, h):
        self.image = Rect(x, y, w, h)

    def draw(self, screen):
        draw.rect(screen, (0, 255, 0), self.image)
class Teleporter:
    def __init__(self, x, y, w, h):
        self.image = Rect(x, y, w, h)

    def draw(self, screen):
        draw.rect(screen, (255, 0, 0), self.image)
    