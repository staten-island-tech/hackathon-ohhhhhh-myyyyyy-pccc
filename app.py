import pygame
print(pygame.__version__)
pygame.init()
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
"""# ChatGPT Coding Diary
Project_Name=("random mobile game idk")
11/21/24
## 1. **Task/Problem Description**
Why doesn't the module pygame work?
> I need to write a program that sorts a list of integers in ascending order.
## 2. **Initial Approach/Code**
Describe the initial approach you took to solving the problem. If you started writing code, include it here.
```python
import pygame
```
I really didn't know what I could do to make import pygame work. I already have it downloaded, so why does it say that there isn't a module named 'pygame'?
## 3. **Interaction with ChatGPT**
### Questions/Requests to ChatGPT
Write down the questions or requests you made to ChatGPT.
Why doesn't importing pygame into my python code work?
## 4. **ChatGPT's Suggestions/Code Changes**
Record the code or suggestions ChatGPT provided. Include any changes or improvements ChatGPT suggested and how it influenced your approach.
```python
pip show pygame
pip install pygame
which python
import pygame
print(pygame.__version__)
```
COPILOT suggested checking for
## 5. **Reflection on Changes**
Reflect on the changes made to your code after ChatGPT's suggestions. Answer the following questions:
- Why do you think ChatGPT's suggestions are helpful or relevant?
- Did the suggestions improve your code? How?
- Did you understand why the changes were made, or are you still uncertain about some parts?
Example
> ChatGPT recommended using a more efficient sorting algorithm like quicksort. I think this will improve the runtime for large inputs, but I need to review the algorithm's complexity to fully understand its advantages.
## 6. **Testing and Results**
After making the changes, did you test your code? What were the results?
- Did you run any tests (e.g., unit tests, edge cases)?
- Did the code work as expected after incorporating ChatGPT's changes?
```python
# Example: Testing the updated sorting function
numbers = [5, 2, 9, 1]
print(optimized_sort(numbers))  # Expected output: [1, 2, 5, 9]
```
- Did you encounter any bugs or issues during testing?
## 7. **What Did You Learn?**
In this section, reflect on what you learned from this coding session. Did you gain any new insights, or were there areas you still struggled with? 
Example:
> I learned how to implement an efficient sorting algorithm, and I now understand the time complexity differences between various sorting methods."""
