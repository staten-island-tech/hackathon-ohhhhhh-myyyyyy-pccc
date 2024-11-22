import pygame
import random
import time

pygame.init()
pygame.mixer.init()

screen_height = 1000
screen_width = 800
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((255, 255, 255))

tile_width = 100
tile_height = 200
tile_speed = 5
tile_gap = 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TILE_COLOR = (0, 0, 255)

def reset_tiles():
    positions = []
    while len(positions) < 5:
        x = random.randint(0, screen_width - tile_width)
        if all(abs(x - pos) > tile_width + tile_gap for pos in positions):
            positions.append(x)
    return [{"x": pos, "y": -tile_height, "hold": random.choice([True, False]), "start_time": 0} for pos in positions]

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

def reset_tile_position(tile):
    x = random.randint(0, screen_width - tile_width)
    while any(abs(x - other["x"]) < tile_width + tile_gap for other in tiles):
        x = random.randint(0, screen_width - tile_width)
    tile["x"] = x
    tile["y"] = -tile_height
    tile["start_time"] = 0

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
                    if tile["hold"]:
                        tile["start_time"] = time.time()
                    else:
                        score += 1
                        tile["y"] = -tile_height

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for tile in tiles:
                if tile["hold"] and tile["start_time"] > 0:
                    if (time.time() - tile["start_time"]) >= 1.0:
                        score += 1
                        tile["y"] = -tile_height
                    tile["start_time"] = 0 

    for tile in tiles:
        tile["y"] += tile_speed

        if tile["y"] > screen_height:
            reset_tile_position(tile)

    draw_tiles()

    update_score(score)

    pygame.display.flip()

pygame.quit()