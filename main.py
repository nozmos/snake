import pygame

WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FPS = 60


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