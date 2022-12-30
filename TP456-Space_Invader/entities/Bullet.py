"""
Class s'occupant des tirs.

"""

from tkinter import Canvas;

class Bullet:

    def __init__(self, canvas: Canvas, tag: str, x: float, y: float, color: str = 'green', width: int = 10, height: int = 30):
        self.__canvas = canvas
        self.__tag = tag
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__color = color
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

    def get_interval_id(self):
        return self.__interval_id

    def init_in_canvas(self):
        id = self.__canvas.create_rectangle(
            self.__x,
            self.__y,
            self.__x + self.__width,
            self.__y + self.__height,
            tags = self.__tag,
            fill = self.__color
        )
        self.__id = id

    def fire(self, speed: float, way: int = -1):
        self.__canvas.move(self.__id, 0, way * 3 * speed)
        self.check_fire_out_of_range()
        self.__interval_id = self.__canvas.after(30, lambda: self.fire(speed, way))

    def check_fire_out_of_range(self):
        c = self.__canvas.coords(self.__id)
        if len(c)>1 and (c[1] < 0 or c[3] > 700) :
            self.__canvas.delete(self.__id)