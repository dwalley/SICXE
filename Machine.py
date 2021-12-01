# SIC Emulator
# SIC/XE code currently commented out

# machine defining classes

from ALU import *
from Registers import *
from IO_supervisor import *

class On_off_switch:
    def __init__(self):
        self.on_off = "off"

        
class Memory():
    def __init__(self):
        self.ram = bytearray(2**20)
        self.max_index = 2**20 - 1

class Clock():
    def __init__(self):
        self.clock_ticks = 0

class Machine(On_off_switch,Registers,Memory,IO_supervisor,Clock,ALU):
    def __init__(self,name):
        self.my_name = name
        self.my_on_off_switch = On_off_switch()
        self.my_memory = Memory()
        self.my_registers = Registers()
        self.my_io = IO_supervisor(self.my_registers)
        self.my_clock = Clock()
        self.my_ALU = ALU(self.my_registers,self.my_memory,self.my_io)
