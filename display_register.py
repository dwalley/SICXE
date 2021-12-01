# class which provides functionality to the display panel register

from byte_light_switch import *
from my_exception_definitions import *

class display_register():

    def __init__(self,location,screen,machine,sounds):

        self.location = location
        self.screen = screen
        self.sounds = sounds
        self.my_machine = machine
        self.connected = True
        self.connected_register = 'A'
        self.current_value = bytearray(3)
        self.bytes = ['High','Middle','Low']
        self.byte_banks = {}

        self.byte_banks['High'] = byte_light_switch('High Byte',self.location,\
                                           [23,22,21,20,19,18,17,16],screen)
        self.byte_banks['Middle'] = byte_light_switch('Middle Byte',\
                            (self.location[0]+220,self.location[1]),\
                            [15,14,13,12,11,10,9,8],screen)
        self.byte_banks['Low'] = byte_light_switch('Low Byte',\
                            (self.location[0]+440,self.location[1]),\
                            [7,6,5,4,3,2,1,0],screen)

    def received_clock_tic(self):
        if self.connected == True:
            # the display register is tracking a machine register,
            # update it
            corresponding_register_value = \
                self.my_machine.my_registers.return_register_value(\
                    self.connected_register)
            #make sure register will fit in display (i.e., not F register)
            if len(corresponding_register_value) == 3:
                self.current_value = corresponding_register_value
                self.display_value(self.current_value)
            else:
                self.current_value[0] = 0 #zero out the array
                self.current_value[1] = 0
                self.current_value[2] = 0
                self.display_value(self.current_value)
        return

    def disconnect_from_register(self):
        self.connected = False
        return

    def connect_to_register(self,register):
        #connected register is a string representation of the registers
        # 'A', 'X', etc
        self.connected_register = register
        self.sounds[self.my_machine.my_registers.registers[register]].play()
        return

    def return_value(self):
        # returns value of register in bytearray format,
        # most significant byte first
        result = bytearray(3)
        for temp_i in range(0,3):
            result[temp_i] = self.byte_banks[self.bytes[temp_i]].return_value()
        return result

    def display_value(self,value):
        # turn on lights appropriately to display value
        #   value is a byte array with most significant byte first

        for temp_i in range(0,3):
            temp_byte = self.bytes[temp_i]
            self.byte_banks[temp_byte].display_value(value[temp_i])
            
        return

        
    def process_click(self,mx,my,sounds):
        if self.connected == True:
            # zero the display to prepart to receive input
            zero_array = bytearray(3)
            self.display_value(zero_array)
        for temp_byte in self.bytes:
            if self.byte_banks[temp_byte].click_on_me(mx,my):
                self.byte_banks[temp_byte].process_click(mx,my,sounds)
                # disconnect from register and stop the machine
                self.disconnect_from_register()
                raise stop_the_machine('Register Data Entry')
                # note that reconnecting to a register will occur when the load
                # register switch is activated, in which case the display register
                # will resume tracking whatever register is indicated by the
                # register knob
        return

    def click_on_me(self,mx,my):
        for temp_byte in self.bytes:
            if self.byte_banks[temp_byte].click_on_me(mx,my):
                return True
        return False

    def my_move(self,speed):
        for temp_byte in self.bytes:
            self.byte_banks[temp_byte].my_move(speed)
        return
            

    def blit_dongle(self,screen):

        for temp_byte in self.bytes:
            self.byte_banks[temp_byte].blit_dongle(screen)
        return

    def my_left(self):
        return self.byte_banks['High'].my_left()
    
    def my_right(self):
        return self.byte_banks['Low'].my_right()
    
    def my_top(self):
        return self.byte_banks['High'].my_top()
    
    def my_bottom(self):
        return self.byte_banks['High'].my_bottom()   
