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
    
