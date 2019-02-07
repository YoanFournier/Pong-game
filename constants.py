import pygame
pygame.init()

# -------------- Colors Constants --------------
FONT1 = pygame.font.Font('freesansbold.ttf', 10)
FONT2 = pygame.font.Font('freesansbold.ttf', 25)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

R = RED
G = GREEN
B = BLUE
W = WHITE

# -------------- Game Constants --------------
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
NORMAL = (5, 5)
HARD = (10, 7)
DIFFICULTY = NORMAL

FPS = 60

DISPLAY = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fps_clock = pygame.time.Clock()

# -------------- Walls Constants --------------
WALL_W = "w"
WALL_H = "h"

# -------------- Block Constants --------------
NUM_ROWS = 5
NUM_COLS = 6
BALL_NUM = 3
BLOCK_COLORS = (BLUE, GREEN, RED)
BLOCK_WIDTH = 50
BLOCK_HEIGHT = 30
BLOCK_BORDER = 0
assert (SCREEN_WIDTH / BLOCK_WIDTH % 2 == 0)

# -------------- Ball Constants --------------
BALL_RADIUS = 10
BALL_SPEED = DIFFICULTY[0]
BALL_START_SPEED = [0, BALL_SPEED]
assert (BALL_SPEED % 5 == 0)
BALL_START_POS = [150, 250]

# -------------- Player Constants --------------
PLAYER_SPEED = DIFFICULTY[1]
PLAYER_WIDTH = 60
PLAYER_HEIGHT = 10
PLAYER_Y = 550
PLAYER_X = 120