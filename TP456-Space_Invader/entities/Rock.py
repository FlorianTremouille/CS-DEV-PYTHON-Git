

from tkinter import Canvas



class Rock:
    def __init__(self, canvas : Canvas):
        self;__canvas = Canvas

    def set_id(self,id):
        self.__id = id

    def check_for_collision(self):        
        continue_check = False
        # c = self.get_canvas().coords(self.get_id())        
        # entitites = self.get_canvas().find_overlapping(c[0], c[1], c[2], c[3]) # a changer a cause du polygone       
        
        # for widget in entitites:
        #     for tag in self.get_canvas().gettags(widget):
        #         if 'p_bullet' == tag:
        #             self.die_and_destroy_bullet(widget)
        #             self.update_score(self.__class__.__name__)
        #         else: 
        #             continue_check = True
        # if (continue_check and self.get_is_alive()):    
        #     self.set_check_for_collision_after_id(self.get_canvas().after(30, lambda: self.check_for_collision()))
