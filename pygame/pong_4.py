import pygame, math, random, time

def ballAnimation(ballspeedx, ballspeedy, ballradius):
    temp_score = score
    temp_life = life
    ball.x += ballspeedx
    ball.y += ballspeedy

    if ball.top <=0 or ball.bottom >= size[1]:
        ballspeedy *= -1
    
    if ball.right >= size[0] - ballradius:
        ballspeedx *= -1
    
    #Score
    if ball.left <= 0:
        temp_life = life - 1
        ball.x, ball.y = random.randint(40, size[0] - 40), random.randint(40, size[1] - 40)
    
    if ball.colliderect(player):
        ballspeedx *= -1
        temp_score = score + 1
    return ballspeedx, ballspeedy, temp_score, temp_life

def playerAnimation(lPadSpeed):
    player.y += lPadSpeed

    if player.top <= 0:
        player.top = 0 
    if player.bottom >= size[1]:
        player.bottom = size[1]



# -- Color 
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50, 255)
YELLOW = (255,255,0)
RED = (255,50,50)
DARKBLUE = (0,0, 150)

pygame.init()

size = (640, 400)
screen = pygame.display.set_mode(size)

surface = pygame.display.set_caption("Pong")

done = False
ballx = 320
bally = 200
ballradius = 20
ballspeedx = 5
ballspeedy = 5
pady = 200
lPadSpeed = 0
pad_width = 15
pad_length = 60
score = 0
life = 10
font = pygame.font.Font("freesansbold.ttf", 32)
score_coor = (500, 10)
life_coor = (500, 30)
player = pygame.Rect(0, pady, pad_width, pad_length)
ball = pygame.Rect(ballx, bally, ballradius, ballradius)


clock = pygame.time.Clock()
while not done:

    # --User Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                lPadSpeed = -5
            elif event.key == pygame.K_DOWN:
                lPadSpeed = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                lPadSpeed = 0
    

    #Logics
    ballspeedx, ballspeedy, score, life = ballAnimation(ballspeedx, ballspeedy, ballradius)
    playerAnimation(lPadSpeed)
    if life == 0 or score == 15:
        done = True

    screen.fill(BLACK)
    #Draw
    pygame.draw.rect(screen, WHITE, ball)
    pygame.draw.rect(screen, BLUE, player)
    scoretxt = font.render("Score: "+ str(score), True, WHITE)
    screen.blit(scoretxt, score_coor)
    lifetxt = font.render("life: "+ str(life), True, WHITE)
    screen.blit(lifetxt, life_coor)

    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)


pygame.quit()

