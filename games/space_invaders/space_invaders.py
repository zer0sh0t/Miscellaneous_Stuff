import math
import random

import pygame
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((800, 600))

background = pygame.image.load("assets/background.png")

mixer.music.load("assets/bgmusic for SI.wav")
mixer.music.play(-1)

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("assets/alien.png")
pygame.display.set_icon(icon)

player_img = pygame.image.load("assets/spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0

enemy_img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 5

for i in range(no_of_enemies):
    enemy_img.append(pygame.image.load("assets/ufo.png"))
    enemyX.append(random.randint(50, 700))
    enemyY.append(random.randint(50, 200))

    enemyX_change.append(3)
    enemyY_change.append(20)

bullet_img = pygame.image.load("assets/bullet.png")
bulletX = 0
bulletY = playerY
bulletY_change = 9
bullet_state = "ready"

score_val = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

over_text = pygame.font.Font("freesansbold.ttf", 80)


def game_over_text(x, y):
    game_over = over_text.render("GAME OVER", True, (255, 0, 0))
    screen.blit(game_over, (x, y))


def show_score(x, y):
    score = font.render("Score : " + str(score_val), True, (255, 102, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


def fire_bullet(x, y):
    global bullet_state

    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y - 20))


def is_collison(a, b, c, d):
    distance = math.sqrt((math.pow(a - c, 2)) + (math.pow(b - d, 2)))
    if distance < 27:
        return True
    else:
        return False


running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for i in range(no_of_enemies):

        if enemyY[i] >= playerY:
            for j in range(no_of_enemies):
                enemyY[j] = 40000
            game_over_text(170, 250)

        enemyX[i] += enemyX_change[i]
        if enemyX[i] >= 736:
            for j in range(no_of_enemies):
                enemyX_change[j] *= -1
                enemyY[j] += enemyY_change[j]

        if enemyX[i] <= 0:
            for j in range(no_of_enemies):
                enemyX_change[j] *= -1
                enemyY[j] += enemyY_change[j]

        collision = is_collison(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision is True:
            explosion_sound = mixer.Sound("assets/explosion.wav")
            explosion_sound.play()

            enemyX[i] = random.randint(50, 700)
            enemyY[i] = random.randint(50, 200)
            score_val += 10
            bullet_state = "ready"
            bulletY = playerY

        enemy(enemyX[i], enemyY[i], i)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change -= 7
            if event.key == pygame.K_d:
                playerX_change += 7
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound("assets/laser.wav")
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

    playerX += playerX_change
    if playerX > 736:
        playerX = 736
    if playerX < 0:
        playerX = 0

    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"

    if bullet_state == "fire":
        bulletY -= bulletY_change
        fire_bullet(bulletX, bulletY)

    player(playerX, playerY)
    show_score(textX, textX)
    pygame.display.update()
