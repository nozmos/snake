import pygame, random
import numpy as np

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

WHITE = (255, 255, 255)
LIGHTGREY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FPS = 60

GRID_WIDTH, GRID_HEIGHT = 16, 16
GRID_SIZE = 50

RIGHT = [1, 0]
UP = [0, -1]
LEFT = [-1, 0]
DOWN = [0, 1]

points = 0
apples = [[5, 5]]


class Snake():
  def __init__(self) -> None:
    self.body = [[9, 9], [8, 9], [7, 9]]
    self.direction = RIGHT
    self.delay = 500
  
  def move(self, grow=False) -> None:
    new_body = []
    head = self.body[0]

    for i in range(len(self.body)):
      if self.body[i] == head:
        new_body.append(list(np.add(head, self.direction)))
      else:
        new_body.append(self.body[i-1])
    
    self.body = new_body
    
    if self.body[0] in apples:
      global points
      points += 1
      print("apple eaten")

      new_body.append(self.body[-1])
      apples.remove(self.body[0])

      create_apple(random.choice(range(GRID_WIDTH)), random.choice(range(GRID_HEIGHT)))


def create_grid(width, height):
  grid = [[WHITE for x in range(width)] for y in range(height)]

  return grid


def create_apple(grid_x, grid_y):
  apples.append([grid_x, grid_y])


def get_grid_rect(grid_x, grid_y):
  rect = pygame.Rect(grid_x * GRID_SIZE, grid_y * GRID_SIZE, GRID_SIZE, GRID_SIZE)

  return rect


def draw_snake(surface, snake: Snake):
  for piece in snake.body:
    pygame.draw.rect(surface, BLACK, get_grid_rect(piece[0], piece[1]))


def draw_apples(surface, apples):
  for apple in apples:
    pygame.draw.rect(surface, RED, get_grid_rect(apple[0], apple[1]))


def draw_window(snake, apples):
  WIN.fill(LIGHTGREY)

  draw_apples(WIN, apples)
  draw_snake(WIN, snake)

  pygame.display.update()


def main():
  clock = pygame.time.Clock()
  run = True

  player = Snake()

  MOVE_SNAKE = pygame.USEREVENT + 1
  pygame.time.set_timer(MOVE_SNAKE, player.delay)

  while run:
    clock.tick(FPS)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        pygame.quit()
      
      if event.type == pygame.KEYDOWN:
        new_direction = [0, 0]
        if event.key == pygame.K_RIGHT and player.direction != LEFT:
          new_direction = RIGHT
        if event.key == pygame.K_UP and player.direction != DOWN:
          new_direction = UP
        if event.key == pygame.K_LEFT and player.direction != RIGHT:
          new_direction = LEFT
        if event.key == pygame.K_DOWN and player.direction != UP:
          new_direction = DOWN
      
      if event.type == MOVE_SNAKE:
        player.direction = new_direction
        player.move()
    
    draw_window(player, apples)
  
  pygame.quit()
  
if __name__ == "__main__":
  main()