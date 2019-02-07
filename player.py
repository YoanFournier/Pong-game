# -------------- Player Class --------------
class Player:
    def __init__(self, color, width, height, posXY, vecX=0):
        """
        Initialization for a Player object
        :param color: color (tuple) (x, x, x)
        :param width: width (int)
        :param height: height (int)
        :param posXY: position (list) [x, y]
        :param vecX: velocity in the x axis (int)
        """
        self.color = color
        self.width = width
        self.height = height
        self.x = posXY[0]
        self.y = posXY[1]
        self.vx = vecX

    def new_pos(self):
        """
        Calculates the new position of a player object
        :return: None
        """
        self.x = self.x + self.vx