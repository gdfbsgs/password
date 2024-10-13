import pygame

pygame.init()
win = pygame.display.set_mode((450, 450))

class Board:
    def draw_line(self):
        pygame.draw.line(win, (0, 0, 0), (150, 0), (150, 450))
        pygame.draw.line(win, (0, 0, 0), (0, 150), (450, 150))
        pygame.draw.line(win, (0, 0, 0), (0, 300), (450, 300))
        pygame.draw.line(win, (0, 0, 0), (300, 0), (300, 450))

    def draw_circle(self, pos):

        pygame.draw.circle(win, (0, 0, 0), center=pos, radius=50)

    def draw_krestiki(self, pos):

        pygame.draw.line(win, (0,0,0), (pos[0]-50, pos[1]-50), (pos[0]+50, pos[1]+50), 5)
        pygame.draw.line(win, (0,0,0), (pos[0]+50, pos[1]-50), (pos[0]-50, pos[1]+50), 5)


mouse = pygame.mouse.get_pos()
board = Board()
hod = 0
win.fill((255, 255, 255))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    mouse = pygame.mouse.get_pos()

    board.draw_line()
    if pygame.mouse.get_pressed()[0] and hod%2==0:
        hod += 1
        if 0 < mouse[0] < 150 and 0 < mouse[1] < 150:
            board.draw_circle((75, 75))
            pygame.time.delay(100)
        if 150 < mouse[0] < 300 and 0 < mouse[1] < 150:
            board.draw_circle((225, 75))
            pygame.time.delay(100)

        if 300 < mouse[0] < 450 and 0 < mouse[1] < 150:
            board.draw_circle((375, 75))
            pygame.time.delay(100)
        if 0 < mouse[0] < 150 and 150 < mouse[1] < 300:
            board.draw_circle((75, 225))
            pygame.time.delay(100)
        if 150 < mouse[0] < 300 and 150 < mouse[1] < 300:
            board.draw_circle((225, 225))
            pygame.time.delay(100)
        if 300 < mouse[0] < 450 and 150 < mouse[1] < 300:
            board.draw_circle((375, 225))
            pygame.time.delay(100)
        if 0 < mouse[0] < 150 and 300 < mouse[1] < 450:
            board.draw_circle((75, 375))
            pygame.time.delay(100)
        if 150 < mouse[0] < 300 and 300 < mouse[1] < 450:
            board.draw_circle((225, 375))
            pygame.time.delay(100)
        if 300 < mouse[0] < 450 and 300 < mouse[1] < 450:
            board.draw_circle((375, 375))
            pygame.time.delay(100)
    elif pygame.mouse.get_pressed()[0] and hod % 2 != 0:
        hod += 1
        if 0 < mouse[0] < 150 and 0 < mouse[1] < 150:
            board.draw_krestiki((75, 75))
            pygame.time.delay(100)
        if 150 < mouse[0] < 300 and 0 < mouse[1] < 150:
            board.draw_krestiki((225, 75))
            pygame.time.delay(100)
        if 300 < mouse[0] < 450 and 0 < mouse[1] < 150:
            board.draw_krestiki((375, 75))
            pygame.time.delay(100)
        if 0 < mouse[0] < 150 and 150 < mouse[1] < 300:
            board.draw_krestiki((75, 225))
            pygame.time.delay(100)
        if 150 < mouse[0] < 300 and 150 < mouse[1] < 300:
            board.draw_krestiki((225, 225))
            pygame.time.delay(100)
        if 300 < mouse[0] < 450 and 150 < mouse[1] < 300:
            board.draw_krestiki((375, 225))
            pygame.time.delay(100)
        if 0 < mouse[0] < 150 and 300 < mouse[1] < 450:
            board.draw_krestiki((75, 375))
            pygame.time.delay(100)
        if 150 < mouse[0] < 300 and 300 < mouse[1] < 450:
            board.draw_krestiki((225, 375))
            pygame.time.delay(100)
        if 300 < mouse[0] < 450 and 300 < mouse[1] < 450:
            board.draw_krestiki((375, 375))
            pygame.time.delay(100)



    pygame.display.update()
    pygame.time.delay(15)