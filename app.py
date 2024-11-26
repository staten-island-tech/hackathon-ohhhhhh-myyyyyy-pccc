import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 20
BALL_SIZE = 20
ball_speed_x, ball_speed_y = 20, 20
paddle1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
        paddle2.y += PADDLE_SPEED
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    pygame.display.flip()
    pygame.time.Clock().tick(60)
"""# Copilot Coding Diary
Project_Name=("random mobile game idk")
11/21/24
## 1. **Task/Problem Description**
Why doesn't the module pygame work?
## 2. **Initial Approach/Code**
Describe the initial approach you took to solving the problem. If you started writing code, include it here.
```python
import pygame
```
I really didn't know what I could do to make import pygame work. I already have it downloaded, so why does it say that there isn't a module named 'pygame'?
## 3. **Interaction with Copilot**
### Questions/Requests to Copilot
Write down the questions or requests you made to Copilot.
Why doesn't importing pygame into my python code work?
## 4. **Copilot's Suggestions/Code Changes**
Record the code or suggestions Copilot provided. Include any changes or improvements Copilot suggested and how it influenced your approach.
```python
pip show pygame
pip install pygame
which python
import pygame
print(pygame.__version__)
```
COPILOT suggested checking to make sure that it was installed. That part might've been pretty useless, but they did give me a source link to a website which told me to run the code in the dedicated terminal instead of the interactive window. 
## 5. **Reflection on Changes**
Reflect on the changes made to your code after Copilot's suggestions.
COPILOT was very helpful in helping me figure out how I could make import python work, despite not telling me how to do so directly.
None of my code needed to be changed; it was just a minor change from running the code in the interactive window to running the code in the dedicated terminal.
## 6. **Testing and Results**
After making the changes, did you test your code? What were the results?
There weren't really any tests to run, and my code did work as intended in the end!
There were no problems after asking copilot.
## 7. **What Did You Learn?**
In this section, reflect on what you learned from this coding session. Did you gain any new insights, or were there areas you still struggled with? 
I learned how to properly install and utilize pygame😀.
11/25/24
## 1. **Task/Problem Description**
How do I make a screen display using pygame?
## 2. **Initial Approach/Code**
I took no initial approach, for this is my first time working with pygame and I honestly don't know a single thing about it.
```python
import pygame
print(pygame.__version__)
pygame.init()
```
I really didn't know what I could do to implement a screen display, as I'm not exactly familiar with pygame and what it can do.
## 3. **Interaction with Copilot**
### Questions/Requests to Copilot
Write down the questions or requests you made to Copilot.
How could one make a screen display in python using pygame?
## 4. **Copilot's Suggestions/Code Changes**
Record the code or suggestions Copilot provided. Include any changes or improvements Copilot suggested and how it influenced your approach.
```python
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("lautobus")
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
```
## 5. **Reflection on Changes**
Reflect on the changes made to your code after Copilot's suggestions.
COPILOT was very helpful in creating a display screen where I will be able to add my own things in.
## 6. **Testing and Results**
After making the changes, did you test your code? What were the results?
After running the code in the terminal, it worked! There was now a screen display.
## 7. **What Did You Learn?**
In this section, reflect on what you learned from this coding session. Did you gain any new insights, or were there areas you still struggled with? 
I was educated on how pygame can be utilized to create a screen display😀.
11/26/24
## 1. **Task/Problem Description**
How do I make a screen display using pygame?
## 2. **Initial Approach/Code**
I took no initial approach, for this is my first time working with pygame and I honestly don't know a single thing about it.
```python
import pygame
print(pygame.__version__)
pygame.init()
```
I really didn't know what I could do to implement a screen display, as I'm not exactly familiar with pygame and what it can do.
## 3. **Interaction with Copilot**
### Questions/Requests to Copilot
Write down the questions or requests you made to Copilot.
How could one make a screen display in python using pygame?
## 4. **Copilot's Suggestions/Code Changes**
Record the code or suggestions Copilot provided. Include any changes or improvements Copilot suggested and how it influenced your approach.
```python
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("lautobus")
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
```
## 5. **Reflection on Changes**
Reflect on the changes made to your code after Copilot's suggestions.
COPILOT was very helpful in creating a display screen where I will be able to add my own things in.
## 6. **Testing and Results**
After making the changes, did you test your code? What were the results?
After running the code in the terminal, it worked! There was now a screen display.
## 7. **What Did You Learn?**
In this section, reflect on what you learned from this coding session. Did you gain any new insights, or were there areas you still struggled with? 
I was educated on how pygame can be utilized to create a screen display😀.
"""