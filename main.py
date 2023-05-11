import pygame, sys, random


def ball_animation():
    global ball_speed_x, ball_speed_y #really only a good solution for small programs - for larger applications use return statements or classes
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    #Use >= or <=, not == - if ball is at 955px and the next frame it is at 962px, it will 'bounce' instead of continuing because it never reaches 960px
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))
    

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

ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7
player_speed = 0
opponent_speed = 7

while True:
    # Handling input
    for event in pygame.event.get():
        #Exiting the screen
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -=7
            if event.key == pygame.K_UP:
                player_speed += 7


    ball_animation()
    player_animation()
    opponent_ai()


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