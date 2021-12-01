# file containing classes for exception handlers

class new_register_knob_setting(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class load_register_activated(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class stop_the_machine(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class execute_instruction_activated(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class step_activated(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class halt_machine(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class run_machine(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
