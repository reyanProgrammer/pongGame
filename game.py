import pygame
import sys
import random

"""© reyan mehmood All right reserved"""
# general setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
ScreenWidth = 1200
ScreenHeight = 700
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption('Pong')

# shapes
ball = pygame.Rect(ScreenWidth / 2 - 15, ScreenWidth / 2 - 15, 30, 30)
player = pygame.Rect(ScreenWidth - 20, ScreenHeight / 2 - 70, 10, 140)
opponent = pygame.Rect(10, ScreenHeight / 2 - 70, 10, 140)

# colors
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

# ball speed
ball_x_speed = 7 * random.choice((1, -1))
ball_y_speed = 7 * random.choice((1, -1))

player_speed = 0

opponent_speed = 7


def ball_move():
    global ball_x_speed, ball_y_speed
    if ball.top <= 0 or ball.bottom >= ScreenHeight:
        ball_y_speed *= -1
    if ball.left <= 0 or ball.right >= ScreenWidth:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_x_speed *= -1


def player_animation():
    if player.top <= 0:
        player.top = 0
    if player.bottom >= ScreenHeight:
        player.bottom = ScreenHeight
    player.y += player_speed


def opponentanimation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= ScreenHeight:
        opponent.bottom = ScreenHeight


def ball_restart():
    global ball_x_speed, ball_y_speed
    ball.center = (ScreenWidth / 2, ScreenHeight / 2)
    ball_y_speed *= random.choice((1, -1))
    ball_x_speed *= random.choice((1, -1))


while True:

    # handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    # Visual
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (ScreenWidth / 2, 0), (ScreenWidth / 2, ScreenHeight))

    ball.x += ball_x_speed
    ball.y += ball_y_speed
    ball_move()
    player_animation()
    opponentanimation()

    # updating the window
    pygame.display.flip()
    clock.tick(60)
