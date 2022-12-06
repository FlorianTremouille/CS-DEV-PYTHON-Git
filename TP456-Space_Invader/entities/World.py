from .Player import CPlayer

class World:
    PLAYER_COORD_X = 350
    PLAYER_COORD_Y = 648
    PLAYER_WIDTH = 50
    PLAYER_HEIGHT = 50


    def __init__(self, canvas): 
        self.init_World(canvas)

    def init_World(self, canvas):
        W_Player = CPlayer(
            self.PLAYER_COORD_X,
            self.PLAYER_COORD_Y,
            self.PLAYER_WIDTH,
            self.PLAYER_HEIGHT,
            )
        W_Player.player_Init(canvas) 
        self.W_Player = W_Player
