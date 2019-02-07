from constants import *
import random


# -------------- Block Class --------------
class Block:
    BLOCKS = []

    def __init__(self, color, width, height, posXY, border):
        """
        Initialization for a Block object
        :param color: color (tuple) (x, x, x)
        :param width: width (int)
        :param height: height (int)
        :param posXY: position (tuple) (x, y)
        :param border: border (int)
        """
        self.color = color
        self.width = width
        self.height = height
        self.border = border
        self.x = posXY[0]
        self.y = posXY[1]
        if self.color != WHITE:
            Block.BLOCKS.append(self)

    def destroy(self):
        """
        Destroy method for a block object
        :return: None
        """
        del Block.BLOCKS[Block.BLOCKS.index(self)]
        del self


def create_blocks(map=None):
    """
    Create a list that contains all the blocks
    :return: block list (list)
    """
    blocks = []
    i = 0
    j = 0
    num = 0
    if map is None:
        for row in range(NUM_ROWS):
            for column in range(NUM_COLS):
                blocks.append(Block(BLOCK_COLORS[random.randint(0, 2)], BLOCK_WIDTH, BLOCK_HEIGHT, (i, j), BLOCK_BORDER))
                i += BLOCK_WIDTH
            i = 0
            j += BLOCK_HEIGHT
        return blocks
    else:
        for block_color in map:
            if block_color == 0:
                i += BLOCK_WIDTH
            else:
                Block(block_color, BLOCK_WIDTH, BLOCK_HEIGHT, (i, j), BLOCK_BORDER)
                i += BLOCK_WIDTH
            num += 1
            if num == 6:
                j += BLOCK_HEIGHT
                i = 0
                num = 0
        return Block.BLOCKS