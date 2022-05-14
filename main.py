import pygame
import random

display = pygame.display.set_mode((480, 640))

bg = pygame.image.load("bg.png")
player = pygame.image.load("player_left.png")
platform = pygame.image.load("platform.png")

platform.set_colorkey((255, 255, 255))

y = 320
x = 240

px = 240
py = 360

px2 = random.randint(0, 480)
py2 = random.randint(-50, 0)

px3 = random.randint(0, 480)
py3 = random.randint(-50, 0)

timer = 0
start_timer = 0

platform = pygame.transform.scale(platform, (60, 25))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if py >= 640:
        px = random.randint(0, 480)
        py = random.randint(-50, 0)
    if py2 >= 640:
        px2 = random.randint(0, 480)
        py2 = random.randint(-50, 0)
    if py3 >= 640:
        px3 = random.randint(0, 480)
        py3 = random.randint(-50, 0)

    if x >= px and x <= px + 60:
        if y <= py and y+65 >= py:
            start_timer = 1
    if x >= px2 and x <= px2 + 60:
        if y <= py2 and y+65 >= py2:
            start_timer = 1
    if x >= px3 and x <= px3 + 60:
        if y <= py3 and y+65 >= py3:
            start_timer = 1

    if start_timer == 1:
        timer += 1

    if timer >= 800:
        start_timer = 0
        timer = 0

    if timer > 0:
        py += 0.25
        py2 += 0.25
        py3 += 0.25

    if start_timer == 0:
        py -= 0.25
        py2 -= 0.25
        py3 -= 0.25

    display.blit(bg, (0, 0))
    display.blit(player, (x, y))
    display.blit(platform, (px, py))
    display.blit(platform, (px2, py2))
    display.blit(platform, (px3, py3))
    pygame.display.update()
