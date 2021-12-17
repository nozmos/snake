import pygame

WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FPS = 60

GRID_WIDTH, GRID_HEIGHT = 18, 18
GRID_SIZE = 50


class Snake():
  def __init__(self) -> None:
    self.body = [(9, 9), (8, 9), (7, 9)]
    self.direction = 0
    self.speed = 1


def create_grid(width, height):
  grid = [[WHITE for x in range(width)] for y in range(height)]

  return grid


def get_grid_rect(grid_x, grid_y):
  rect = pygame.Rect(grid_x * GRID_SIZE, grid_y * GRID_SIZE, GRID_SIZE, GRID_SIZE)

  return rect


def draw_snake(surface, snake: Snake):
  for piece in snake.body:
    pygame.draw.rect(surface, BLACK, get_grid_rect(piece[0], piece[1]))


def draw_window():
  WIN.blit(WHITE, (0, 0))

  pygame.display.update()


def main():
  clock = pygame.time.Clock()
  run = True

  while run:
    clock.tick(FPS)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        pygame.quit()
  
if __name__ == "__main__":
  main()