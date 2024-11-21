import pygame
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Lautobus")
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(GREEN)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
