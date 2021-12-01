# class defining class consisting of bit light and toggle toggle switch pairs
import sys, pygame,os

from bit_lights import *
from switches import *

class bit_light_switch():

    def __init__(self,name,location,screen):

        self.name = name
        self.screen = screen
        # note location is the center of the bit light of the light/switch pair
        # the switch is located below the light, centered on the light
        self.current_location = location
        self.bit_light = bit_lights(name+'BitLight',self.current_location,self.screen)

        self.bit_switch = switches(name+'BitSwitch',self.current_location,self.screen)
        delta_y = self.bit_light.my_top() - self.bit_light.my_bottom()
        delta_y += self.bit_switch.my_top() - self.bit_switch.my_bottom()
        delta_y = -1*(delta_y/2)

        #move the bit_switch down to be under the light
        self.bit_switch.my_move((0,delta_y))

        return

    def return_value(self):
        return self.bit_light.return_value()

    def display_value(self,value):
        # value is either a one or a zero
        if value == 1:
            self.bit_light.change_setting('Red')
        else:
            self.bit_light.change_setting('Black')
        return

    def my_move(self,speed):
        #move both sprites associated with the light/switch pair together
        #  to a new location

        self.bit_light.my_move(speed)
        self.bit_switch.my_move(speed)

        return

    def process_click(self,mx,my,sounds):

        self.bit_light.process_click(mx,my,sounds)
        self.bit_switch.process_click(mx,my,sounds)

        return

    def blit_dongle(self,screen):
        
        self.bit_light.blit_dongle(screen)
        self.bit_switch.blit_dongle(screen)

        return

    def click_on_me(self,mx,my):

        if self.bit_light.click_on_me(mx,my) or \
            self.bit_switch.click_on_me(mx,my):
                return True
        else:
            return False

    def my_left(self):
        return min(self.bit_light.my_left(),self.bit_switch.my_left())

    def my_right(self):
        return max(self.bit_light.my_right(),self.bit_switch.my_right())

    def my_top(self):
        return self.bit_light.my_top()

    def my_bottom(self):
        return self.bit_switch.my_bottom()
