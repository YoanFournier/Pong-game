from constants import *
import main


# -------------- Ball Class --------------
class Ball:
    BALLS_LEFT = 3

    def __init__(self, color, radius, posXY, vecXY):
        """
        Initialization for the ball class. This class stocks all the info
        of a ball object like it's size, position and velocity
        :param color: color (tuple) (x, x, x)
        :param radius: radius (int)
        :param posXY: list [x, y]
        :param vecXY: list [vx, vy]
        """
        self.color = color
        self.radius = radius
        self.x = posXY[0]
        self.y = posXY[1]
        self.vx = vecXY[0]
        self.vy = vecXY[1]

    def new_pos(self):
        """
        Calculates the new position of a ball object
        :return: None
        """
        self.x = self.x + self.vx
        self.y = self.y + self.vy

    def check_player_collision(self, player):
        """
        Calculates the modification of the velocity of a ball object
        if their is a collision with a player object
        :param player: player object
        :return: None
        """
        if player.y <= self.y + self.radius <= player.y + 1:
            if self.x + self.radius >= player.x and self.x - self.radius <= player.x + PLAYER_WIDTH:
                coll_angle = self.x - (player.x + PLAYER_WIDTH/2)
                if coll_angle == 0:
                    self.vy *= -1
                    self.vx = 0
                if -40 <= coll_angle < 0:
                    self.vx = round(BALL_SPEED * coll_angle / 40)
                    self.vy = -BALL_SPEED
                if 40 >= coll_angle > 0:
                    self.vx = round(BALL_SPEED * coll_angle / 40)
                    self.vy = -BALL_SPEED

    def check_ball_fall(self, player):
        """
        Check if the ball falls
        :param player: player object
        :return: None
        """
        if self.y + self.radius >= SCREEN_HEIGHT + 2 * BALL_RADIUS:
            self.x = player.x + 30
            self.y = BALL_START_POS[1]
            self.vx = 0
            self.vy = BALL_START_SPEED[1]
            Ball.BALLS_LEFT -= 1
            pygame.draw.circle(main.DISPLAY, self.color, [self.x, self.y], self.radius)
            pygame.display.update()
            pygame.time.wait(1000)

    def check_wall_collision(self, side):
        """
        Calculates the modification of the velocity of a ball object
        if their is a collision with a wall
        :param side: string that represents if the ball hits the top/bottom walls
        or the left/right walls
        :return: None
        """
        if side == WALL_W:
            if self.x + self.radius >= SCREEN_WIDTH:
                self.x -= 5
                self.vx *= -1
            elif self.x - self.radius <= 0:
                self.x += 5
                self.vx *= -1

        if self.y - self.radius <= 0:
            if side == WALL_H:
                self.vy *= -1

    def check_block_collision(self, blocks):
        """
        Calculates the modification of the velocity of a ball object
        if their is a collision with a block
        :param blocks: block object list
        :return: None
        """

        def block_change(block):
            """
            Changes the block color
            :param block: block object
            :return: None
            """
            if block.color == RED:
                block.destroy()
            if block.color == GREEN:
                block.color = RED
            if block.color == BLUE:
                block.color = GREEN

        for block in blocks:
            # -------------- Bottom Collision --------------
            if self.y - self.radius == block.y + BLOCK_HEIGHT and self.x - self.radius <= block.x + BLOCK_WIDTH and self.x + self.radius >= block.x:
                self.vy = BALL_SPEED
                block_change(block)
                continue
            # -------------- Right Collision ---ma-----------
            elif block.x + BLOCK_WIDTH >= self.x - self.radius >= block.x + BLOCK_WIDTH - BALL_SPEED and self.y + self.radius >= block.y and self.y - self.radius <= block.y + BLOCK_HEIGHT:
                self.x += 5
                self.vx *= -1
                block_change(block)
                continue
            # -------------- Left Collision --------------
            elif block.x <= self.x + self.radius <= block.x + BALL_SPEED and self.y + self.radius >= block.y and self.y - self.radius <= block.y + BLOCK_HEIGHT:
                self.x -= 5
                self.vx *= -1
                block_change(block)
                continue
            # -------------- Top Collision --------------
            elif self.y + self.radius == block.y and self.x - self.radius <= block.x + BLOCK_WIDTH and self.x + self.radius >= block.x:
                self.vy = -BALL_SPEED
                block_change(block)
                continue