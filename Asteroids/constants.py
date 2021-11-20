import pygame
import math

pygame.font.init()

if __name__ == "__main__":
     print (pygame.font.get_fonts())

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# display
DISPLAY_WIDTH, DISPLAY_HEIGHT = 1200, 800
FPS = 30


# ship
SHIP_VERTECIES = [
     (0, -20),
     (10, 10),
     (0, 5),
     (-10, 10)
]
SHIP_LINE_WIDTH = 2

SHIP_SIZE = 15

PUSH_FORCE = [0, -0.5]
DRAG_FORCE = 0.01

ROTATION_FORCE = 0.05
ROTATION_DRAG = 3

RECOIL_FORCE = 0.1


# rocks
ROCK_SIZE_MIN = 70
ROCK_SIZE_MAX = 100

ROCK_SIZE_LIMIT = 15

ROCK_WIDTH = 2
ROCK_SPEED = 2

ROCK_AMOUNT = 8

ROCK_INIT_ANGLE_THRESHOLD = math.radians(30)

ROCK_SIZE_DIVISION_RANGE = (1.5, 2)
ROCK_SIZE_DIVISION_AMOUNT = 2
ROCK_ANGLE_DIVISION_RANGE = math.radians(180)


ROCK_POINTS_MULTIPLIER = 50000


# bullets
BULLET_SIZE = 3
BULLET_SPEED = 30
BULLET_LIFESPAN = 30


# ui
COOLDOWN_TIMER_LOCATION = [50, 50]
COOLDOWN_TIMER_SIZE = [20, 100]
COOLDOWN_TIMER_WIDTH = 2

SCORE_FONT = pygame.font.Font("freesansbold.ttf", 32)
SCORE_LOCATION = [DISPLAY_WIDTH-50, 50]

GAME_OVER_FONT = pygame.font.Font("freesansbold.ttf", 124)
GAME_OVER_LOCATION = [DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2-50]
GAME_OVER_TEXT = "GAME OVER"

MESSAGE_FONT = pygame.font.Font("freesansbold.ttf", 16)
MESSAGE_LOCATION = [GAME_OVER_LOCATION[0], GAME_OVER_LOCATION[1]+130]
MESSAGE_TEXT = "PRESS R TO RESTART OR PRESS BACKSPACE TO QUIT"


# variations
GUN_COOLDOWN = 0.5
END_COOLDOWN = 2