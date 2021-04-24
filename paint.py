import pygame

win = pygame.display.set_mode((700, 700))
bg_color = (255, 255, 255)
win.fill(bg_color)
pygame.display.set_caption("paint")
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pygame.mouse.get_pressed()[0]: # hold left mb to draw
            pos = pygame.mouse.get_pos() 
            pygame.draw.circle(win, (200, 0, 140), pos, 20)
        if event.type == pygame.KEYDOWN: # space to clear screen
            if event.key == pygame.K_SPACE:
                win.fill(bg_color)
    pygame.display.update()
