import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock
clock = pygame.time.Clock()

def draw_snake(snake_body):
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

def main():
    snake_pos = [100, 50]
    snake_body = [[100, 50], [80, 50], [60, 50]]
    direction = "RIGHT"
    change_to = direction

    food_pos = [random.randrange(1, (WIDTH // CELL_SIZE)) * CELL_SIZE,
                random.randrange(1, (HEIGHT // CELL_SIZE)) * CELL_SIZE]
    food_spawn = True
    score = 0

    def show_score():
        font = pygame.font.SysFont("arial", 24)
        score_surface = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_surface, (10, 10))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    change_to = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    change_to = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    change_to = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    change_to = "RIGHT"

        direction = change_to

        if direction == "UP":
            snake_pos[1] -= CELL_SIZE
        if direction == "DOWN":
            snake_pos[1] += CELL_SIZE
        if direction == "LEFT":
            snake_pos[0] -= CELL_SIZE
        if direction == "RIGHT":
            snake_pos[0] += CELL_SIZE

        snake_body.insert(0, list(snake_pos))
        if snake_pos == food_pos:
            score += 1
            food_spawn = False
        else:
            snake_body.pop()

        if not food_spawn:
            food_pos = [random.randrange(1, (WIDTH // CELL_SIZE)) * CELL_SIZE,
                        random.randrange(1, (HEIGHT // CELL_SIZE)) * CELL_SIZE]
        food_spawn = True

        screen.fill(BLACK)
        draw_snake(snake_body)
        pygame.draw.rect(screen, RED, (food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))
        show_score()

        # Game over conditions
        if (snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
            snake_pos[1] < 0 or snake_pos[1] >= HEIGHT or
            snake_pos in snake_body[1:]):
            pygame.quit()
            sys.exit()

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
