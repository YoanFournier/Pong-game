from block import*
from ball import*


def intro_screen():
    """
    Intro screen function
    :return: None
    """
    introstring = "PONG GAME"
    introText = FONT2.render(introstring, True, WHITE, BLACK)
    introRect = introText.get_rect()
    introRect.center = (150, 300)

    pressstring = "Press space to play..."
    pressText = FONT1.render(pressstring, True, WHITE, BLACK)
    pressRect = pressText.get_rect()
    pressRect.center = (150, 350)

    DISPLAY.fill(BLACK)
    DISPLAY.blit(introText, introRect)
    DISPLAY.blit(pressText, pressRect)

    fps_clock.tick(FPS)
    pygame.display.update()


def pause_screen():
    """
    Pause screen function
    :return: None
    """
    pausestring = "Pause"
    pauseText = FONT2.render(pausestring, True, WHITE, BLACK)
    pauseRect = pauseText.get_rect()
    pauseRect.center = (150, 300)
    DISPLAY.blit(pauseText, pauseRect)
    pygame.display.update()


def ball_left_text():
    """
    Text that shows the balls left
    :return: None
    """
    ballleftstring = "Balls left : " + str(Ball.BALLS_LEFT)
    ballText = FONT1.render(ballleftstring, True, WHITE, BLACK)
    ballRect = ballText.get_rect()
    ballRect.center = (50, 580)
    DISPLAY.blit(ballText, ballRect)


def blocks_left_text():
    """
    Text that shows the blocks left
    :return: None
    """
    blocksremainstring = "Blocks remaining : " + str(len(Block.BLOCKS))
    blockText = FONT1.render(blocksremainstring, True, WHITE, BLACK)
    blockRect = blockText.get_rect()
    blockRect.center = (220, 580)
    DISPLAY.blit(blockText, blockRect)


def lost_screen():
    """
    Losing screen function
    :return: None
    """
    loststring = "You lost... "
    lostText = FONT2.render(loststring, True, WHITE, BLACK)
    lostRect = lostText.get_rect()
    lostRect.center = (150, 300)
    DISPLAY.blit(lostText, lostRect)


def win_screen():
    """
    Win screen function
    :return: None
    """
    winstring = "You won !"
    winText = FONT2.render(winstring, True, WHITE, BLACK)
    winRect = winText.get_rect()
    winRect.center = (150, 300)
    DISPLAY.blit(winText, winRect)

