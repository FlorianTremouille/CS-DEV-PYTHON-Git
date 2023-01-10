"""
Class singleton qui s'occupe du compte et de l'actualisation de l'affichage du score.
"""

from tkinter import Canvas

from .EnemyType import EnemyType


class Score:
    _instance = None
    __points = 0

    def __new__(cls, canvas : Canvas):
        if cls._instance is None:
            cls._instance = super(Score, cls).__new__(cls)
        return cls._instance

    def __init__(self, canvas : Canvas):
        self.__canvas = canvas
        # self.__points = 0
    
    def get_points(self):
        return self.__points

    def reset_score(self):
        self.__points = 0

    def update_score(self, enemy_type: str):

        if enemy_type == 'BasicEnemy':
            self.__points += 10
        elif enemy_type == 'AdvancedEnemy':
            self.__points += 25
        elif enemy_type == 'BossEnemy':
            self.__points += 150
        
        self.__canvas.itemconfig('score_text', text='Score : ' + str(self.__points))
