import pygame
import time
import random

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Dodgey Space")
# This function sets up a graphical window with the specified width and height.

pygame.display.set_caption("Dodgey Space")
# is a function call that sets the caption of the Pygame window to "Dodgey Space."

BG = pygame.transform.scale(pygame.image.load("6497836.jpg"), (WIDTH, HEIGHT))
# This is to load the image background of my choice
# Scaling the image pygame.transform.scale

custom_image = pygame.image.load("IMG_0207-2.png")

PLAYER_WIDTH = 150
PLAYER_HEIGHT = 175

PLAYER_VEL = 6


def draw(player):
    WIN.blit(BG, (0, 0))
    WIN.blit(custom_image, (player.x, player.y))
    # Blit is a special method when you want to draw an image
   # pygame.draw.rect(WIN, "yellow",player)
    pygame.display.update()


# Creating Main Game Loop, Runs while game runs
def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    # create a clock in order to have it run at a constant time on every computer

    while run:
        clock.tick(60)
        # 60 is the fPS you would like it to run in

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(player)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_UP] and player.y - PLAYER_VEL >= 0:
            player.y -= PLAYER_VEL
        if keys[pygame.K_DOWN] and player.y + PLAYER_VEL + player.height <= HEIGHT:
            player.y += PLAYER_VEL

    pygame.quit()


# calling main function

if __name__ == '__main__':
    main()