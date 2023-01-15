"""
Class s'occupant de la création de rochers.
Utilisation d'une liste.
Date : 09/12/2022
Florian Trémouille et Hugo Miaglia
"""

from tkinter import Canvas

from .Rock import Rock

class RocksGroup: 

    def __init__(self, canvas : Canvas):
        self.__canvas = canvas
        self.__rock_width = 20
        self.__rocks_groups_number = 6
        self.__rocks_groups_spawn_points = []
        # self.__rock_placement_cross = [                       "Permet de placer les rocher en forme de croix"
        #     (0,-1),
        #     (-1,0), (0,0), (1,0),
        #     (0,1)
        #     ]
        self.__rock_placement_cube = [
            (-1,-1), (0,-1), (1,-1),
            (-1,0), (0,0), (1,0),
            (-1,1), (0,1), (1,1)
            ]

        self.init_rock_spawn_points()
        self.init__rocks()

    def init_rock_spawn_points(self):
        """Calcul les points de spawn des groupes de rochers en fonction du nombre de groupe et de la largeur du canvas."""
        self.__canvas.update()
        canvas_width = self.__canvas.winfo_width()
        x_spawn_point = canvas_width / (self.__rocks_groups_number + 1)
        for i in range (1, self.__rocks_groups_number +1):
            self.__rocks_groups_spawn_points.append(x_spawn_point * i - (self.__rock_width/2) )

    def init__rocks(self):
        """Crée les rochers selon le placement prédéfini."""
        dist = self.__rock_width
        for spawn_point in self.__rocks_groups_spawn_points:
            for c in self.__rock_placement_cube:
                x, y = c[0], c[1]
                p1 = spawn_point + (dist*x)
                p2 = 500 + (dist*y)
                p3 = spawn_point + (dist*(x+1))
                p4 = 500 + (dist*(y+1))

                rock = Rock(self.__canvas)
                tag = 'rock'
                id = self.__canvas.create_rectangle(p1, p2, p3, p4, fill='darkgrey', tags = tag)

                rock.set_id(id)
                rock.check_for_collision()