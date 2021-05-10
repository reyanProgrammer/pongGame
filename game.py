import pygame, sys

# general setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
ScreenWidth = 800
ScreenHeight = 400
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption('Pong')

# shapes
ball = pygame.Rect(ScreenWidth / 2 - 15, ScreenWidth / 2 - 15, 30, 30)
player = pygame.Rect(ScreenWidth - 20, ScreenHeight / 2 - 70, 10, 140)
opponent = pygame.Rect(10, ScreenHeight/2 - 70, 10, 140)

while True:

    # handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # updating the window

    pygame.display.flip()
    clock.tick(60)
