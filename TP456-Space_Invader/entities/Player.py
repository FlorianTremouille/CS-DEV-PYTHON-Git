from .Projectile import CProjectile

class CPlayer:

    def __init__(self,x,y,w,h):
        self.__x=x
        self.__y=y
        self.__w=w
        self.__h=h
        self.__tir = []

    def init_player(self,canvas):
        Can_Player = canvas.create_rectangle(
            self.__x,
            self.__y,
            self.__x + self.__w,
            self.__y + self.__h,
            fill='blue'
            )
        self.__Can_Player = Can_Player
        return self.__Can_Player

    def deletir(self) :
        self.__tir = self.__tir[0:-1]

    def gettir(self):
        return self.__tir
    
    def settir(self,tir):
        self.__tir.append(tir)

    def getw(self):
        return self.__w

    def getCP(self):
        return self.__Can_Player

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def set(self,x,y):
        self.__x = x
        self.__y = y


    def PlayerProj_Init(self,canvas,x,y):
        CPlayerProj = CProjectile(
        x, # pas bon il faut récupérer en live
        y,
        5,
        30,
        )
        PlayerProj = CPlayerProj.projectile_Init(canvas)
        return PlayerProj