import tkinter as tk
import pygame
pygame.init()

pygame.mixer.init()

pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1, 0.0)

click_sound = pygame.mixer.Sound("click_sound.wav")

def tiles(pianotiles):
    return tiles(pianotiles)

screen_height = 800
screen_width = 600
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((255, 255, 255))

tile_width = 100
tile_height = 200
tile_speed = 5
tile_gap = 150
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TILE_COLOR = (0, 0, 255)

tiles = [{"x": 100 + (i * (tile_width + tile_gap)), "y": 0} for i in range(5)]

def reset_tiles():
    return [{"x": 100 + (i * (tile_width + tile_gap)), "y": 0} for i in range(5)]

tiles = reset_tiles()

pygame.display.set_caption("Piano Tiles Game")
score = 0
font = pygame.font.Font(None, 36)

def update_score(score):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

def draw_tiles():
    for tile in tiles:
        pygame.draw.rect(screen, TILE_COLOR, (tile["x"], tile["y"], tile_width, tile_height))

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            for tile in tiles:
                if (tile["x"] <= mouse_x <= tile["x"] + tile_width) and (tile["y"] <= mouse_y <= tile["y"] + tile_height):
                    click_sound.play()  
                    score += 1  
                    tile["y"] = -tile_height  

    for tile in tiles:
        tile["y"] += tile_speed

        if tile["y"] > screen_height:
            tile["y"] = -tile_height  

    draw_tiles()

    update_score(score)

    pygame.display.flip()

pygame.quit()