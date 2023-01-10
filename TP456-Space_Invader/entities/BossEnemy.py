"""
Class s'occupant du Boss dans le level 5
"""

from tkinter import Canvas
from random import uniform

from .AdvancedEnemy import AdvancedEnemy
from .Bullet import Bullet

class BossEnemy(AdvancedEnemy):

    bullet_speed = 5

    def __init__(self, canvas: Canvas, scale: int = 50, color: str = 'black'):
        super().__init__(canvas, scale, color)

        # self.__min_fire_delay = 1
        # self.__max_fire_delay = 3


    def fire_bullet(self):
        if self.get_is_alive():
            for num_bullet in range(0,3) :
                bullet_tag = 'e_bullet'
                actual_enemy_coords = self.get_canvas().coords(self.get_id())
                delta = num_bullet
                if num_bullet == 2 :
                    delta = -1  # centrer les tirs
                x = actual_enemy_coords[0] + delta * 10
                y = actual_enemy_coords[1] 
                Bullet(self.get_canvas(), bullet_tag, x, y, 'red').fire(self.bullet_speed, 1)
            self.define_fire()