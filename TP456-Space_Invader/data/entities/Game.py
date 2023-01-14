"""
Class s'occupant de la partie en générale. Elle coordonne les autres classes.
"""

from tkinter import Canvas, PhotoImage

from .Player import Player
from .Level import Level
from .Score import Score


class Game: 

    def __init__(self, canvas: Canvas): 
        self.__canvas = canvas

        self.__img_player = PhotoImage(file='data/images/player_2.png')
        self.__player = self.init_player()
        self.is_player_alive()
        
        self.__score = Score(self.__canvas)
        self.init_infos(self.__player.get_life_remaining())
        
        self.__current_level = self.init_level()
        self.is_level_finished()

    def get_canvas(self) -> Canvas:
        return self.__canvas

    def init_player(self) -> Player:
        player = Player(self.__canvas)
        id = self.__canvas.create_image(
            player.get_x(),
            player.get_y(),
            tags = 'player',
            image = self.__img_player
        )
        player.set_id(id)
        player.check_for_collision()
        return player
    
    def init_infos(self, vies : int, score : int = 0):
        self.__canvas.create_text(60,10,tags='score_text' ,text= 'Score : ' + str(self.__score.get_points()), fill='red', font=('Helvetica', '15'), justify='center')
        self.__canvas.create_text(715,10,tags='life_text' ,text= 'Vies restantes : ' + str(vies), fill='red', font=('Helvetica', '15'), justify='center')

    def init_level(self):
        """Crée le niveau."""
        return Level(self.__canvas)

    def set_next_level(self):
        self.display_level_won()
        self.__canvas.delete('p_bullet')
        self.__current_level.increase_level()
        self.is_level_finished()

    def display_level_won(self):
        text = 'Niveau ' + str(self.__current_level.level_number) + ' terminé !'
        self.game_transition(text)

    def display_game_lost(self):
        text = 'PERDU !\n Vous avez atteint le niveau ' + str(self.__current_level.level_number) + '. \n Score : ' + str(self.__score.get_points()) + '\n Meilleur Score : ' + str(self.__score.get_best())
        self.game_transition(text, False)

    def game_transition(self, text : str, delete_after_delay : bool = True):
        id = self.__canvas.create_text(400, 300, text=text, fill='red', font=('Helvetica', '32'), justify='center')
        if delete_after_delay:
            self.__canvas.after(3*1000,lambda: self.erase_text(id))

    def game_lost(self):
        self.__score.save_if_new_best()
        self.display_game_lost()
        self.__canvas.delete('p_bullet')
        self.__canvas.addtag_withtag('disabled','rock')
        self.__canvas.delete('player')

    def erase_text(self, id : int):
        self.__canvas.delete(id)

    def is_level_finished(self):
        if self.__current_level.is_level_finished:
            self.set_next_level()
        else:
            self.__canvas.after(500, lambda: self.is_level_finished())

    def is_player_alive(self):
        if self.__player.is_alive == False:
            self.game_lost()
        else:
            self.__canvas.after(500, lambda: self.is_player_alive())