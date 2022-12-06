class CPlayer:
    
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h

    def init_player(self,canvas):
        Can_Player = canvas.create_rectangle(
            self.x,
            self.y,
            self.x + self.w,
            self.y + self.h,
            fill='blue'
            )
        self.Can_Player = Can_Player
        return self.Can_Player