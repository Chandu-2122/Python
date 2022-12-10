import math
import random
import pygame
from pygame import mixer
#initialize the pygame
pygame.init()

#create the screen\window
window=pygame.display.set_mode((800,500))



#set the title/caption and icon
pygame.display.set_caption("Space Game")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

#create the spaceship
spaceshipimg = pygame.image.load('spaceship.png')
spaceshipX = 350
spaceshipY = 400
spaceshipX_change=0

    
#create the enemy-meteor
meteorimg = []
meteorX = []
meteorY = []
meteorX_change = []
meteorY_change = []
no_of_meteors = 4
for i in range(no_of_meteors):
    meteorimg.append(pygame.image.load('meteor.png'))
    meteorX.append(random.randint(0,700))
    meteorY.append(random.randint(50,150))
    meteorX_change.append(4)
    meteorY_change.append(40)




#create the bullet
    #ready-the spaceship is ready to fire
    #fire-the bullets will be released from the spaceship
bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 400
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

#score
score_count = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

#Gameover
over_font = pygame.font.Font('freesansbold.ttf', 64)



def show_score(x,y):
    score = font.render("Score: " + str(score_count), True, (255,255,255))
    window.blit(score, (x,y))
def game_over():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    window.blit(over_text, (200, 250))
def spaceship(x,y):
    window.blit(spaceshipimg, (x,y))
def meteor(x,y,i):
    window.blit(meteorimg[i], (x,y))
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    window.blit(bulletimg, (x+16, y+10))

#bullet colliding with the meteor
def isCollision(meteorX, meteorY, bulletX, bulletY):
    distance = math.sqrt(math.pow(meteorX - bulletX, 2) + (math.pow(meteorY - bulletY, 2)))
    if distance <27:
        return True
    else:
        return False

#create game loop
running=True
while running:

    #for continuous movement
    #spaceshipX +=0.1
    #spaceshipY -=0.1
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running  = False

        #if keystroke is pressed check whether its right or left or up or down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                spaceshipX_change -= 2
            if event.key == pygame.K_RIGHT:
                spaceshipX_change += 2
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletsound = mixer.sound("laser.wav")
                    bulletsound.play()
                    #get the current x-coordinate of the spaceship
                    bulletX = spaceshipX
                    fire_bullet(bulletX, bulletY)
                    
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                spaceshipX_change=0
    
    spaceshipX += spaceshipX_change
    if spaceshipX<=0:
        spaceshipX = 0
    elif spaceshipX >=700:
        spaceshipX = 700
    # Enemy Movement
    for i in range(no_of_meteors):

        # Game Over
        if meteorY[i] > 440:
            for j in range(no_of_meteors):
                meteorY[j] = 2000
            game_over()
            break

        meteorX[i] += meteorX_change[i]
        if meteorX[i] <= 0:
            meteorX_change[i] = 1
            meteorY[i] += meteorY_change[i]
        elif meteorX[i] >= 736:
            meteorX_change[i] = -1
            meteorY[i] += meteorY_change[i]

        # Collision
        collision = isCollision(meteorX[i], meteorY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_count += 1
            meteorX[i] = random.randint(0, 736)
            meteorY[i] = random.randint(50, 150)

        meteor(meteorX[i], meteorY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    spaceship(spaceshipX, spaceshipY)
    show_score(textX, textY)
    pygame.display.update()
       
    
pygame.quit()
