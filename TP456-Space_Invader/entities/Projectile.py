class CProjectile :

    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h

    def projectile_Init(self,canvas):
        self.projectile = canvas.create_rectangle(
            self.x,
            self.y,
            self.x + self.w,
            self.y + self.h,
            fill = 'green'           
        )
        return self.projectile

    
