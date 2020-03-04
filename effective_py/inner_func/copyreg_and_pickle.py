class GameState(object):

    def __init__(self):
        self.level = 0
        self.lives = 4


state = GameState()
state.level += 1
state.lives -= 1
