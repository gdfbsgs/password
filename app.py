import pygame

pygame.init()
win = pygame.display.set_mode((1545,900))




x = 10
a = 10
while True:
    x = x + 0.123232132113
    if x > 1000:
        x = 0
    a = a + 121
    if a > 1000:
        a = 0
    win.fill((255,255,255))
    pygame.draw.rect(win, (184,71, 100), (x, x, x, x))
    pygame.draw.rect(win, (23, 1, 100), (a, x, a, x))
    pygame.draw.rect(win, (134, 1, 100), (500, x, x, x))
    pygame.display.update()
for i in pygame.event.get():
    if i.type != pygame.QUIT:
        pass
    else:
        exit()