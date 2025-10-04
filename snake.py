import pygame
import time
import random

# Initialize
pygame.init()

# Screen settings
WIDTH = 600
HEIGHT = 400
CELL = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('🐍 Snake Game')

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 10

# Font
font = pygame.font.SysFont('Arial', 24)

def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], CELL, CELL])

def message(text, color, y_offset=0):
    msg = font.render(text, True, color)
    rect = msg.get_rect(center=(WIDTH//2, HEIGHT//2 + y_offset))
    screen.blit(msg, rect)

def game_loop():
    # Starting position
    x = WIDTH // 2
    y = HEIGHT // 2
    dx = 0
    dy = 0

    snake = []
    length = 1

    # Food
    food_x = round(random.randrange(0, WIDTH - CELL) / CELL) * CELL
    food_y = round(random.randrange(0, HEIGHT - CELL) / CELL) * CELL

    score = 0
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -CELL
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = CELL
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx = 0
                    dy = -CELL
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx = 0
                    dy = CELL

        # Move snake
        x += dx
        y += dy

        # Game over conditions
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_over = True
            break

        head = [x, y]
        snake.append(head)
        if len(snake) > length:
            snake.pop(0)

        # Self collision
        if head in snake[:-1]:
            game_over = True
            break

        # Food collision
        if x == food_x and y == food_y:
            length += 1
            score += 1
            food_x = round(random.randrange(0, WIDTH - CELL) / CELL) * CELL
            food_y = round(random.randrange(0, HEIGHT - CELL) / CELL) * CELL

        # Drawing
        screen.fill(BLACK)
        draw_snake(snake)
        pygame.draw.rect(screen, RED, [food_x, food_y, CELL, CELL])
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, [10, 10])
        pygame.display.update()

        clock.tick(FPS)

    # Game Over Screen
    screen.fill(BLACK)
    message("💀 Game Over!", RED, -20)
    message(f"Score: {score}", WHITE, 20)
    pygame.display.update()
    time.sleep(3)
    pygame.quit()

# Run
if __name__ == "__main__":
    game_loop()
