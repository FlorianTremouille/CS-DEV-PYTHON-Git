"""
Class s'occupant des ennemies avancés (capables de tirer).
"""

from tkinter import Canvas
from random import uniform

from .BasicEnemy import BasicEnemy
from .Bullet import Bullet

class AdvancedEnemy(BasicEnemy):

    bullet_speed = 3

    def __init__(self, canvas: Canvas, width: int = 50, height: int = 50, color: str = 'purple'):
        super().__init__(canvas, width, height, color)

        self.define_fire()

    def define_fire(self):
        random_timer = int(round(uniform(1,5),3))
        self.fire_bullet_after_id = self.get_canvas().after(random_timer*1000, lambda: self.fire_bullet())

    def fire_bullet(self):
        if self.get_is_alive():
            bullet_tag = 'e_bullet'
            actual_enemy_coords = self.get_canvas().coords(self.get_id())
            x = actual_enemy_coords[0] + (self.get_width() / 2)
            y = actual_enemy_coords[1]
            Bullet(self.get_canvas(), bullet_tag, x, y, 'red').fire(self.bullet_speed, 1)
            self.define_fire()