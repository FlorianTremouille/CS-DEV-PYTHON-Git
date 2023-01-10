"""
Class s'occupant du groupe des ennemis.
"""

from tkinter import Canvas
from turtle import color, width

from .EnemyType import EnemyType
from .BasicEnemy import BasicEnemy
from .AdvancedEnemy import AdvancedEnemy
from .BossEnemy import BossEnemy

class Army:

    def __init__(self, canvas: Canvas, level):
        self.__canvas = canvas
        self.__level = level
        self.__initial_wave_size = self.initial_wave_size()

        # self.__initial_wave_size = 5
        self.is_army_alive = True

        self.init_enemies()
    
    def initial_wave_size(self):
        wave_size = 0
        for enemy_raw in self.__level:
            wave_size += len(enemy_raw)
        return wave_size

    def init_enemies(self):
        self.is_army_alive = True
        y_start = 5
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

        self.start_enemies_pattern(self.__initial_wave_size)

        
    def start_enemies_pattern(self, last_enemy_count: int, way: int = 1, speed: float = 5):
        y = 0
        enemies = self.__canvas.find_withtag('enemy')

        if len(enemies) > 0 :
            new_enemy_count = len(enemies)
            speed += ((last_enemy_count - new_enemy_count) / last_enemy_count) * speed * 0.5    

            last_enemy_of_row_c = self.__canvas.coords(enemies[-1])
            first_enemy_of_row_c = self.__canvas.coords(enemies[0])

            if last_enemy_of_row_c[20] > 750 and way == 1 :  #2
                way = -1
            elif first_enemy_of_row_c[4] < 50 and way == -1 : #0
                y = 50
                way = 1
            
            for enemy in enemies:
                if way == 1:
                    self.__canvas.move(enemy, speed, y)
                elif way == -1:
                    self.__canvas.move(enemy, -speed, y)
            
            self.__canvas.after(40, lambda: self.start_enemies_pattern(new_enemy_count, way, speed))     
        else:
            self.is_army_alive = False