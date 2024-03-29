"""
Class s'occupant des ennemies avancés (capables de tirer).
Date : 30/12/2022
Florian Trémouille et Hugo Miaglia
"""

from tkinter import Canvas
from random import uniform

from .BasicEnemy import BasicEnemy
from .Bullet import Bullet

class AdvancedEnemy(BasicEnemy):

    bullet_speed = 3

    def __init__(self, canvas: Canvas, scale: int = 50, color: str = 'purple'):
        super().__init__(canvas, scale, color)

        self.__min_fire_delay = 1           # Temps MINIMUM entre 2 tirs.
        self.__max_fire_delay = 5           # Temps MAXIMUM entre 2 tirs.

        self.define_fire()

    def set_min_fire_delay(self, time : float):
        self.__min_fire_delay = time

    def set_max_fire_delay(self, time : float):
        self.__max_fire_delay = time

    def get_min_fire_delay(self) -> int:
        return self.__min_fire_delay

    def get_max_fire_delay(self) -> int:
        return self.__max_fire_delay

    def define_fire(self):
        """Défini de manière pseudo aléatoire le moment où l'alien va tirer."""
        random_timer = int(round(uniform(self.get_min_fire_delay(),self.get_max_fire_delay()),3)*1000)
        self.get_canvas().after(random_timer, lambda: self.fire_bullet())

    def fire_bullet(self):
        """
        Réalise le tir de l'alien.
        Crée l'objet de classe Bullet avec les paramètres adaptés à l'alien.
        """
        actual_enemy_coords = self.get_canvas().coords(self.get_id())
        if self.get_is_alive() and len(actual_enemy_coords) != 0:
            bullet_tag = 'e_bullet'
            x = actual_enemy_coords[0]
            y = actual_enemy_coords[1]
            Bullet(self.get_canvas(), bullet_tag, x, y, 'red').fire(self.bullet_speed, 1)
            self.define_fire()