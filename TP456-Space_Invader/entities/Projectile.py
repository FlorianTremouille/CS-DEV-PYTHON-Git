class CProjectile :

    def __init__(self,x,y,w,h):
        self.__x=x
        self.__y=y
        self.__w=w
        self.__h=h

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def projectile_Init(self,canvas):
        self.__projectile = canvas.create_rectangle(
            self.__x,
            self.__y,
            self.__x + self.__w,
            self.__y + self.__h,
            fill = 'green'           
        )
        return self.__projectile

    
