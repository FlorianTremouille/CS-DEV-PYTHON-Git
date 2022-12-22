from tkinter import Canvas

from .Player import Player
from .Enemy import Enemy

class Game:  

    def __init__(self, canvas: Canvas): 
        self.__canvas = canvas 
        self.init_player()   
        self.init_enemies()
        self.start_enemies_pattern()
    
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

        for i in range(0, 5):
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
    
    def start_enemies_pattern(self, way: int = -1):
        x = 5
        y = 0
        enemies = self.__canvas.find_withtag('enemy')
        last_enemy_of_row = self.__canvas.coords(enemies[-1])
        first_enemy_of_row = self.__canvas.coords(enemies[0])

        if last_enemy_of_row[2] > 750 and way == 1 :
            way = -1
        elif first_enemy_of_row[0] < 50 and way == -1 :
            y = 50
            way = 1
        
        for enemy in enemies:
            if way == 1:
                self.__canvas.move(enemy, x, y)
            elif way == -1:
                self.__canvas.move(enemy, -x, y)

        self.__canvas.after(40, lambda: self.start_enemies_pattern(way))     
