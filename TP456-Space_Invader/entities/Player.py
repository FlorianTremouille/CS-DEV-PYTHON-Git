from .Projectile import CProjectile

class CPlayer:

    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h

    def player_Init(self,canvas):
        self.Can_Player = canvas.create_rectangle(
            self.x,
            self.y,
            self.x + self.w,
            self.y + self.h,
            fill='blue'
            )
        return self.Can_Player

    def PlayerProj_Init(self,canvas):
        self.CPlayerProj = CProjectile(
        self.x, # pas bon il faut récupérer e,n live
        self.y,
        5,
        30,
        )
        PlayerProj = self.CPlayerProj.projectile_Init(canvas)
        return PlayerProj