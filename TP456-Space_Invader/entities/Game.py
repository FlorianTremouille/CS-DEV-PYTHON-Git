"""
Class s'occupant de la partie en générale. Elle coordonne les autres classes.
"""

from tkinter import Canvas
from time import sleep

from .Player import Player
from .Level import Level


class Game: 

    def __init__(self, canvas: Canvas): 
        self.__canvas = canvas

        self.__player = self.init_player()
        self.is_player_alive()
        
        self.__current_level = self.init_level()
        self.is_level_finished()

    def get_canvas(self):
        return self.__canvas

    def init_player(self):
        player = Player(self.__canvas)
        id = self.__canvas.create_rectangle(
            player.get_x(),
            player.get_y(),
            player.get_x() + player.get_width(),
            player.get_y() + player.get_height(),
            tags = 'player',
            fill = player.get_color()
        )
        player.set_id(id)
        player.check_for_collision()
        return player

    def init_level(self):
        """Crée le niveau."""
        level = Level(self.__canvas)
        return level

    def set_next_level(self):
        self.display_level_won()
        self.__canvas.delete('p_bullet')
        self.__current_level.increase_level()
        self.is_level_finished()

    def display_level_won(self):
        text = 'Niveau ' + str(self.__current_level.level_number) + ' terminé !'
        self.game_transition(text)

    def display_game_lost(self):
        
        text = 'PERDU !\n Vous avez atteint le niveau ' + str(self.__current_level.level_number) + '. \n Score : ' + str('SCORERERE')
        self.game_transition(text)


    def game_transition(self, text:str, delete_after_delay: bool = True):
        id = self.__canvas.create_text(400, 350, text=text, fill='red', font=('Helvetica', '32'), justify='center')
        if delete_after_delay:
            self.__canvas.after(3*1000,lambda: self.erase_text(id))

    def game_lost(self):
        self.display_game_lost()

    def erase_text(self,id):
        self.__canvas.delete(id)

    def is_level_finished(self):
        if self.__current_level.is_level_finished:
            self.__canvas.after_cancel(self.__is_level_finished_after_id)
            self.set_next_level()
        else:
            self.__is_level_finished_after_id = self.__canvas.after(500, lambda: self.is_level_finished())

    def is_player_alive(self):
        if not self.__player.is_alive:
            self.__canvas.after_cancel(self.__is_player_alive_after_id)
            self.game_lost()
        else:
            self.__is_player_alive_after_id = self.__canvas.after(500, lambda: self.is_player_alive())
