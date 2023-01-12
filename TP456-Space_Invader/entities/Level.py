"""
Class s'occupant de la partie en générale. Elle coordonne les autres classes.
"""

from tkinter import Canvas
import json
from typing import List

from .Army import Army
from .RocksGroups import RocksGroup



class Level: 

    is_level_finished = False

    def __init__(self, canvas : Canvas, level_number: int = 1):
        self.__canvas = canvas
        
        self.level_number = level_number
        self.load_level()

        self.init_rock()   

    def load_level(self, level_name: str = 'level_1.json'):
        self.is_level_finished = False
        with open('levels_test/'+level_name, ) as level_file: 
            level = json.load(level_file)
            self.init_army(level)

    def increase_level(self):
        del self.__current_army

        self.level_number += 1
        level_to_load = self.level_number%5
        if level_to_load == 0:
            level_to_load = 5

        level = 'level_'+ str(level_to_load) + '.json'
        self.load_level(level)

    def init_army(self, level : List):
        speed_factor = (self.level_number-1)//5
        self.__current_army = Army(self.__canvas, level, speed_factor)
        self.is_army_alive()

    def init_rock(self):
        RocksGroup(self.__canvas)

    def is_army_alive(self):
        if not self.__current_army.is_army_alive:
            self.is_level_finished = True            
        else:
            self.__canvas.after(500, lambda: self.is_army_alive())        
    
    


