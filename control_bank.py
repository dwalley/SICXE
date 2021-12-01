# class defining the collection of control switches

import sys, pygame,os
from switches import *
from my_exception_definitions import *

class control_bank():

    def __init__(self,screen,machine):

        self.my_switches = {}

        self.my_machine = machine

        self.control_bank_switches = ['Run','Halt','Step','Exec_Instr','Load_Reg']
        
        # initialize the run switch
        self.run_switch_location = (770,715)
        self.run_switch = switches('Run',self.run_switch_location,screen)
        self.my_switches['Run'] = self.run_switch

        #initialize the halt switch
        self.halt_switch_location = (710,715)
        self.halt_switch = switches('Halt',self.halt_switch_location,screen)
        self.my_switches['Halt'] = self.halt_switch

        #initialize the step switch
        self.step_switch_location = (640,715)
        self.step_switch = switches('Step',self.step_switch_location,screen)
        self.my_switches['Step'] = self.step_switch

        
        #initialize the EXECute INSTRuction switch
        self.exec_instr_switch_location = (560,715)
        self.exec_instr_switch = switches('Exec_Instr',\
                                          self.exec_instr_switch_location,screen)
        self.my_switches['Exec_Instr'] = self.exec_instr_switch

        #initialize the Load REGister switch
        self.load_reg_switch_location = (492,715)
        self.load_reg_switch = switches('Load_Reg',\
                                          self.load_reg_switch_location,screen)
        self.my_switches['Load_Reg'] = self.load_reg_switch

        return

    def click_on_me(self,mx,my):
        for switch in self.my_switches.keys():
            if self.my_switches[switch].click_on_me(mx,my):
                return True
        return False

    def process_click(self,mx,my,sounds):
        for switch in self.my_switches.keys():
            if self.my_switches[switch].click_on_me(mx,my):
                self.my_switches[switch].process_click(mx,my,sounds)
                if switch == 'Load_Reg':
                    raise load_register_activated("Load_Reg")
                elif switch == 'Exec_Instr':
                    raise execute_instruction_activated("Exec_Instr")
                elif switch == 'Step':
                    raise step_activated("Step")
                elif switch == 'Halt':
                    raise halt_machine("Halt")
                elif switch == 'Run':
                    raise run_machine("Run")
                return
        return

    def blit_dongle(self,screen):
        for switch in self.my_switches.keys():
            self.my_switches[switch].blit_dongle(screen)
        return
            
        
