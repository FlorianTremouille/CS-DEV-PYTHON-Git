import time

VITESSE_ENNEMI_X = 5
VITESSE_ENNEMI_Y = 50

class CEnnemi:

    DIST_BETWEEN = 20
    ENNEMI_COORD_X_START = 235
    ENNEMI_COORD_Y_START = 2
    ENNEMI_WIDTH = 50
    ENNEMI_HEIGHT = 50

    def __init__(self,canvas):
        self.__Can_Tag_Ennemis = []
        
        pass
    def init_ennemis(self,canvas):
        X_Ennemi = self.ENNEMI_COORD_X_START
        Y_Ennemi =self.ENNEMI_COORD_Y_START

        for x in range(0, 5):
            self.__Can_Tag_Ennemis.append("Ennemi_{0}".format(x))
            canvas.create_rectangle(X_Ennemi,
                                    Y_Ennemi,
                                    X_Ennemi +self.ENNEMI_WIDTH,
                                    Y_Ennemi + self.ENNEMI_HEIGHT,
                                    tags = "Ennemi_{0}".format(x),
                                    fill= 'red')
            X_Ennemi += self.ENNEMI_WIDTH + self.DIST_BETWEEN
        self.EnnemiMove(-1,canvas)
    
    def get(self):
        return self.__Can_Tag_Ennemis

    def EnnemiMove(self,way,canvas):
        x = VITESSE_ENNEMI_X
        y = 0
        CoordsLast = canvas.coords(self.__Can_Tag_Ennemis[-1])
        CoordsFirst = canvas.coords(self.__Can_Tag_Ennemis[0])

        if CoordsLast[2] > 750 and way == 1 :
            way = -1
        elif CoordsFirst[0] < 50 and way == -1 :
            y = VITESSE_ENNEMI_Y
            way = 1
        
        for ennemi in self.__Can_Tag_Ennemis:
            if way == 1:
                canvas.move(ennemi,x,y)
            elif way == -1:
                canvas.move(ennemi,-x,y)
        canvas.after(40,lambda: self.EnnemiMove(way,canvas))
    