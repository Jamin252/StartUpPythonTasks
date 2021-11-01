import pygame, math
# --Global Constant

# -- Color 
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50, 255)
YELLOW = (255,255,0)
RED = (255,50,50)
DARKBLUE = (0,0, 150)

# -- Initialize pygame
pygame.init()

# -- Blank Screen
size = (640, 400)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
surface = pygame.display.set_caption("Pong")
# -- Exit game flag set to False
done = False
sun_x = 40
sun_y = 100
sun_flag = True
ball_xflag = True
ball_yflag = True
ballWidth = 20
x_val = 150
y_val = 200
x_direction = 5
y_direction = 5
pad_width = 15
pad_length = 60
lPadSpeed = 0
lPady = size[1] // 2
# -- Manages how fast screen refresh
clock = pygame.time.Clock()

### -- Game loop
while not done:
    # -- User input and controls
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

    """ if keys[pygame.K_UP]:
        lPady -= 5
    if keys[pygame.K_DOWN]:
        lPady += 5"""
        #Endif
    #Next event
    #--Game logic goes after this comment
    lPady += lPadSpeed
    if x_val >= size[0] -20:
        ball_xflag = False
    elif x_val < 0:
        ball_xflag = True
    if ball_xflag:
        x_val += x_direction
    else:
        x_val -= x_direction
    if y_val <= 0:
        ball_yflag = True
    elif y_val >= size[1] - 20:
        ball_yflag = False
    if ball_yflag:
        y_val += y_direction
    else:
        y_val -= y_direction

    # -- Screen background is BLACK
    screen.fill(BLACK)

    # -- Draw here
    # screen, [red, blue, green], (left, top, width, height))
    #BALL
    pygame.draw.rect(screen,BLUE,(x_val, y_val,ballWidth,ballWidth))
    pygame.draw.rect(screen,WHITE, (0, lPady,  pad_width, pad_length))
    

    # circle(surface, color, center, radius, width)

    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)
    if sun_x > size[0] + 40 or sun_x < -40:
        screen.fill(DARKBLUE)
        pygame.display.update()
        pygame.time.delay(100)
#Endwhile
pygame.quit()