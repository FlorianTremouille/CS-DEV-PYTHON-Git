
from tkinter import Canvas

class Rock: 

    def __init__(self, canvas : Canvas):
        self.__canvas = canvas
        self.__rock_width = 40
        self.__rocks_groups_number = 3
        self.__rocks_groups_spawn_points = []
        self.__rock_placement = [
            (-1,-1), (0,-1), (1,-1),
            (-1,0), (0,0), (1,0),
            (-1,1), (0,1), (1,1),
            ]

        self.init_rock_spawn_points()
        self.init__rocks()


    def init_rock_spawn_points(self):
        self.__canvas.update()
        canvas_width = self.__canvas.winfo_width()
        x_spawn_point = canvas_width / (self.__rocks_groups_number + 1)
        for i in range (1, self.__rocks_groups_number +1):
            self.__rocks_groups_spawn_points.append(x_spawn_point * i - (self.__rock_width/2) )

    def init__rocks(self):
        dist = self.__rock_width
        for spawn_point in self.__rocks_groups_spawn_points:
            for c in self.__rock_placement:
                x, y = c[0], c[1]
                p1 = spawn_point + (dist*x)
                p2 = 500 + (dist*y)
                p3 = spawn_point + (dist*(x+1))
                p4 = 500 + (dist*(y+1))
                self.__canvas.create_rectangle(p1, p2, p3, p4, fill='red')