"""
Class s'occupant des tirs.
Date : 22/12/2022
Florian Trémouille et Hugo Miaglia
"""

from tkinter import Canvas;

class Bullet:

    def __init__(self, canvas: Canvas, tag: str, x: float, y: float, color: str = 'green', width: int = 10, height: int = 30):
        self.__canvas = canvas
        self.__canvas_height = self.__canvas.winfo_height()

        self.__tag = tag
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__color = color

        self.__bullet_display = True
        self.init_in_canvas()

    def get_canvas(self):
        return self.__canvas

    def get_tag(self):
        return self.__tag

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_width(self):
        return self.__width

    def get_height(self): 
        return self.__height   

    def get_color(self):        
        return self.__color

    def set_bullet_display(self, value : bool):
        self.__bullet_display = value

    def init_in_canvas(self):
        id = self.__canvas.create_rectangle(
            self.__x - (self.__width/2),
            self.__y,
            self.__x + (self.__width/2),
            self.__y - self.__height,
            tags = self.__tag,
            fill = self.__color
        )
        self.__id = id

    def fire(self, speed: float, way: int = -1):
        if self.__bullet_display:
            self.__canvas.move(self.__id, 0, way * 3 * speed)
            self.check_fire_on_screen()
            self.__interval_id = self.__canvas.after(30, lambda: self.fire(speed, way))

    def check_fire_on_screen(self):
        c = self.__canvas.coords(self.__id)
        if len(c)>1 and (c[3] < 0 or c[1] > self.__canvas_height):
            self.kill_bullet()
        if len(c) == 0:
            self.kill_bullet()
    
    def kill_bullet(self):
        self.set_bullet_display(False)
        self.__canvas.delete(self.__id)