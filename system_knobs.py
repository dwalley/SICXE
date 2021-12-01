# class defining the collection of knobs

import sys, pygame,os
from knobs import *
from my_exception_definitions import *

class system_knobs():

    def __init__(self,screen,machine):

        self.my_machine = machine

        self.my_knobs = {}

        self.my_system_knobs = ['on_off','register']

        # initialize the on/off knob        
        self.on_off_knob_settings = {'ON':'NorthEast','OFF':'SouthEast'}
        self.on_off_knob_location = (103,705)
        self.on_off_knob = knobs("on_off_knob",self.on_off_knob_location,\
                            self.on_off_knob_settings,'ON',screen)
        self.my_knobs['on_off'] = self.on_off_knob

        #initialize the registers knob        
        self.register_knob_settings = {'A':'North', 'X':'NorthEast','L':'East',\
                                  'PC':'SouthEast','SW':'South','B':'SouthWest',\
                                  'S':'West','T':'NorthWest'}
        self.register_knob_location = (909,185)
        self.register_knob = knobs("register_knob",self.register_knob_location,\
                                   self.register_knob_settings,'A',screen)
        self.my_knobs['register']=self.register_knob

        return

    def click_on_me(self,mx,my):
        for temp_knob in self.my_knobs.keys():
            if self.my_knobs[temp_knob].click_on_me(mx,my):
                return True
        return False

    def process_click(self,mx,my,sounds):
        for temp_knob in self.my_knobs.keys():
            if self.my_knobs[temp_knob].click_on_me(mx,my):
                self.my_knobs[temp_knob].process_click(mx,my,sounds)
                if temp_knob == 'register':
                    # we need to connect the display register to the machine
                    #register for the new setting
                    raise new_register_knob_setting(\
                        self.my_knobs[temp_knob].current_setting)
                if temp_knob == 'on_off':
                    sounds[0].play()
                return
        return

    def blit_dongle(self,screen):
        for temp_knob in self.my_knobs.keys():
            self.my_knobs[temp_knob].blit_dongle(screen)
        return
