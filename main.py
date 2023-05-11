import pygame, sys

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

#Game Rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 -15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10,140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Visuals
    #Beware of order first element drawn at bottom of the frame, last eliment at the top (z-index)
    #fills object with a color
    screen.fill(bg_color)
    #draws object(where to draw, color, what object)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    #anti-alias line(surface to draw on, color, tuple with start point, tuple with end point)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))
    # Updating the window
    pygame.display.flip()
    clock.tick(60)