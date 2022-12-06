class CEnnemi:

    DIST_BETWEEN = 20
    ENNEMI_COORD_X_START = 235
    ENNEMI_COORD_Y_START = 2
    ENNEMI_WIDTH = 50
    ENNEMI_HEIGHT = 50

    def __init__(self):
        pass
    def init_ennemis(self,canvas):
        X_Ennemi = self.ENNEMI_COORD_X_START
        Y_Ennemi =self.ENNEMI_COORD_Y_START
        dEnnemis = {}
        for x in range(0, 5):
            dEnnemis["Ennemi_{0}".format(x)] = canvas.create_rectangle(
                                                                    X_Ennemi,
                                                                    Y_Ennemi,
                                                                    X_Ennemi +self.ENNEMI_WIDTH,
                                                                    Y_Ennemi + self.ENNEMI_HEIGHT,
                                                                    fill='red')
            X_Ennemi += self.ENNEMI_WIDTH + self.DIST_BETWEEN
        self.dEnnemis = dEnnemis
        print(dEnnemis)
    
