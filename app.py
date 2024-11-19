import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
TILE_WIDTH = 100
TILE_HEIGHT = 150
TILE_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)
WHITE = (255, 255, 255)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Piano Tiles')

# Load font
font = pygame.font.SysFont(None, 55)

# Define the Tile class
class Tile:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TILE_WIDTH, TILE_HEIGHT)
        self.color = TILE_COLOR

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, speed):
        self.rect.y += speed

# Main game loop
def game():
    clock = pygame.time.Clock()
    tiles = [Tile(x, -TILE_HEIGHT) for x in range(0, SCREEN_WIDTH, TILE_WIDTH)]
    speed = 5
    score = 0
    running = True

    while running:
        screen.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                if key in ['a', 's', 'd', 'f']:
                    for tile in tiles:
                        if tile.rect.collidepoint((tiles.index(tile) * TILE_WIDTH + TILE_WIDTH / 2, SCREEN_HEIGHT - TILE_HEIGHT / 2)):
                            tiles.remove(tile)
                            score += 1

        for tile in tiles:
            tile.move(speed)
            if tile.rect.top > SCREEN_HEIGHT:
                tiles.remove(tile)
                tiles.append(Tile(random.choice([0, TILE_WIDTH, 2 * TILE_WIDTH, 3 * TILE_WIDTH]), -TILE_HEIGHT))
            tile.draw(screen)

        score_text = font.render('Score: ' + str(score), True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# Run the game
game()
