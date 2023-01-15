"""
Class SINGLETON qui s'occupe du compte et de l'actualisation de l'affichage du score.
Utilisation d'une pile.
Date : 09/12/2022
Florian Trémouille et Hugo Miaglia
"""

from tkinter import Canvas
import json

from .EnemyType import EnemyType


class Score:
    _instance = None
    __points = 0

    def __new__(cls, canvas : Canvas = None):
        if cls._instance is None:
            cls._instance = super(Score, cls).__new__(cls)
        return cls._instance

    def __init__(self, canvas : Canvas = None):
        self.__canvas = canvas
    
    def get_points(self):
        return self.__points

    def reset_score(self):
        self.__points = 0

    def update_score(self, enemy_type: str):
        """Augmente le score en fonction du type d'ennemi et actualise l'affichage."""
        if enemy_type == 'BasicEnemy':
            self.__points += 10
        elif enemy_type == 'AdvancedEnemy':
            self.__points += 25
        elif enemy_type == 'BossEnemy':
            self.__points += 150
        
        self.__canvas.itemconfig('score_text', text='Score : ' + str(self.__points))

    def save_if_new_best(self):
        """Enregistre le score de la partie si il est un noueau meilleur score."""
        best_scores_lst = self.read_bests()
        last_best = best_scores_lst[-1]
        if self.__points > last_best:
            best_scores_lst.append(self.__points)
            self.write_bests(best_scores_lst)

    def delete_last_best(self):
        """Supprime le dernier meilleur score."""
        best_scores_lst = self.read_bests()
        best_scores_lst.pop()
        self.write_bests(best_scores_lst)

    def get_best(self) -> int:
        return self.read_bests().pop()

    def read_bests(self) -> list:
        """Permet de de lire le fichier des meilleurs scores."""
        with open('data/best_scores.json', 'r') as score_file:
            score_lst = json.load(score_file)
        return score_lst

    def write_bests(self, score_lst : list):
        """Permet d'écrire le fichier des meilleurs scores."""
        with open("data/best_scores.json", "w") as outfile:
            json.dump(score_lst, outfile)