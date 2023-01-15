"""
Class s'occupant du groupe des ennemis.
Date : 30/12/2022
Florian Trémouille et Hugo Miaglia
"""

from tkinter import Canvas


from .EnemyType import EnemyType
from .BasicEnemy import BasicEnemy
from .AdvancedEnemy import AdvancedEnemy
from .BossEnemy import BossEnemy

class Army:

    def __init__(self, canvas: Canvas, level, speed_factor : int):
        self.__canvas = canvas
        self.__level = level

        self.__initial_wave_size = self.initial_wave_size()

        self.init_enemies()
        self.start_enemies_pattern(self.__initial_wave_size, speed_factor)

    
    def initial_wave_size(self) -> int:
        """Retourne le nombre d'alien initialisé au début du niveau."""
        wave_size = 0
        for enemy_raw in self.__level:
            wave_size += len(enemy_raw)
        return wave_size

    def init_enemies(self):
        """Crée tous les aliens en fonction du niveau."""
        self.is_army_alive = True
        y_start = 25
        space_between = 20
        tag = 'enemy'

        for enemy_raw in self.__level:
            x_start = 50
            for enemy_type in enemy_raw:  
                enemy = None

                if enemy_type == EnemyType.BasicEnemy.value:
                    enemy = BasicEnemy(self.__canvas)                
                elif enemy_type == EnemyType.AdvancedEnemy.value:
                    enemy = AdvancedEnemy(self.__canvas)
                elif enemy_type == EnemyType.BossEnemy.value:
                    enemy = BossEnemy(self.__canvas)

                scale = enemy.get_scale()/5
                pts = [
                    (x_start+2.5*scale,y_start+5*scale),
                    (x_start+0.5*scale,y_start+2*scale),
                    (x_start,y_start+1*scale),
                    (x_start+1*scale,y_start),
                    (x_start+2*scale,y_start+1*scale),
                    (x_start+1.5*scale,y_start+2*scale),
                    (x_start+2.5*scale,y_start+3*scale),
                    (x_start+3.5*scale,y_start+2*scale),
                    (x_start+3*scale,y_start+1*scale),
                    (x_start+4*scale,y_start),
                    (x_start+5*scale,y_start+1*scale),
                    (x_start+4.5*scale,y_start+2*scale),
                    ]
                
                id = self.__canvas.create_polygon(
                    pts,
                    smooth=1,
                    splinesteps=12,
                    tags = tag,
                    fill= enemy.get_color())

                enemy.set_id(id)
                enemy.check_for_collision()

                if enemy_type == EnemyType.BossEnemy.value:
                    self.__canvas.itemconfig(id, outline = 'green', width = 4)

                x_start += enemy.get_scale() + space_between
            y_start += enemy.get_scale() + space_between
        
    def start_enemies_pattern(self, last_enemy_count : int, speed_factor: int, way: int = 1):
        """Lance le déplacement des aliens."""
        y = 0
        speed = speed_factor*2.5 + 50
        enemies = self.__canvas.find_withtag('enemy')

        if len(enemies) > 0 :
            new_enemy_count = len(enemies)
            speed += ((last_enemy_count - new_enemy_count) / last_enemy_count) * speed * 0.5        # Permet d'augmenter la vitesse des aliens lorsqu'un d'entre eux est tué.
            
            max_X_enemy_coord = self.__canvas.coords(enemies[-1])[20]
            min_X_enemy_coord = self.__canvas.coords(enemies[0])[4]

            for enemy in enemies:
                x_max = self.__canvas.coords(enemy)[20]
                x_min = self.__canvas.coords(enemy)[4]
                if x_max > max_X_enemy_coord:
                    max_X_enemy_coord = x_max
                if x_min < min_X_enemy_coord:
                    min_X_enemy_coord = x_min

            if max_X_enemy_coord > 750 and way == 1 :
                way = -1
            elif min_X_enemy_coord < 50 and way == -1 :
                y = 50
                way = 1
            
            for enemy in enemies:
                if way == 1:
                    self.__canvas.move(enemy, speed, y)
                elif way == -1:
                    self.__canvas.move(enemy, -speed, y)
            
            self.__canvas.after(40, lambda: self.start_enemies_pattern(new_enemy_count, speed_factor, way))     
        else:
            self.is_army_alive = False