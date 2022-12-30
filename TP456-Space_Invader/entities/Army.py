"""
Class s'occupant du groupe des ennemis.
"""

from tkinter import Canvas

from .EnemyType import EnemyType
from .BasicEnemy import BasicEnemy
from .AdvancedEnemy import AdvancedEnemy

class Army:

    def __init__(self, canvas: Canvas, level):
        self.__canvas = canvas
        self.__level = level
        self.__initial_wave_size = len(self.__level)

        # self.__initial_wave_size = 5
        self.is_army_alive = True

        self.init_enemies()

    def init_enemies(self):
        x_start = 235
        y_start = 5
        space_between = 20
        tag = 'enemy'

        # for _ in range (0, self.__initial_wave_size):
        for enemy_type in self.__level:  
            enemy = None         
            if enemy_type == EnemyType.BasicEnemy.value:
                enemy = BasicEnemy(self.__canvas)                
            elif enemy_type == EnemyType.AdvancedEnemy.value:
                enemy = AdvancedEnemy(self.__canvas)
            
            id = self.__canvas.create_rectangle(
                x_start,
                y_start,
                x_start + enemy.get_width(),
                y_start + enemy.get_height(),
                tags = tag,
                fill= enemy.get_color())
            enemy.set_id(id)
            enemy.check_for_collision()

            x_start += enemy.get_width() + space_between

        self.start_enemies_pattern(self.__initial_wave_size)

        
    def start_enemies_pattern(self, last_enemy_count: int, way: int = -1, speed: float = 5):
        y = 0
        enemies = self.__canvas.find_withtag('enemy')      

        if len(enemies) > 0 :
            new_enemy_count = len(enemies)
            speed += ((last_enemy_count - new_enemy_count) / last_enemy_count) * speed * 0.5    

            last_enemy_of_row_c = self.__canvas.coords(enemies[-1])
            first_enemy_of_row_c = self.__canvas.coords(enemies[0])

            if last_enemy_of_row_c[2] > 750 and way == 1 :
                way = -1
            elif first_enemy_of_row_c[0] < 50 and way == -1 :
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