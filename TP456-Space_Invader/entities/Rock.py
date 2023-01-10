

from tkinter import Canvas



class Rock:
    def __init__(self, canvas : Canvas):
        self.__canvas = canvas

    def set_id(self,id):
        self.__id = id

    def check_for_collision(self):        
        continue_check = False
        c = self.__canvas.coords(self.__id)
        print(c)     
        entitites = self.__canvas.find_overlapping(c[0], c[1], c[2], c[3]) # a changer a cause du polygone       
        
        for widget in entitites:
            for tag in self.__canvas.gettags(widget):
                if 'p_bullet' == tag:
                    print('Player bullet contact')
                    self.destroy_contact_widget(widget)
                    continue_check = True
                if 'e_bullet' == tag:
                    self.die_and_destroy_widget(widget)
                if 'enemy' == tag:
                    self.die_and_destroy_widget(widget)
                else: 
                    continue_check = True
                    print('Continue check = TRUE')
        if (continue_check):    
            self.__canvas.after(30, lambda: self.check_for_collision())

    def die_and_destroy_widget(self, widget):
        self.__canvas.delete(self.__id)
        self.destroy_contact_widget(widget)

    def destroy_contact_widget(self, widget):
        self.__canvas.delete(widget)



