# Module containing code for registers

class Registers():
    def __init__(self):
        self.A = bytearray(3)
        self.X = bytearray(3)
        self.L = bytearray(3)
        self.PC = bytearray(3)
        self.SW = bytearray(3)
        self.B = bytearray(3)
        self.S = bytearray(3)
        self.T = bytearray(3)
        self.F = bytearray(6)
        self.CC_less_than = 192
        self.CC_greater_than = 64
        self.CC_equal_to = 0
        self.CC_mask = 192 #bits 6-7
        self.not_CC_mask = 63 #bits 0-5
        self.supervisor_mode_mask = 1
        self.not_supervisor_mode_mask = 254 # bits 1-7
        self.registers = {'A':0,'X':1,'L':2,'PC':8,'SW':9,'B':3,'S':4,'T':5,'F':6}
        self.register_list = [self.A, self.X,self.L,self.B,self.S,self.T,self.F,0,self.PC,self.SW]
        
    def return_register_value(self,register):
        # register is a string representation of the register name
        target_register_index = self.registers[register]
        return self.register_list[target_register_index]

    def set_register_value(self,register,value):
        # register is a string representation of the register name
        # value is a byte array of the appropriate length, 3 or 6 bytes

        if register <> 'F':
            target_register_index = self.registers[register]
            self.register_list[target_register_index][0] = value[0]
            self.register_list[target_register_index][1] = value[1]
            self.register_list[target_register_index][2] = value[2]
        else:
            target_register_index = self.registers[register]
            self.register_list[target_register_index][0] = value[0]
            self.register_list[target_register_index][1] = value[1]
            self.register_list[target_register_index][2] = value[2]
            self.register_list[target_register_index][3] = value[3]
            self.register_list[target_register_index][4] = value[4]
            self.register_list[target_register_index][5] = value[5]
            

        return

    def CC_eq_query(self):
        if self.SW[0].__and__(self.CC_mask) == self.CC_equal_to:
            return True
        else:
            return False
        
    def CC_gt_query(self):
        if self.SW[0].__and__(self.CC_mask) == self.CC_greater_than:
            return True
        else:
            return False
        
    def CC_lt_query(self):
        if self.SW[0].__and__(self.CC_mask) == self.CC_less_than:
            return True
        else:
            return False

    def CC_eq_set(self):
        self.SW[0] = self.SW[0].__and__(self.not_CC_mask).__or__(self.CC_equal_to)
        
    def CC_gt_set(self):
        self.SW[0] = self.SW[0].__and__(self.not_CC_mask).__or__(self.CC_greater_than)
        
    def CC_lt_set(self):
        self.SW[0] = self.SW[0].__and__(self.not_CC_mask).__or__(self.CC_less_than)

