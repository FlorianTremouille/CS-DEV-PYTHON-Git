"""
Class s'occupant des rochers.
Date : 09/12/2022
Florian Trémouille et Hugo Miaglia
"""

from tkinter import Canvas

class Rock:
    def __init__(self, canvas : Canvas):
        self.__canvas = canvas
        self.__is_alive = True

    def set_id(self,id : int) -> None:
        self.__id = id

    def set_is_alive(self,value : bool):
        self.__is_alive = value

    def check_for_collision(self):
        if len(self.__canvas.gettags(self.__id)) == 1:
            c = self.__canvas.coords(self.__id)
            entitites = self.__canvas.find_overlapping(c[0], c[1], c[2], c[3])
            
            for widget in entitites:
                for tag in self.__canvas.gettags(widget):
                    if 'p_bullet' == tag:
                        self.destroy_contact_widget(widget)
                    if 'e_bullet' == tag:
                        self.die_and_destroy_widget(widget)
                    if 'enemy' == tag:
                        self.die_and_destroy_widget(widget)

            if (self.__is_alive):    
                self.__canvas.after(30, lambda: self.check_for_collision())

    def die_and_destroy_widget(self, widget):
        self.set_is_alive(False)
        self.__canvas.delete(self.__id)
        self.destroy_contact_widget(widget)

    def destroy_contact_widget(self, widget):
        self.__canvas.delete(widget)