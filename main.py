import pygame
import random
import math
from pygame import mixer


pygame.init()


screen = pygame.display.set_mode((800, 600))



#Title and Icon of game
pygame.display.set_caption("Spurious Aliens")
icon= pygame.image.load('logo.png')
pygame.display.set_icon(icon)

background = pygame.image.load('background image.jpg')

over_font = pygame.font.Font('font2.ttf', 64)


textX = 10
testY = 10


counter_score1=0
counter_score2=0

stopbots=False


playerImg = pygame.image.load('player big.png')
playerX = 370
playerY = 480
playerX_change = 0

mixer.music.load("background music.mp3")
mixer.music.play(-1)



enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
enemyX_speed=5
enemyY_speed=20
changeX= 0.001
changeY=0.001

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy medium.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 100))
    enemyX_change.append(enemyX_speed)
    enemyY_change.append(enemyY_speed)



explosionImg= pygame.image.load('explosion.png')



bulletImg = pygame.image.load('playerbullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 8
bullet_state = "ready"



#adding minibot1
miniImg=pygame.image.load('minibots.png')
miniX = 368
miniY= 380
minix_change=1


bulImg=pygame.image.load('botbullet.png')

bulX =336
bulY=380
bulx_change=0
buly_change=6
bul_state="ready"


miniImg2=pygame.image.load('minibots.png')
miniX2 = 400
miniY2= 380
minix2_change=1


bul2Img=pygame.image.load('botbullet.png')

bul2X =416
bul2Y=380
bul2x_change=0
bul2y_change=6
bul_state="ready"




score_value = 0
font = pygame.font.Font('font.otf', 32)



explosionImg= pygame.image.load('explosion.png')
explosion1X=0
explosion2X=0
explosionY=380


def player(x, y):
    screen.blit(playerImg, (x, y))



def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))



def minibot(x,y):

    screen.blit(miniImg,(x, y))


def minibullets(x,y):
    global bul_state
    bul_state="fire"
    screen.blit(bulImg,(x+16, y+10))


def minibot2(x,y):
    screen.blit(miniImg2,(x, y))



def minibullets2(x,y):
   
    screen.blit(bul2Img,(x+16, y+10))




def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY,dist):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < dist:
        return True
    else:
        return False



def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))



def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    mixer.music.stop()
    Gameover_Sound = mixer.Sound("gameover.wav")
    Gameover_Sound.play()

def explosion(x,y):
    screen.blit(explosionImg, (x + 16, y + 10))


def change():
    global changeX
    global changeY
    changeX+=0.0002
    changeY+=0.001




running = True
while running:

    
    screen.fill((255, 0, 255))

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2



            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    miniX+=minix_change
    
   
    if miniX<=0:
        miniX=0
        minix_change=1
    
    elif miniX>=336:
        miniX=336
        minix_change=-1




    miniX2+=minix2_change
    
    if miniX2>=736:
        miniX2=736
        minix2_change=-1
    elif miniX2<=400:
        miniX2=400
        minix2_change=1




    if bulY<=0:
        bulY=380
        bul_state="ready"
    
    if bul_state is "ready":
        bulX=miniX
    


    if bul2Y<=0:
        bul2Y=380
        bul_state="ready"


    if bul_state is "ready":
        bul2X=miniX2


    if stopbots==False:

        minibullets(bulX,bulY)
        bulY-=buly_change


        minibullets(bul2X,bul2Y)
        bul2Y-=bul2y_change



        minibot(miniX,miniY)
        minibot2(miniX2,miniY2)
        explosion1X=miniX

        explosion1X=miniX2
    else:

        explosion(explosion1X,explosionY)
        explosion(explosion2X,explosionY)




      
    






    

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736



    for i in range(num_of_enemies):


        if enemyY[i] > 430:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break



        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1 + changeX
            enemyY[i] += enemyY_change[i] + changeY
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1 - changeX
            enemyY[i] += enemyY_change[i] + changeY
        
        #Check if enemy reached the minibots
        if(enemyY[i]>365):
            stopbots=True


        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY,27)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            score_value += 1
            bulletY = 480
            bullet_state = "ready"
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)


        collision2 = isCollision(enemyX[i], enemyY[i], bulX, bulY,10)

        if collision2:
            counter_score1+=1
            if(counter_score1>10):
                score_value += 1
                counter_score1=0
                explosionSound = mixer.Sound("explosion.wav")
                explosionSound.play()
                bulY=380
                bul_state="ready"
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)

        collision3 = isCollision(enemyX[i], enemyY[i], bul2X, bul2Y,10)     
        if collision3:
            counter_score2+=1
            if(counter_score2>10):
                score_value += 1
                counter_score2=0
                explosionSound = mixer.Sound("explosion.wav")
                explosionSound. play()
                bul2Y=380
                bul2_state="ready"
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)


        enemy(enemyX[i], enemyY[i], i)

    collision4 = isCollision(miniX, miniY, bulletX, bulletY,27)
    collision5 = isCollision(miniX2, miniY2, bulletX, bulletY,27)
    
    if stopbots == False:
        if collision4 or collision5:
            score_value-=2
            bulletY=480
            bullet_state="ready"
            blooperSound = mixer.Sound("blooper.wav")
            blooperSound. play()

 
    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        


   
    change()
    

    show_score(textX, testY)
    player(playerX, playerY)
    pygame.display.update()
pygame.quit()