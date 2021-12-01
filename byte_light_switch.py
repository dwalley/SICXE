# class defining a 8 bit byte array of lights and switches

import sys, pygame,os

from bit_light_switch import *

class byte_light_switch():

    def __init__(self,name,location,bit_locations,screen):

        working_directory = os.getcwd()

        self.name = name
        self.screen = screen

        # bit locations is a list indicating the order of the bits
        # typically something like [7,6,5,4,3,2,1,0] or [15,14,13,12,11,10,9,8]
        self.bit_locations = bit_locations

        # location is relative to the center of the light on the top
        # left hand side of the bank of lights and switches

        self.current_location = location

        self.bit_light_switches = {}
        self.bit_light_switches_labels = {}
        self.label_sprites = {}
        self.label_rects = {}

        temp_offset_counter = 0
        for temp_bit in self.bit_locations:
            
            # create a light/switch pair for each bit in the byte
            self.bit_light_switches[temp_bit] = \
                bit_light_switch(self.name+str(temp_bit),self.current_location,\
                                 self.screen)

            # figure out how far over to move the light/switch pair, and move them
            temp_offset = temp_offset_counter * \
                (self.bit_light_switches[temp_bit].my_right() - \
                 self.bit_light_switches[temp_bit].my_left())
            
            self.bit_light_switches[temp_bit].my_move((temp_offset,0))
            temp_offset_counter += 1

            # create a label, label sprite, and label rectangle for each
            #  light/switch pair
            self.bit_light_switches_labels[temp_bit] = str(temp_bit)
            self.label_sprites[temp_bit] = pygame.image.load(\
                    os.path.join(working_directory,"GraphicDrawing",'Label'+str(temp_bit)+'.png'))
            self.label_rects[temp_bit] = self.label_sprites[temp_bit].get_rect()
            self.label_rects[temp_bit].center = \
                (self.current_location[0] + temp_offset,\
                 self.current_location[1] + \
                 (self.bit_light_switches[temp_bit].bit_light.my_top() - \
                  self.bit_light_switches[temp_bit].bit_light.my_bottom()))

        return

    def return_value(self):
        temp_value = 0
        for i in range(0,8):
            temp_value += \
                self.bit_light_switches[self.bit_locations[i]].return_value() * \
                2 ** (7-i)
        return temp_value

    def display_value(self,value):
        # value is a byte from a bytearray
        temp_value = value
        for i in range(0,8):
            if temp_value/(2**(7-i)) == 1:
                self.bit_light_switches[self.bit_locations[i]].display_value(1)
            else:
                self.bit_light_switches[self.bit_locations[i]].display_value(0)
            temp_value -= (temp_value/(2**(7-i)))* (2**(7-i))

    def process_click(self,mx,my,sounds):
        for temp_bit in self.bit_locations:
            if self.bit_light_switches[temp_bit].click_on_me(mx,my):
                self.bit_light_switches[temp_bit].process_click(mx,my,sounds)
        return

    def click_on_me(self,mx,my):
        for temp_bit in self.bit_locations:
            if self.bit_light_switches[temp_bit].click_on_me(mx,my):
                return True
        return False

    def my_move(self,speed):
        for temp_bit in self.bit_locations:
            self.bit_light_switches[temp_bit].my_move(speed)
            self.label_rects[temp_bit] = self.label_rects[temp_bit].move(speed)
        return
            

    def blit_dongle(self,screen):

        for temp_bit in self.bit_locations:
            self.bit_light_switches[temp_bit].blit_dongle(screen)
            screen.blit(self.label_sprites[temp_bit],\
                        self.label_rects[temp_bit])
        return

    def my_left(self):
        return self.bit_light_switches[self.bit_locations[0]].my_left()
    
    def my_right(self):
        return self.bit_light_switches[self.bit_locations[-1]].my_right()
    
    def my_top(self):
        return self.label_rects[self.bit_locations[0]].top()
    
    def my_bottom(self):
        return self.bit_light_switches[self.bit_locations[-1]].my_bottom()                

            
