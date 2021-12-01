# class which provides functionality to the display panel opcode/operand bank

from byte_light_switch import *
from my_exception_definitions import *

class display_opcode_operand():

    def __init__(self,location,screen,machine):

        self.location = location
        self.screen = screen
        self.my_machine = machine
        self.connected = True
        self.bytes = ['Opcode','Operand_high','Operand_low']
        self.byte_banks = {}

        self.byte_banks['Opcode'] = byte_light_switch('Opcode',self.location,\
                                           [7,6,5,4,3,2,1,0],screen)
        self.byte_banks['Operand_high'] = byte_light_switch('Operand High',\
                            (self.location[0]+220,self.location[1]),\
                            [15,14,13,12,11,10,9,8],screen)
        self.byte_banks['Operand_low'] = byte_light_switch('Operand Low',\
                            (self.location[0]+440,self.location[1]),\
                            [7,6,5,4,3,2,1,0],screen)

    def received_clock_tic(self):
        if self.connected == True:
            # the opcode/operand bank is tracking the ALU
            #  update the lights
            self.display_value(self.my_machine.my_ALU.current_opcode_operand)
        return

    def disconnect_from_ALU(self):
        self.connected = False
        return

    def connect_to_ALU(self):
        self.connected = True
        return

    def return_value(self):
        # returns opcode/operand value from user interface in bytearray format
        # opcode first
        result = bytearray(3)
        for temp_i in range(0,3):
            result[temp_i] = self.byte_banks[self.bytes[temp_i]].return_value()
        return result

    def display_value(self,value):
        # turn on lights appropriately to display value
        #  value is a bytearray with operand first

        for temp_i in range(0,len(value)):
            temp_byte = self.bytes[temp_i]
            self.byte_banks[temp_byte].display_value(value[temp_i])

        for temp_i in range(len(value),3):
            temp_byte = self.bytes[temp_i]
            self.byte_banks[temp_byte].display_value(0)
            
        return

        
    def process_click(self,mx,my,sounds):
        if self.connected == True:
            # zero the display to prepart to receive input
            zero_array = bytearray(3)
            self.display_value(zero_array)
        for temp_byte in self.bytes:
            if self.byte_banks[temp_byte].click_on_me(mx,my):
                self.byte_banks[temp_byte].process_click(mx,my,sounds)
                # disconnect from ALU and stop the machine
                self.disconnect_from_ALU()
                raise stop_the_machine('Opcode/Operand Entry')
                # note that reconnecting to the ALU will occur when the execute
                # instruction switch or run switch is activated, in which case
                # the display will resume tracking the ALU current opcode/operand
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
        return self.byte_banks['Opcode'].my_left()
    
    def my_right(self):
        return self.byte_banks['Operand Low'].my_right()
    
    def my_top(self):
        return self.byte_banks['Opcode'].my_top()
    
    def my_bottom(self):
        return self.byte_banks['Opcode'].my_bottom()   
