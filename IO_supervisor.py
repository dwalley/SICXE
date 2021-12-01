# Module which defines how the I/O system works

import sys, os

from Registers import *
from random import *
from binascii import *

class IO_supervisor(Registers):
    
    def __init__(self,my_registers):
        self.i_o = 'stuff'
        self.num_devices = 2
        # native OS files simulate devices
        working_directory = os.getcwd()
        device00 = os.path.join(working_directory,'device00')
        device01 = os.path.join(working_directory,'device01')
        self.device_names = [device00, device01]
        self.files = [open(self.device_names[0],'r+'),\
                      open(self.device_names[1],'r+')]
        self.device_statuses = [1,1]
        self.num_channels = 16
        self.devices_per_channel = 16
        self.my_registers = my_registers
        self.hex_digits = "0123456789ABCDEF"

    def read_character(self,device):
        # low level direct fetch of the next byte from device # device
        # device is between 0 and 255
        # NOTE: files are sequences of 2 character hexidecimal numbers

        if device < 0 or device >255:
            raise address_out_of_range

        my_buffer = bytearray(1)

        hex_string = self.files[device].read(2)
        if len(hex_string) <> 2:
            raise IO_fault

        # convert two hex digits to a byte
        my_buffer[0] = unhexlify(hex_string)

        return my_buffer[0]

    def test_device(self,device):

        a = randint(-2,1)
        self.device_statuses[device] = a

        result = bytearray(1)

        if a == -1:
            result[0] = self.my_registers.CC_less_than
        elif a == 0:
            result[0] = self.my_registers.CC_equal_to
        else:
            result[0] = self.my_registers.CC_greater_than

        return result[0]

    def write_character(self,device,char):
        # low level direct write of the next byte to device # device
        # device is between 0 and 255
        # NOTE: files are sequences of 2 character hexidecimal numbers
        
        if device < 0 or device >255:
            raise address_out_of_range

        # break char into low and high half-bytes
##        print("in write_character, char is",char)
##        print("((char/16)*16) is",((char/16)*16))
        low_4_bits = char - ((char/16)*16)
##        print("low 4 bits is ",low_4_bits)
        high_4_bits = (char - low_4_bits)/16
##        print("high 4 bits is ",high_4_bits)

        # convert to 2 character hex string
        hex_string = self.hex_digits[high_4_bits] + self.hex_digits[low_4_bits]
##        print("hex string is ",hex_string)

        self.files[device].write(hex_string)

    def shutdown(self):
        for i in self.files: i.close()
##        raise io_shutdown
        return

    def restart(self):
        self.files = [open(self.device_names[0],'r+'),\
                      open(self.device_names[1],'r+')]
        return
        
