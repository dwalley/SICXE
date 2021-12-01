# Module which defines how the ALU works

from math import *

class ALU():
    def __init__(self,the_registers,the_memory,the_io_supervisor):
        self.my_registers = the_registers
        self.my_memory = the_memory
        self.my_io_supervisor = the_io_supervisor
        self.running = False
        self.current_opcode_operand = []
        self.instruction_word_length = 3 # may change as new instructions are fetched
        self.n_bit = 0 # for addressing mode of current instruction
        self.i_bit = 0 # for addressing mode of current instruction
        self.SIC_instruction_set_encode_table = \
            {'ADD':'18','ADDF':'58','AND':'40','COMP':'28','DIV':'24','J':'3C','JEQ':'30',\
             'JGT':'34','JLT':'38',\
             'JSUB':'48','LDA':'00','LDCH':'50','LDL':'08','LDX':'04','MUL':'20',\
             'OR':'44','RD':'D8',\
             'RSUB':'4C','STA':'0C','STCH':'54','STL':'14','STSW':'E8',\
             'STX':'10','SUB':'1C','TD':'E0','TIX':'2C','WD':'DC'}
        self.SIC_instruction_set_decode_table = \
            {'18':self.ADD,'40':self.AND,'28':self.COMP,'24':self.DIV,'3C':self.J,'30':self.JEQ,\
             '34':self.JGT,'38':self.JLT,\
             '48':self.JSUB,'00':self.LDA,'50':self.LDCH,'08':self.LDL,'04':self.LDX,'20':self.MUL,\
             '44':self.OR,'D8':self.RD,\
             '4C':self.RSUB,'0C':self.STA,'54':self.STCH,'14':self.STL,'E8':self.STSW,\
             '10':self.STX,'1C':self.SUB,'E0':self.TD,'2C':self.TIX,'DC':self.WD}
        self.format_1_instruction_set_decode_table = \
            { }
        self.format_2_instruction_set_decode_table = \
            { }
        self.format_3or4_instruction_set_decode_table = \
            {'58':self.ADDF, \
             '18':self.ADD,'40':self.AND,'28':self.COMP,'24':self.DIV,'3C':self.J,'30':self.JEQ,\
             '34':self.JGT,'38':self.JLT,\
             '48':self.JSUB,'00':self.LDA,'50':self.LDCH,'08':self.LDL,'04':self.LDX,'20':self.MUL,\
             '44':self.OR,'D8':self.RD,\
             '4C':self.RSUB,'0C':self.STA,'54':self.STCH,'14':self.STL,'E8':self.STSW,\
             '10':self.STX,'1C':self.SUB,'E0':self.TD,'2C':self.TIX,'DC':self.WD }
        
        self.entire_instruction_set_decode_table = {}
        self.entire_instruction_set_decode_table.update(self.format_1_instruction_set_decode_table)
        self.entire_instruction_set_decode_table.update(self.format_2_instruction_set_decode_table)
        self.entire_instruction_set_decode_table.update(self.format_3or4_instruction_set_decode_table)

        
        self.hex_decode = \
            {'00':0,'01':1,'02':2,'03':3,'04':4,'05':5,'06':6,'07':7,'08':8,'09':9,\
             '0A':10,'0B':11,'0C':12,'0D':13,'0E':14,'0F':15,\
             
             '10':16,'11':17,'12':18,'13':19,'14':20,'15':21,'16':22,'17':23,'18':24,'19':25,\
             '1A':26,'1B':27,'1C':28,'1D':29,'1E':30,'1F':31,\
             
             '20':32,'21':33,'22':34,'23':35,'24':36,'25':37,'26':38,'27':39,'28':40,'29':41,\
             '2A':42,'2B':43,'2C':44,'2D':45,'2E':46,'2F':47,\
             
             '30':48,'31':49,'32':50,'33':51,'34':52,'35':53,'36':54,'37':55,'38':56,'39':57,\
             '3A':58,'3B':59,'3C':60,'3D':61,'3E':62,'3F':63,\
             
             '40':64,'41':65,'42':66,'43':67,'44':68,'45':69,'46':70,'47':71,'48':72,'49':73,\
             '4A':74,'4B':75,'4C':76,'4D':77,'4E':78,'4F':79,\
             
             '50':80,'51':81,'52':82,'53':83,'54':84,'55':85,'56':86,'57':87,'58':88,'59':89,\
             '5A':90,'5B':91,'5C':92,'5D':93,'5E':94,'5F':95,\
             
             '60':96,'61':97,'62':98,'63':99,'64':100,'65':101,'66':102,'67':103,'68':104,'69':105,\
             '6A':106,'6B':107,'6C':108,'6D':109,'6E':110,'6F':111,\
             
             '70':112,'71':113,'72':114,'73':115,'74':116,'75':117,'76':118,'77':119,'78':120,'79':121,\
             '7A':122,'7B':123,'7C':124,'7D':125,'7E':126,'7F':127,\
             
             '80':128,'81':129,'82':130,'83':131,'84':132,'85':133,'86':134,'87':135,'88':136,'89':137,\
             '8A':138,'8B':139,'8C':140,'8D':141,'8E':142,'8F':143,\
             
             '90':144,'91':145,'92':146,'93':147,'94':148,'95':149,'96':150,'97':151,'98':152,'99':153,\
             '9A':154,'9B':155,'9C':156,'9D':157,'9E':158,'9F':159,\
             
             'A0':160,'A1':161,'A2':162,'A3':163,'A4':164,'A5':165,'A6':166,'A7':167,'A8':168,'A9':169,\
             'AA':170,'AB':171,'AC':172,'AD':173,'AE':174,'AF':175,\
             
             'B0':176,'B1':177,'B2':178,'B3':179,'B4':180,'B5':181,'B6':182,'B7':183,'B8':184,'B9':185,\
             'BA':186,'BB':187,'BC':188,'BD':189,'BE':190,'BF':191,\
             
             'C0':192,'C1':193,'C2':194,'C3':195,'C4':196,'C5':197,'C6':198,'C7':199,'C8':200,'C9':201,\
             'CA':202,'CB':203,'CC':204,'CD':205,'CE':206,'CF':207,\
             
             'D0':208,'D1':209,'D2':210,'D3':211,'D4':212,'D5':213,'D6':214,'D7':215,'D8':216,'D9':217,\
             'DA':218,'DB':219,'DC':220,'DD':221,'DE':222,'DF':223,\
             
             'E0':224,'E1':225,'E2':226,'E3':227,'E4':228,'E5':229,'E6':230,'E7':231,'E8':232,'E9':233,\
             'EA':234,'EB':235,'EC':236,'ED':237,'EE':238,'EF':239,\
             
             'F0':240,'F1':241,'F2':242,'F3':243,'F4':244,'F5':245,'F6':246,'F7':247,'F8':248,'F9':249,\
             'FA':250,'FB':251,'FC':252,'FD':253,'FE':254,'FF':255}

    def fetch_next_instruction(self):
        # internal function which fetches the next instruction
        #  returns list containing the next instruction

        # calculate the absolute address of the next instruction
        m = (self.my_registers.PC[0]*65536) + (self.my_registers.PC[1]*256) + self.my_registers.PC[2]

        x=[]

        # get the first byte of the next instruction
        first_byte = self.my_memory.ram[m]
        first_byte_without_last_two_bits = (first_byte/4)*4
        x.append(first_byte)
        first_byte_hex_string = self.convert_int_to_hex_string(x[0])
        first_byte_without_last_two_bits_string = self.convert_int_to_hex_string(\
            first_byte_without_last_two_bits)
        if first_byte_hex_string in self.format_1_instruction_set_decode_table:
            # we  have a format 1, 1 byte instruction
            self.increment_program_counter(1)
            return x
        elif first_byte_hex_string in self.format_1_instruction_set_decode_table:
            # we have a format 2, 2 byte instruction
            x.append(self.my_memory.ram[m+1])
            self.increment_program_counter(2)
            return x
        elif first_byte_without_last_two_bits_string in self.format_3or4_instruction_set_decode_table:
            # we have a format 3 or 4 instruction
            #  get the next two bytes
            x.append(self.my_memory.ram[m+1])
            x.append(self.my_memory.ram[m+2])
            # figure out if we are dealing with a format 3 or format 4, check bit e
            if (x[1] % 32)/16 == 0:
                # we have format 3
                self.increment_program_counter(3)
            elif (x[1] % 32)/16 == 1:
                # we have format 4
                x.append(self.my_memory.ram[m+3])
                self.increment_program_counter(4)
            else:
                raise instruction_format_error
        else:
            raise instruction_not_found

        self.current_opcode_operand = x
            
        return x


    def execute_instruction(self,instruction_word):
        # internal function which takes a list representing an instruction with operand
        # decodes the instruction and executes it

        #decode the instruction

        index = self.convert_int_to_hex_string((instruction_word[0]/4)*4)
        instruction = self.entire_instruction_set_decode_table[index]

        # build the operand for the instruction in the form of an integer i
        i=None
        self.instruction_word_length = len(instruction_word)
        if self.instruction_word_length == 1:
            i = None
        else:
            i = 0
            
        power = 1

        for j in range(len(instruction_word)-1,0,-1):
            i += instruction_word[j] *power
            power *= 256

        # set the addressing mode bits
        self.n_bit = (instruction_word[0] % 4) / 2
        self.i_bit = instruction_word[0] % 2

        # execute the instruction
        instruction(i)

        return
    
    def received_clock_tic(self):
        # executes ALU logic associated with a tic of the clock
        #  Note: execution of a single instruction takes one clock tic

        if self.running:

            x = self.fetch_next_instruction()
                            
            # update data for the display            
            self.current_opcode_operand[0] = x[0]
            if len(x) == 2:
                self.current_opcode_operand[1] = x[1]
                self.current_opcode_operand[2] = 0
            elif len(x) == 3:
                self.current_opcode_operand[1] = x[1]
                self.current_opcode_operand[2] = x[2]
            elif len(x) == 4:
                self.current_opcode_operand[1] = x[1]
                self.current_opcode_operand[2] = x[2]
                self.current_opcode_operand[3] = x[3]

            self.execute_instruction(x)
        return

    def step(self):
        # execute a single instruction, whether or not machine is running
        
        self.current_opcode_operand = self.fetch_next_instruction()
        self.execute_instruction(self.current_opcode_operand)
        self.increment_program_counter(len(self.current_opcode_operand))
        return

    def increment_program_counter(self,num_bytes):
        # increment the PC register by num_bytes
        #  Note that if incrementing PC results in register overflow, the register is left unchanged

        for i in range(0,num_bytes):

            if self.my_registers.PC[2] == 255:
                if self.my_registers.PC[1] == 255:
                    if self.my_registers.PC[0] == 255:
                        raise Address_out_of_range
                    else:
                        self.my_registers.PC[0] += 1
                    self.my_registers.PC[1] = 0
                else:
                    self.my_registers.PC[1] += 1
                self.my_registers.PC[2] = 0
            else:
                self.my_registers.PC[2] += 1

        return
    
    def absolute_address(self,i):
        # internal function which takes into account address mode, instruction format,
        # and indexing, and returns an absolute memory location
        # starts with an integer representation of the operand data
        #  returns an integer representation of the absolute RAM address


        if self.i_bit == 1 and self.n_bit == 0: # we have immediate addressing, raise an error
            raise immediate_addressing_in_absolute_address
        elif self.i_bit == 0 and self.n_bit == 0: # we have SIC compatible simple addressing            # figure out if we are using indexed addressing
            if i/32768 >= 1: # we are, high order bit set
                m = (i - (i/32768)*32768) + self.my_registers.X[2] + \
                    self.my_registers.X[1]*256 + self.my_registers.X[0]*65536
                if m > self.my_memory.max_index:
                    raise address_out_of_range
            elif i > self.my_memory.max_index:
                raise address_out_of_range
            else:
                m=i
        elif self.i_bit == 1 and self.n_bit == 1: # we have simple addressing with possible indexing
            if self.instruction_word_length == 3: # we have a format 3 instruction
                x_bit = (i/32768)
                b_bit = (i/16382)%2
                p_bit = (i/8192)%2
                disp = i % 4096
                offset = 0
                if x_bit == 1: # add in the X register offset
                    offset = self.my_registers.X[2] + \
                             self.my_registers.X[1]*256 + self.my_registers.X[0]*65536
                if (b_bit == 1) and (p_bit == 0): #add in the base register offset
                    offset += self.my_registers.B[2] + \
                              self.my_registers.B[1]*256 + self.my_registers.B[0]*65536
                elif (b_bit == 0) and (p_bit == 1): # add in the program counter offset
                    offset += self.my_registers.PC[2] + \
                              self.my_registers.PC[1]*256 + self.my_registers.PC[0]*65536
                elif (b_bit == 0) and (p_bit == 0): # no addition to the offset
                    pass
                else: # invalid combination
                    raise invalid_indexing_in_absolute_address
                m = disp + offset
                
            elif self.instruction_word_length == 4: # we have a format 4 instruction
                x_bit = i/(2**23)
                b_bit = (i/(2**22))%2
                p_bit = (i/(2**21))%2
                address = i % (2**20)
                if (b_bit <> 0) or (p_bit <> 0): # invalid instruction, must be set to 0 for format 4
                    raise invalid_format4_in_absolute_address
                offset = 0
                if x_bit == 1: # add in the X register offset
                    offset = self.my_registers.X[2] + \
                             self.my_registers.X[1]*256 + self.my_registers.X[0]*65536
                m = address + offset
                
            else:
                raise invalid_instruction_word_length_absolute_address_simple_addressing

        elif self.i_bit == 0 and self.n_bit == 1: # we have indirect addressing with possible indexing
            if self.instruction_word_length == 3: # we have a format 3 instruction
                x_bit = (i/32768)
                b_bit = (i/16382)%2
                p_bit = (i/8192)%2
                disp = i % 4096
                offset = 0
                if x_bit == 1: # add in the X register offset
                    offset += self.my_registers.X[2] + \
                             self.my_registers.X[1]*256 + self.my_registers.X[0]*65536
                if (b_bit == 1) and (p_bit == 0): #add in the base register offset
                    offset += self.my_registers.B[2] + \
                              self.my_registers.B[1]*256 + self.my_registers.B[0]*65536
                elif (b_bit == 0) and (p_bit == 1): # add in the program counter offset
                    offset += self.my_registers.PC[2] + \
                              self.my_registers.PC[1]*256 + self.my_registers.PC[0]*65536
                elif (b_bit == 0) and (p_bit == 0): # no addition to the offset
                    pass
                else: # invalid combination
                    raise invalid_indexing_in_absolute_address
                j = disp + offset
                
            elif self.instruction_word_length == 4: # we have a format 4 instruction
                x_bit = i/(2**23)
                b_bit = (i/(2**22))%2
                p_bit = (i/(2**21))%2
                address = i % (2**20)
                if (b_bit <> 0) or (p_bit <> 0): # invalid instruction, must be set to 0 for format 4
                    raise invalid_format4_in_absolute_address
                offset = 0
                if x_bit == 1: # add in the X register offset
                    offset = self.my_registers.X[2] + \
                             self.my_registers.X[1]*256 + self.my_registers.X[0]*65536
                j = address + offset
                
            else:
                raise invalid_instruction_word_length_absolute_address_simple_addressing

            # now go get the address pointed to by the data starting at absolute memory location j
            m = self.my_memory.ram[j]*(2**16) + self.my_memory.ram[j+1]*(2**8) + \
                self.my_memory.ram[j+2]

        else:
            print("n bit and i bit are",self.n_bit,self.i_bit)
            raise invalid_address_mode_in_absolute_address
                       
        return m
    

    def ADD(self,i):
        # assumes that self. instruction_word_length, self.n_bit,
        #   and self.i_bit have been previously correctly set
        # i is an integer representation of the operand
        # A <- (A) + (m..m+2)
        #   possibly dealing with negative numbers


        if self.n_bit == 0 and self.i_bit == 1: # we have immediate addressing
            if self.instruction_word_length == 3: # we have a format 3 instruction (16 bit integer)
                x=i
            elif self.instruction_word_length == 4: # we have a format 4 instruction
                x=self.convert_twos_compliment_immediate_to_int(i)
            else:
                raise ADD_invalid_word_length
        else:
            x = self.convert_twos_compliment_mem_to_int(i)

            
        y = self.convert_twos_compliment_A_to_int()           
        z = x+y

        self.convert_int_to_twos_compliment_in_A(z)

        return

    def ADDF(self,i):
        # FIXME
        # i is an address pointing to 6 consecutive bytes in memory representing a floating point
        # number,
        # F <- (F) + (m..m+5)

        addend = bytearray(6)
        m = self.absolute_address(i)
        register_exponent,sign = self.extract_exponent_from_byte_array_float(self.my_registers.F)
        
        return
        
            
    def AND(self,i):      
        # assumes that self. instruction_word_length, self.n_bit,
        #   and self.i_bit have been previously correctly set
        # i is an integer representation of the operand
        # A <- (A) & (m..m+2)

        if self.n_bit == 0 and self.i_bit == 1: # we have immediate addressing
            if self.instruction_word_length == 3: # we have a format 3 instruction (16 bit integer)
                self.my_registers.A[0] = 0
                self.my_registers.A[1] = self.my_registers.A[1].__and__(i/(2**8))
                self.my_registers.A[2] = self.my_registers.A[2].__and__(i%(2**8))
                
            elif self.instruction_word_length == 4: # we have a format 4 instruction
                self.my_registers.A[0] = self.my_registers.A[0].__and__(i/(2**16))
                self.my_registers.A[1] = self.my_registers.A[1].__and__((i/2**8)%2**8)
                self.my_registers.A[2] = self.my_registers.A[2].__and__(i%(2**8))
            else:
                raise AND_invalid_word_length
        else:

            m = self.absolute_address(i)

            self.my_registers.A[0] = self.my_registers.A[0].__and__(self.my_memory.ram[m])
            self.my_registers.A[1] = self.my_registers.A[1].__and__(self.my_memory.ram[m+1])
            self.my_registers.A[2] = self.my_registers.A[2].__and__(self.my_memory.ram[m+2])

        return

    def COMP(self,i):
        # assumes that self. instruction_word_length, self.n_bit,
        #   and self.i_bit have been previously correctly set
        # i is an integer representation of the operand
        # (A) : (m..m+2) C
        
        if self.n_bit == 0 and self.i_bit == 1: # we have immediate addressing
            if self.instruction_word_length == 3: # we have a format 3 instruction (16 bit integer)
                m0=0
                m1=i/2**8
                m2=i%2**8                
            elif self.instruction_word_length == 4: # we have a format 4 instruction
                m0=i/(2**16)
                m1=(i/2**8)%2**8
                m2=i%(2**8)
            else:
                raise COMP_invalid_word_length
        else:
            m = self.absolute_address(i)
            m0=self.my_memory.ram[m]
            m1=self.my_memory.ram[m+1]
            m2=self.my_memory.ram[m+2]

        # compare high order bits
        if self.my_registers.A[0] < m0:
            self.my_registers.CC_lt_set()
        elif self.my_registers.A[0] > m0:
            self.my_registers.CC_gt_set()

        # compare middle order bits
        elif self.my_registers.A[1] < m1:
            self.my_registers.CC_lt_set()
        elif self.my_registers.A[1] > m1:
            self.my_registers.CC_gt_set()
            
        # compare low order bits
        elif self.my_registers.A[2] < m2:
            self.my_registers.CC_lt_set()
        elif self.my_registers.A[2] > m2:
            self.my_registers.CC_gt_set()

        # the two words are equal
        else:
            self.my_registers.CC_eq_set()

        return

    def DIV(self,i):
        # assumes that self. instruction_word_length, self.n_bit,
        #   and self.i_bit have been previously correctly set
        # i is an integer representation of the operand
        # (A) <- (A) / (m..m+2)
        
        if self.n_bit == 0 and self.i_bit == 1: # we have immediate addressing
            if self.instruction_word_length == 3: # we have a format 3 instruction (16 bit integer)
                m0=0
                m1=i/2**8
                m2=i%2**8                
            elif self.instruction_word_length == 4: # we have a format 4 instruction
                m0=i/(2**16)
                m1=(i/2**8)%2**8
                m2=i%(2**8)
            else:
                raise DIV_invalid_word_length
        else:
            m = self.absolute_address(i)
            m0=self.my_memory.ram[m]
            m1=self.my_memory.ram[m+1]
            m2=self.my_memory.ram[m+2]
            
        iprime = m0*2**16+m1*2**8+m2

        x = self.convert_twos_compliment_immediate_to_int(iprime)
        y = self.convert_twos_compliment_A_to_int()
       
        z = y/x

        self.convert_int_to_twos_compliment_in_A(z)

        return
        
    def J(self,i):
        # assumes that self. instruction_word_length, self.n_bit,
        #   and self.i_bit have been previously correctly set
        # i is an integer representation of the operand
        # PC <- m

        if self.n_bit == 0 and self.i_bit == 1: # we have immediate addressing
            if self.instruction_word_length == 3: # we have a format 3 instruction
                self.my_registers.PC[0] = 0
                self.my_registers.PC[1] = i/(2**8)
                self.my_registers.PC[2] = i % (2**8)
            elif self.instruction_word_length == 4: # we have a format 4 instruction
                self.my_registers.PC[0] = i/(2**16)
                self.my_registers.PC[1] = ((i/(2**8)) % (2**8))
                self.my_registers.PC[2] = i % (2**8)
            else:
                raise J_invalid_word_length
        else:

            m = self.absolute_address(i)

            self.my_registers.PC[0] = m/(2**16)
            self.my_registers.PC[1] = ((m/(2**8)) % (2**8))
            self.my_registers.PC[2] = m % (2**8)

        return

    def JEQ(self,i):
        # assumes that self. instruction_word_length, self.n_bit,
        #   and self.i_bit have been previously correctly set
        # i is an integer representation of the operand
        # PC <- i if CC set to =

        if self.my_registers.CC_eq_query():
            self.J(i)

    def JGT(self,i):
        # assumes that self. instruction_word_length, self.n_bit,
        #   and self.i_bit have been previously correctly set
        # i is an integer representation of the operand
        # PC <- i if CC set to =

        if self.my_registers.CC_gt_query():
            self.J(i)

    def JLT(self,i):
        # assumes that self. instruction_word_length, self.n_bit,
        #   and self.i_bit have been previously correctly set
        # i is an integer representation of the operand
        # PC <- i if CC set to =

        if self.my_registers.CC_lt_query():
            self.J(i)

    def JSUB(self,i):
        # assumes that self. instruction_word_length, self.n_bit,
        #   and self.i_bit have been previously correctly set
        # i is an integer representation of the operand
        # L <- PC, PC <- m

        self.my_registers.L[0] = self.my_registers.PC[0]
        self.my_registers.L[1] = self.my_registers.PC[1]
        self.my_registers.L[2] = self.my_registers.PC[2]

        # now load i into PC
        self.J(i)

    def LDA(self,i):
        # assumes that self. instruction_word_length, self.n_bit,
        #   and self.i_bit have been previously correctly set
        # i is an integer representation of the operand
        # A <- (m..m+2)

        if self.n_bit == 0 and self.i_bit == 1: # we have immediate addressing
            if self.instruction_word_length == 3: # we have a format 3 instruction
                self.my_registers.A[0] = 0
                self.my_registers.A[1] = i/(2**8)
                self.my_registers.A[2] = i % (2**8)
            elif self.instruction_word_length == 4: # we have a format 4 instruction
                self.my_registers.A[0] = i/(2**16)
                self.my_registers.A[1] = ((i/(2**8)) % (2**8))
                self.my_registers.A[2] = i % (2**8)
            else:
                raise LDA_invalid_word_length
        else:

            m = self.absolute_address(i)

            self.my_registers.A[0] = self.my_memory.ram[m]
            self.my_registers.A[1] = self.my_memory.ram[m+1]
            self.my_registers.A[2] = self.my_memory.ram[m+2]

        return

    def LDCH(self,i):
        # assumes that self. instruction_word_length, self.n_bit,
        #   and self.i_bit have been previously correctly set
        # i is an integer representation of the operand
        # A[rightmost byte] <- (m)
        
        if self.n_bit == 0 and self.i_bit == 1: # we have immediate addressing
            if self.instruction_word_length == 3: # we have a format 3 instruction
                self.my_registers.A[2] = i % (2**8)
            elif self.instruction_word_length == 4: # we have a format 4 instruction
                self.my_registers.A[2] = i % (2**8)
            else:
                raise LDA_invalid_word_length
        else:

            m = self.absolute_address(i)

            self.my_registers.A[2] = self.my_memory.ram[m]
            
        return

    def LDL(self,i):
        # assumes that self. instruction_word_length, self.n_bit,
        #   and self.i_bit have been previously correctly set
        # i is an integer representation of the operand
        # L <- (m..m+2)

        if self.n_bit == 0 and self.i_bit == 1: # we have immediate addressing
            if self.instruction_word_length == 3: # we have a format 3 instruction
                self.my_registers.L[0] = 0
                self.my_registers.L[1] = i/(2**8)
                self.my_registers.L[2] = i % (2**8)
            elif self.instruction_word_length == 4: # we have a format 4 instruction
                self.my_registers.L[0] = i/(2**16)
                self.my_registers.L[1] = ((i/(2**8)) % (2**8))
                self.my_registers.L[2] = i % (2**8)
            else:
                raise LDL_invalid_word_length
        else:

            m = self.absolute_address(i)

            self.my_registers.L[0] = self.my_memory.ram[m]
            self.my_registers.L[1] = self.my_memory.ram[m+1]
            self.my_registers.L[2] = self.my_memory.ram[m+2]

        return

    def LDX(self,i):
        # assumes that self. instruction_word_length, self.n_bit,
        #   and self.i_bit have been previously correctly set
        # i is an integer representation of the operand
        # X <- (m..m+2)

        if self.n_bit == 0 and self.i_bit == 1: # we have immediate addressing
            if self.instruction_word_length == 3: # we have a format 3 instruction
                self.my_registers.X[0] = 0
                self.my_registers.X[1] = i/(2**8)
                self.my_registers.X[2] = i % (2**8)
            elif self.instruction_word_length == 4: # we have a format 4 instruction
                self.my_registers.X[0] = i/(2**16)
                self.my_registers.X[1] = ((i/(2**8)) % (2**8))
                self.my_registers.X[2] = i % (2**8)
            else:
                raise LDX_invalid_word_length
        else:

            m = self.absolute_address(i)

            self.my_registers.X[0] = self.my_memory.ram[m]
            self.my_registers.X[1] = self.my_memory.ram[m+1]
            self.my_registers.X[2] = self.my_memory.ram[m+2]

        return

    def MUL(self,i):
        # assumes that self. instruction_word_length, self.n_bit,
        #   and self.i_bit have been previously correctly set
        # i is an integer representation of the operand
        # (A) <- (A) * (m..m+2)
        
        if self.n_bit == 0 and self.i_bit == 1: # we have immediate addressing
            if self.instruction_word_length == 3: # we have a format 3 instruction (16 bit integer)
                m0=0
                m1=i/2**8
                m2=i%2**8                
            elif self.instruction_word_length == 4: # we have a format 4 instruction
                m0=i/(2**16)
                m1=(i/2**8)%2**8
                m2=i%(2**8)
            else:
                raise DIV_invalid_word_length
        else:
            m = self.absolute_address(i)
            m0=self.my_memory.ram[m]
            m1=self.my_memory.ram[m+1]
            m2=self.my_memory.ram[m+2]
            
        iprime = m0*2**16+m1*2**8+m2

        x = self.convert_twos_compliment_immediate_to_int(iprime)
        y = self.convert_twos_compliment_A_to_int()
       
        z = x * y

        self.convert_int_to_twos_compliment_in_A(z)

        return

    def OR(self,i):
        # assumes that self. instruction_word_length, self.n_bit,
        #   and self.i_bit have been previously correctly set
        # i is an integer representation of the operand
        # A <- (A) | (m..m+2)
        if self.n_bit == 0 and self.i_bit == 1: # we have immediate addressing
            if self.instruction_word_length == 3: # we have a format 3 instruction (16 bit integer)
                m0=0
                m1=i/2**8
                m2=i%2**8                
            elif self.instruction_word_length == 4: # we have a format 4 instruction
                m0=i/(2**16)
                m1=(i/2**8)%2**8
                m2=i%(2**8)
            else:
                raise DIV_invalid_word_length
        else:
            m = self.absolute_address(i)
            m0=self.my_memory.ram[m]
            m1=self.my_memory.ram[m+1]
            m2=self.my_memory.ram[m+2]

        self.my_registers.A[0] = self.my_registers.A[0].__or__(m0)
        self.my_registers.A[1] = self.my_registers.A[1].__or__(m1)
        self.my_registers.A[2] = self.my_registers.A[2].__or__(m2)

    def RD(self,i):
        # assumes that self. instruction_word_length, self.n_bit,
        #   and self.i_bit have been previously correctly set
        # i is an integer representation of the operand
        # A[rightmost byte] <- data from device specified (m)

        # switch to supervisor mode
        self.my_registers.SW[0]=self.my_registers.SW[0].__or__(self.my_registers.supervisor_mode_mask)

        if self.my_registers.SW[0].__and__(self.my_registers.supervisor_mode_mask) == 0:
            raise RD_privileged_instruction_in_user_mode
        else:
            if self.n_bit == 0 and self.i_bit == 1: # we have immediate addressing
                if self.instruction_word_length == 3: # we have a format 3 instruction (16 bit integer)
                    m0=0
                    m1=i/2**8
                    m2=i%2**8                
                elif self.instruction_word_length == 4: # we have a format 4 instruction
                    m0=i/(2**16)
                    m1=(i/2**8)%2**8
                    m2=i%(2**8)
                else:
                    raise DIV_invalid_word_length
            else:
                m = self.absolute_address(i)
                m0=self.my_memory.ram[m]
                m1=self.my_memory.ram[m+1]
                m2=self.my_memory.ram[m+2]

            self.my_registers.A[2] = self.my_io_supervisor.read_character( (m0*65536)+(m1*256)+m2 )

        #switch back to user mode
        self.my_registers.SW[0].__and__(self.my_registers.not_supervisor_mode_mask)

        return

    def RSUB(self,i):
        # note i which is part of the instruction format is not used
        # PC <- (L)

        self.my_registers.PC[0] = self.my_registers.L[0]
        self.my_registers.PC[1] = self.my_registers.L[1]
        self.my_registers.PC[2] = self.my_registers.L[2]

        return

    def STA(self,i):
        # assumes that self. instruction_word_length, self.n_bit,
        #   and self.i_bit have been previously correctly set
        # i is an integer representation of the operand
        # m..m+2 <- (A)
        
        if self.n_bit == 0 and self.i_bit == 1: # we have immediate addressing
            if self.instruction_word_length == 3: # we have a format 3 instruction (16 bit integer)
                m=i              
            elif self.instruction_word_length == 4: # we have a format 4 instruction
                m=i%(2**20)
            else:
                raise DIV_invalid_word_length
        else:
            m = self.absolute_address(i)

        self.my_memory.ram[m+0] = self.my_registers.A[0]
        self.my_memory.ram[m+1] = self.my_registers.A[1]
        self.my_memory.ram[m+2] = self.my_registers.A[2]

        return

    def STCH(self,i):
        # assumes that self. instruction_word_length, self.n_bit,
        #   and self.i_bit have been previously correctly set
        # i is an integer representation of the operand
        # m <- (A) [rightmost byte]

        if self.n_bit == 0 and self.i_bit == 1: # we have immediate addressing
            if self.instruction_word_length == 3: # we have a format 3 instruction (16 bit integer)
                m=i              
            elif self.instruction_word_length == 4: # we have a format 4 instruction
                m=i%(2**20)
            else:
                raise DIV_invalid_word_length
        else:
            m = self.absolute_address(i)

        self.my_memory.ram[m] = self.my_registers.A[2]

        return

    def STL(self,i):
        # i is address pointing to 3 consecutive bytes in memory
        # assumes that self. instruction_word_length, self.n_bit,
        #   and self.i_bit have been previously correctly set
        # i is an integer representation of the operand
        # m..m+2 <- (L)
        
        if self.n_bit == 0 and self.i_bit == 1: # we have immediate addressing
            if self.instruction_word_length == 3: # we have a format 3 instruction (16 bit integer)
                m=i              
            elif self.instruction_word_length == 4: # we have a format 4 instruction
                m=i%(2**20)
            else:
                raise DIV_invalid_word_length
        else:
            m = self.absolute_address(i)

        self.my_memory.ram[m+0] = self.my_registers.L[0]
        self.my_memory.ram[m+1] = self.my_registers.L[1]
        self.my_memory.ram[m+2] = self.my_registers.L[2]

        return

    def STSW(self,i):
        # i is address pointing to 3 consecutive bytes in memory
        # assumes that self. instruction_word_length, self.n_bit,
        #   and self.i_bit have been previously correctly set
        # i is an integer representation of the operand
        # m..m+1 <- (SW)

        if (self.my_registers.SW[0].__and__(self.my_registers.supervisor_mode_mask) == \
            self.my_registers.supervisor_mode_mask):

            if self.n_bit == 0 and self.i_bit == 1: # we have immediate addressing
                if self.instruction_word_length == 3: # we have a format 3 instruction (16 bit integer)
                    m=i              
                elif self.instruction_word_length == 4: # we have a format 4 instruction
                    m=i%(2**20)
                else:
                    raise DIV_invalid_word_length
            else:
                m = self.absolute_address(i)

                self.my_memory.ram[m] = self.my_registers.SW[0]
                self.my_memory.ram[m+1] = self.my_registers.SW[1]
                self.my_memory.ram[m+2] = self.my_registers.SW[2]

        else:
            raise Privileged_instruction_in_user_mode

        return

    def STX(self,i):
        # i is address pointing to 3 consecutive bytes in memory
        # assumes that self. instruction_word_length, self.n_bit,
        #   and self.i_bit have been previously correctly set
        # i is an integer representation of the operand
        # m..m+2 <- (X)
        
        if self.n_bit == 0 and self.i_bit == 1: # we have immediate addressing
            if self.instruction_word_length == 3: # we have a format 3 instruction (16 bit integer)
                m=i              
            elif self.instruction_word_length == 4: # we have a format 4 instruction
                m=i%(2**20)
            else:
                raise DIV_invalid_word_length
        else:
            m = self.absolute_address(i)

        self.my_memory.ram[m+0] = self.my_registers.X[0]
        self.my_memory.ram[m+1] = self.my_registers.X[1]
        self.my_memory.ram[m+2] = self.my_registers.X[2]

        return

    def SUB(self,i):
        # assumes that self. instruction_word_length, self.n_bit,
        #   and self.i_bit have been previously correctly set
        # i is an integer representation of the operand
        # A <- (A) - (m..m+2)
        #   possibly dealing with negative numbers

        if self.n_bit == 0 and self.i_bit == 1: # we have immediate addressing
            if self.instruction_word_length == 3: # we have a format 3 instruction (16 bit integer)
                x=i
            elif self.instruction_word_length == 4: # we have a format 4 instruction
                x=self.convert_twos_compliment_immediate_to_int(i)
            else:
                raise ADD_invalid_word_length
        else:
            x = self.convert_twos_compliment_mem_to_int(i)

            
        y = self.convert_twos_compliment_A_to_int()           
        z = y-x

        self.convert_int_to_twos_compliment_in_A(z)

        return
            
    def TD(self,i):
        # assumes that self. instruction_word_length, self.n_bit,
        #   and self.i_bit have been previously correctly set
        # i is an integer representation of the operand
        # test device specified by (m), sets condition code

        # switch to supervisor mode
        self.my_registers.SW[0]=self.my_registers.SW[0].__or__(self.my_registers.supervisor_mode_mask)

        if self.my_registers.SW[0].__and__(self.my_registers.supervisor_mode_mask) == 0:
            raise privileged_instruction_in_user_mode
        else:
            if self.n_bit == 0 and self.i_bit == 1: # we have immediate addressing
                if self.instruction_word_length == 3: # we have a format 3 instruction (16 bit integer)
                    m=i                
                elif self.instruction_word_length == 4: # we have a format 4 instruction
                    m=i%(2**20)
                else:
                    raise DIV_invalid_word_length
            else:
                m = self.absolute_address(i)
            device = self.my_memory.ram[m]
            result = self.my_io_supervisor.test_device(device)

            self.my_registers.SW[0] = self.my_registers.SW[0].__and__(self.my_registers.not_CC_mask).\
                                      __or__(result)

        #switch back to user mode
        self.my_registers.SW[0]=self.my_registers.SW[0].\
                                 __and__(self.my_registers.not_supervisor_mode_mask)

        return

    def TIX(self,i):
        # i is address pointing to 3 consecutive bytes in memory
        #  might possibly have an indexing bit set
        # X <- (X) + 1; (X) : (m..m+2) setting condition code

        m = self.absolute_address(i)

        # increment the index register X
        #  Note that if incrementing X results in register overflow, the register is left unchanged

        if self.my_registers.X[2] == 255:
            if self.my_registers.X[1] == 255:
                if self.my_registers.X[0] == 255:
                    raise Arithemetic_overflow
                else:
                    self.my_registers.X[0] += 1
                self.my_registers.X[1] = 0
            else:
                self.my_registers.X[1] += 1
            self.my_registers.X[2] = 0
        else:
            self.my_registers.X[2] += 1

        # now do the comparison

        # compare high order bits
        if self.my_registers.X[0] < self.my_memory.ram[m]:
            self.my_registers.CC_lt_set()
        elif self.my_registers.X[0] > self.my_memory.ram[m]:
            self.my_registers.CC_gt_set()

        # compare middle order bits
        elif self.my_registers.X[1] < self.my_memory.ram[m+1]:
            self.my_registers.CC_lt_set()
        elif self.my_registers.X[1] > self.my_memory.ram[m+1]:
            self.my_registers.CC_gt_set()
            
        # compare low order bits
        elif self.my_registers.X[2] < self.my_memory.ram[m+2]:
            self.my_registers.CC_lt_set()
        elif self.my_registers.X[2] > self.my_memory.ram[m+2]:
            self.my_registers.CC_gt_set()

        # the two words are equal
        else:
            self.my_registers.CC_eq_set()

    def WD(self,i):
        # i is address pointing to 3 consecutive bytes in memory
        #  might possibly have an indexing bit set
        # Device specified by (m) <- (A) rightmost byte

        # switch to supervisor mode
        self.my_registers.SW[0]=self.my_registers.SW[0].__or__(self.my_registers.supervisor_mode_mask)

        if self.my_registers.SW[0].__and__(self.my_registers.supervisor_mode_mask) == 0:
            raise privileged_instruction_in_user_mode
        else:
            
            m = self.absolute_address(i)
            device = (self.my_memory.ram[m]*65536)+(self.my_memory.ram[m+1]*256)+self.my_memory.ram[m+2]

            self.my_io_supervisor.write_character(device,self.my_registers.A[2])

        #switch back to user mode
        self.my_registers.SW[0].__and__(self.my_registers.not_supervisor_mode_mask)


    
    def convert_byte_array_float_to_float(self,float_array):
        # convert a 6 byte array representation of a floating point number to
        # a Python float number
        
        exponent,sign = self.extract_exponent_from_byte_array_float(float_array)
        
        # create a string of 1's and 0's representing the fractional part of the number
        zeros = '00000000'
        bit_string = bin(float_array[1]%16)[2:]
        if len(bit_string) <> 4: # we have a unnormalized number, handle it anyway
            bit_string = zeros[0:4-len(bit_string)]+bit_string
        for i in range(2,6):
            temp_string = bin(float_array[i])[2:]
            if len(temp_string) <> 8: # pad with leading zero's
                temp_string = zeros[0:8-len(temp_string)]+temp_string
            bit_string += temp_string
        fraction = 0
        for i in range(0,36):
            if bit_string[i] == '1': # add the appropriate amoint to the fraction
                fraction += float(1)/((2**i)+1)
        return sign*(2**exponent)*fraction

    def extract_exponent_from_byte_array_float(self,float_array):
        
        if float_array[0]/128 == 1: #high order bit is set, we have a negative number
            sign = -1
            high_exponent = (float_array[0] - 128)*16              
        else:
            sign = 1
            high_exponent = float_array[0]*16
        low_exponent = float_array[1]/16
        uncorrected_exponent = low_exponent+high_exponent
        exponent = uncorrected_exponent - 1024

        return exponent,sign
        
    def convert_float_to_byte_array_float(self,my_number):
        # DUBIOUS ACCURACY
        # FIX ME
        # NEED TO CODE INTERNAL FLOATING POINT FUNCTIONS BY HAND
        #converts a python number into the SIC-XE bytearray representation of a float
        float_result = bytearray(6)
        (mantissa,exponent) = frexp(my_number)
        if mantissa <= 0:
            sign_bit_string = '1'
            mantissa *= -1
        else:
            sign_bit_string = '0'
        exponent += 1024
        exponent_string = ''
        if exponent < 0 or exponent > 2047:
            raise floating_point_overflow_or_underflow
        for i in range(0,11):
            if exponent/(2**(10-i)) == 1:
                exponent_string += '1'
                # strip off the leading digit
                exponent = exponent - (exponent/(2**(10-i)))*(2**(10-i))
            else:
                exponent_string += '0'
        mantissa_string = ''
        big_mantissa = int(mantissa*(2**36))
        for i in range(0,36):
            if big_mantissa/(2**(35-i)) >= 1: #the leading digit is a 1
                mantissa_string += '1'
            else: #the leading digit is a 0
                mantissa_string += '0'
            big_mantissa /= 2
            
##            if mantissa*2.0 >= 1.0: #leading digit is a 1
##                mantissa_string += '1'
##                mantissa = (mantissa * 2.0) -1.0
##            else:
##                mantissa_string += '0'
##                mantissa *= 2.0
        representation_string = sign_bit_string+exponent_string+mantissa_string
        my_result = self.convert_string_float_to_byte_array(representation_string)
        return my_result

    def convert_string_float_to_byte_array(self,representation_string):
        # assumes a valid representation string
        my_result = bytearray(6)
        for i in range(0,6):
            for j in range(0,8):
                if representation_string[(i*8)+j] == '1':
                    my_result[i] += 2**(7-j)
        return my_result

    def convert_int_to_hex_string(self,i):
        # internal function which converts an integer to a hexadecimal string
        # 0 <= i <= 255
        hex_letters = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        high_hex_index = i/16
        low_hex_index = i - (high_hex_index*16)
        return hex_letters[high_hex_index]+hex_letters[low_hex_index]


    def convert_int_to_twos_compliment_in_A(self,z):
        # internal function which takes an integer z and converts it to a 3-byte 2's compliment
        # representation, storing result in register A
        if (z > ((2**23)-1)) or (z < (-1*(2**23))):
            raise arimetic_overflow
        else:
            if z >= 0:
                # store low order byte
                self.my_registers.A[2] = z - ((z/256)*256)
                # shift right 8 bits
                z = z/256
                #store middle order byte
                self.my_registers.A[1] = z - ((z/256)*256)
                #store high order byte
                self.my_registers.A[0] = z/256
            else: # we are dealing with a negative number
                #complement the number
                temp = -1*(z+1)
                temp = ((2**23)-1) - temp
                #set the high order bit
                temp += 2**23
                # store result
                # store low order byte
                self.my_registers.A[2] = temp - ((temp/256)*256)
                # shift right 8 bits
                temp = temp/256
                #store middle order byte
                self.my_registers.A[1] = temp - ((temp/256)*256)
                #store high order byte
                self.my_registers.A[0] = temp/256

    def convert_twos_compliment_mem_to_int(self,i):
        # internal function to fetch an integer from memory location m
        #  returns an integer.

        m = self.absolute_address(i)

        if (self.my_memory.ram[m] > 128):
            # we are dealing with a negative number, need to take into account 2's compliment
            #  strip off the leading but
            y = self.my_memory.ram[m] - 128
            # add up the result
            x = (y*65536) + (self.my_memory.ram[m+1]*256) + self.my_memory.ram[m+2]
            # complement it
            x = -1 * ((2**23) - x)
        else:
            x = (self.my_memory.ram[m]*65536) + (self.my_memory.ram[m+1]*256) + self.my_memory.ram[m+2]

        return x

    def convert_twos_compliment_immediate_to_int(self,i):
        # internal function to convert a twos compliment integer to a python integer
        #  returns an integer.

        m = [i/2**16,(i/2**8)%2**8,i%2**8]

        if (m[0] > 128):
            # we are dealing with a negative number, need to take into account 2's compliment
            #  strip off the leading but
            y = m[0] - 128
            # add up the result
            x = (y*65536) + (m[1]*256) + m[2]
            # complement it
            x = -1 * ((2**23) - x)
        else:
            x = (m[0]*2**16) + (m[1]*2**8) + m[2]

        return x



    def convert_twos_compliment_A_to_int(self):
        # internal function to fetch an integer register A
        #  returns an integer.


        if (self.my_registers.A[0] > 128):
            # we are dealing with a negative number, need to take into account 2's compliment
            #  strip off the leading but
            y = self.my_registers.A[0] - 128
            # add up the result
            x = (y*65536) + (self.my_registers.A[1]*256) + self.my_registers.A[2]
            # complement it
            x = -1 * ((2**23) - x)
        else:
            x = (self.my_registers.A[0]*65536) + (self.my_registers.A[1]*256) + \
                self.my_registers.A[2]

        return x
