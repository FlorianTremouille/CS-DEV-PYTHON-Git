"""
Class s'occupant du Boss dans le level 5.
"""

from tkinter import Canvas

from .AdvancedEnemy import AdvancedEnemy
from .Bullet import Bullet

class BossEnemy(AdvancedEnemy):

    bullet_speed = 5

    def __init__(self, canvas: Canvas, scale: int = 100, color: str = 'grey'):
        super().__init__(canvas, scale, color)

        self.__remaining_lives = 2

        self.set_min_fire_delay(0.5)
        self.set_max_fire_delay(3)


    def fire_bullet(self):
        if self.get_is_alive():
            for num_bullet in range(0,3) :
                bullet_tag = 'e_bullet'
                actual_enemy_coords = self.get_canvas().coords(self.get_id())
                delta = num_bullet
                if num_bullet == 2 :
                    delta = -1  # centrer les tirs
                x = actual_enemy_coords[0] + delta * 20
                y = actual_enemy_coords[1] 
                Bullet(self.get_canvas(), bullet_tag, x, y, 'grey').fire(self.bullet_speed, 1)
            self.define_fire()

    def touch_and_destroy_bullet(self, bullet):
        if self.__remaining_lives == 0:
            self.boss_dead()
        else:
            self.__remaining_lives -= 1
            if self.__remaining_lives == 1 :
                self.get_canvas().itemconfig(self.get_id(), outline = 'orange')
            
            if self.__remaining_lives == 0 :
                self.get_canvas().itemconfig(self.get_id(), outline = 'red')

        self.get_canvas().delete(bullet)

    def boss_dead(self):
        self.__is_alive = False
        self.get_canvas().delete(self.get_id())
        self.update_score(self.__class__.__name__)