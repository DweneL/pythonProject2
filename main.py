import pygame
import time
import random
pygame.font.init()
# initialize font (1)

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
PLAYER_HEIGHT = 65

PLAYER_VEL = 6
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 6

FONT = pygame.font.SysFont("comicsans", 25)
# create font object here (2)
def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))
    WIN.blit(custom_image, (player.x, player.y))
    # Blit is a special method when you want to draw an image
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    # pass the string and text we want to render on the screen
    # round time to nearest seconds
    # 1: makes text better
    # color
    WIN.blit(time_text, (10,10))
    # showing this up the screen

   # pygame.draw.rect(WIN, "yellow",player)

    for star in stars:
        pygame.draw.rect(WIN, "white", star)


    pygame.display.update()


# Creating Main Game Loop, Runs while game runs
def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    # create a clock in order to have it run at a constant time on every computer

    start_time = time.time()
    # going to give us the current time when game started
    elapsed_time = 0
    #

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False

    while run:
        star_count += clock.tick(60)
        # 60 is the fPS you would like it to run in
        elapsed_time = time.time() - start_time
        # Storing the time we started the while loop, every time we iteratre we get current time and subtract from star
        # time
        # which gives us number of seconds that has elapsed

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)


            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(player, elapsed_time, stars)
        # now we have elapsed time we pass it to our draw function

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_UP] and player.y - PLAYER_VEL >= 0:
            player.y -= PLAYER_VEL
        if keys[pygame.K_DOWN] and player.y + PLAYER_VEL + player.height <= HEIGHT:
            player.y += PLAYER_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break


    pygame.quit()


# calling main function

if __name__ == '__main__':
    main()