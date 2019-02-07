"""
ponggame.py
Created by @Yoan Fournier
11/02/18
"""

import sys
from pygame.locals import *

from animations import*
from player import *
from ball import*
from block import*
import maps


# -------------- Choosing Map --------------
MAP = maps.MAP2


# -------------- Check win or loose --------------
def check_win():
    """
    Checks if the player destroyed all the blocks
    :return: boolean
    """
    if len(Block.BLOCKS) == 0:
        return True
    else:
        return False


def check_lose(ball_num):
    """
    Check if the player used all the balls
    :param ball_num: number of balls (int)
    :return: None
    """
    if ball_num == 0:
        return True
    else:
        return False


# -------------- Main Function --------------
def main_fct():
    """
    Main function of the game
    :return: None
    """
    # -------------- Display variables --------------
    pygame.display.set_caption("Pong Game")

    # -------------- Object variables --------------
    BLOCKS = create_blocks(MAP)

    Ball.BALLS_LEFT = BALL_NUM

    ball = Ball(WHITE, BALL_RADIUS, BALL_START_POS, BALL_START_SPEED)

    player1 = Player(WHITE, PLAYER_WIDTH, PLAYER_HEIGHT, [PLAYER_X, PLAYER_Y])

    # -------------- Loop variables --------------
    pause = False

    intro = True

    # -------------- Main loop --------------
    while True:

        # -------------- Intro loop --------------
        while intro:
            intro_screen()
            for event in pygame.event.get():
                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        intro = False
                    if event.key == K_r:
                        Block.BLOCKS = []
                        main_fct()
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

        # -------------- Pause loop --------------
        pause_screen()
        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    pause = False
                if event.key == K_r:
                    Block.BLOCKS = []
                    main_fct()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # -------------- Game loop --------------
        while not pause:

            # -------------- Checks if the ball falls --------------
            ball.check_ball_fall(player1)

            # -------------- Check collisions --------------
            ball.check_wall_collision(WALL_H)

            ball.check_wall_collision(WALL_W)

            ball.check_player_collision(player1)

            ball.check_block_collision(BLOCKS)

            # -------------- Event control --------------
            for event in pygame.event.get():
                if event.type == KEYUP:
                    if event.key == K_d:
                        player1.vx = 0
                    if event.key == K_a:
                        player1.vx = 0
                    if event.key == K_SPACE:
                        pause = True
                    if event.key == K_r:
                        Block.BLOCKS = []
                        main_fct()
                if event.type == KEYDOWN:
                    if event.key == K_d:
                        player1.vx = PLAYER_SPEED
                    if event.key == K_a:
                        player1.vx = -PLAYER_SPEED
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # -------------- Limiting the players movement --------------
            if player1.x <= 0:
                player1.x += PLAYER_SPEED

            if player1.x + player1.width >= SCREEN_WIDTH:
                player1.x -= PLAYER_SPEED

            # -------------- Calculating new positions --------------
            player1.new_pos()

            ball.new_pos()

            # -------------- Creating images --------------
            DISPLAY.fill(BLACK)

            for block in BLOCKS:
                pygame.draw.rect(DISPLAY, block.color, (block.x, block.y, BLOCK_WIDTH, BLOCK_HEIGHT), BLOCK_BORDER)

            pygame.draw.rect(DISPLAY, player1.color, [player1.x, player1.y, player1.width, player1.height])

            pygame.draw.circle(DISPLAY, ball.color, [ball.x, ball.y], ball.radius)

            ball_left_text()

            blocks_left_text()

            if check_lose(Ball.BALLS_LEFT):
                lost_screen()

            if check_win():
                win_screen()

            # -------------- Updating board --------------
            fps_clock.tick(FPS)
            pygame.display.update()

            if check_lose(Ball.BALLS_LEFT) or check_win():
                pygame.time.wait(2000)
                Ball.BALLS_LEFT = BALL_NUM
                Block.BLOCKS = []
                BLOCKS = create_blocks(MAP)
                ball.x = BALL_START_POS[0]
                ball.y = BALL_START_POS[1]
                ball.vx = BALL_START_SPEED[0]
                ball.vy = BALL_START_SPEED[1]
                player1.x = PLAYER_X


if __name__ == "__main__":
    main_fct()
