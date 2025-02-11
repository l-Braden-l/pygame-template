# --- pygame template 1.0 --- #

# -- import the pygame and system modules -- #
import pygame 
import sys
# -- Constants -- #

WIDTH = 800
HEIGHT = 600 
TITLE = "My Pygame Template"

FPS = 60 #frames a second

WHITE = (255,255,255) #RGB triplet saved in a tuple



# -- Initialize Pygame  -- #
pygame.init()

# -- Screen Setup -- #
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# -- Clock Setup -- # 
clock = pygame.time.Clock()

# -- Game Loop -- # 
running = True 
while running:
    # -- Listen for and handle events -- # 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #QUIT in uppercase 
            running = False 
    # -- Game Logic -- # 
    # -- This is where to put game logic -- # 
        
    # -- Draw -- # 
    screen.fill(WHITE) #fill screen with color

    # -- This is where to draw your game objects -- #

    pygame.display.flip() #Update display

    # -- Limit frames per second (FPS) -- #
    clock.tick(FPS)

# -- Quit Pygame and exit system module -- #
pygame.quit()
sys.exit()





