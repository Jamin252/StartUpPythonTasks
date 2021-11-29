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
size = (640, 700)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
surface = pygame.display.set_caption("My window")
# -- Exit game flag set to False
done = False
sun_x = 40
sun_y = 100
sun_flag = True
# -- Manages how fast screen refresh
clock = pygame.time.Clock()
xspeed = 5

### -- Game loop
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #Endif
    #Next event
    #--Game logic goes after this comment
    if sun_x >= size[0] + 60 or sun_x <= -60:
        xspeed *= -1
    sun_x += xspeed
    sun_y = -math.sqrt(abs((size[0]/2 + 60) ** 2 - (sun_x - size[0] / 2) ** 2)) + size[1] / 2
    # -- Screen background is BLACK
    screen.fill(BLACK)

    # -- Draw here
    # screen, [red, blue, green], (left, top, width, height))
    pygame.draw.rect(screen,BLUE,(220,165,200,150))

    # circle(surface, color, center, radius, width)
    pygame.draw.circle(screen,YELLOW,(sun_x,sun_y),40,0)

    pygame.draw.rect(screen,WHITE, (250, 185, 30, 30))

    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)
#Endwhile
pygame.quit()