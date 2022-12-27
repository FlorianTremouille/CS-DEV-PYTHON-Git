"""
Class s'occupant de la partie en générale. Elle coordonne les autres classes.
"""

from tkinter import Canvas

from .Player import Player
from .Enemy import Enemy

class Game: 

    def __init__(self, canvas: Canvas): 
        self.__canvas = canvas
        self.__Enemy_per_wave = 5
        self.__First_Tag_of_summoned_enemy = 0
        self.__Last_Tag_of_summoned_enemy = 5
        self.init_player()   
        self.init_enemies()
    
    def get_canvas(self):
        return self.__canvas

    def init_player(self):
        player = Player(self.__canvas)
        self.__canvas.create_rectangle(
            player.get_x(),
            player.get_y(),
            player.get_x() + player.get_width(),
            player.get_y() + player.get_height(),
            tags = 'player',
            fill = player.get_color()
        )

    def init_enemies(self):
        x_start = 235
        y_start = 5
        space_between = 20
        Enemy_To_Summon = []

        for i in range(
            self.__First_Tag_of_summoned_enemy,
            self.__Last_Tag_of_summoned_enemy):

            Tag = 'Enemy_{0}'.format(i)
            Enemy_To_Summon.append(Tag)

        for id in Enemy_To_Summon:
            tag = 'enemy'
            enemy = Enemy(self.__canvas)                                  
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
        
        self.__First_Tag_of_summoned_enemy = self.__Last_Tag_of_summoned_enemy +1
        self.__Last_Tag_of_summoned_enemy += self.__Enemy_per_wave

        self.start_enemies_pattern()

        
    def start_enemies_pattern(self, way: int = -1):
        x = 5
        y = 0
        enemies = self.__canvas.find_withtag('enemy')
        if len(enemies) > 0 :

            last_enemy_of_row_c = self.__canvas.coords(enemies[-1])
            first_enemy_of_row_c = self.__canvas.coords(enemies[0])

            if last_enemy_of_row_c[2] > 750 and way == 1 :
                way = -1
            elif first_enemy_of_row_c[0] < 50 and way == -1 :
                y = 50
                way = 1
            
            for enemy in enemies:
                if way == 1:
                    self.__canvas.move(enemy, x, y)
                elif way == -1:
                    self.__canvas.move(enemy, -x, y)
            self.__canvas.after(40, lambda: self.start_enemies_pattern(way))     
