"""
Class s'occupant du chargement des niveaux. Leur chargement et leur difficulté.
Date : 30/12/2022
Florian Trémouille et Hugo Miaglia
"""


from tkinter import Canvas
import json

from .Army import Army
from .RocksGroups import RocksGroup


class Level: 

    is_level_finished = False

    def __init__(self, canvas : Canvas, level_number : int = 1):
        self.__canvas = canvas

        self.init_rock()
        
        self.level_number = level_number
        self.load_level()   

    def load_level(self, level_name : str = 'level_1.json'):
        """
        Charge le fichier .json associé au niveau souhaité.
        Puis initialise le groupe d'alien du niveau.
        """
        self.is_level_finished = False
        with open('data/levels/'+level_name, ) as level_file: 
            level = json.load(level_file)
            self.init_army(level)

    def increase_level(self):
        """
        Supprime le précédent objet Army.
        Calcul le fichier level devant etre chargé.
        Puis lance le chargement du nieau suivant.
        """
        del self.__current_army

        self.level_number += 1
        level_to_load = self.level_number%5
        if level_to_load == 0:
            level_to_load = 5

        level = 'level_'+ str(level_to_load) + '.json'
        self.load_level(level)

    def init_army(self, level : list):
        """
        Calcul la vitesse du groupe d'armée en fonction du niveau.
        Crée l'objet Army en lui associant la liste d'ennemie et la vitesse correspondant au niveau.
        Puis lance la boucle is_army_alive()
        """
        speed_factor = (self.level_number-1)//5
        self.__current_army = Army(self.__canvas, level, speed_factor)
        self.is_army_alive()

    def init_rock(self):
        """Initialise les groupes de roches."""
        RocksGroup(self.__canvas)

    def is_army_alive(self):
        """Boucle permetttant de vérifier si l'armée est toujours en vie."""
        if not self.__current_army.is_army_alive:
            self.is_level_finished = True            
        else:
            self.__canvas.after(500, lambda: self.is_army_alive())