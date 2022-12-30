"""
Class s'occupant de la partie en générale. Elle coordonne les autres classes.
"""

from tkinter import Canvas
import json

from .Army import Army



class Level: 

    is_level_finished = False

    def __init__(self, canvas : Canvas, level_number: int = 1):
        self.__canvas = canvas
        self.level_number = level_number
        self.load_level()       

    def load_level(self, level_name: str = 'level_3.json'):
        with open('levels/'+level_name, ) as level_file: 
            level = json.load(level_file)
            self.init_army(level)

    def increase_level(self):
        self.level_number += 1
        level = 'level_'+ str(self.level_number) + '.json'
        self.load_level(level)

    def init_army(self, level):
        self.__current_army = Army(self.__canvas, level)
        self.is_army_alive()

    def is_army_alive(self):
        if not self.__current_army.is_army_alive:
            self.__canvas.after_cancel(self.__is_army_alive_after_id)
            self.is_level_finished = True            
        else:
            self.__is_army_alive_after_id = self.__canvas.after(500, lambda: self.is_army_alive())        
    
    


