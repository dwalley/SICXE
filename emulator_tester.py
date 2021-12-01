# code for testing the machine

import random
from Machine import *

my_machine = Machine('My first SIC Machine')

print(my_machine.my_name)
print
print(my_machine.my_ALU.running)
print (my_machine.my_ALU.hex_decode)
print (my_machine.my_ALU.entire_instruction_set_decode_table)

# test internal function to convert an integer and store in it A
print("testing storing 2's compliment in A")
i=1
print("converting",i)
my_machine.my_ALU.convert_int_to_twos_compliment_in_A(i)
print("yields",my_machine.my_registers.A[0],my_machine.my_registers.A[1],my_machine.my_registers.A[2])
i=-1
print("converting",i)
my_machine.my_ALU.convert_int_to_twos_compliment_in_A(i)
print("yields",my_machine.my_registers.A[0],my_machine.my_registers.A[1],my_machine.my_registers.A[2])
i=2**23 - 1
print("converting",i)
my_machine.my_ALU.convert_int_to_twos_compliment_in_A(i)
print("yields",my_machine.my_registers.A[0],my_machine.my_registers.A[1],my_machine.my_registers.A[2])
i=-1*(2**23)
print("converting",i)
my_machine.my_ALU.convert_int_to_twos_compliment_in_A(i)
print("yields",my_machine.my_registers.A[0],my_machine.my_registers.A[1],my_machine.my_registers.A[2])

# test integer addition function
print("testing addition")
my_machine.my_memory.ram[3] = 1
my_machine.my_memory.ram[4] = 2
my_machine.my_memory.ram[5] = 3
print("adding",my_machine.my_memory.ram[3],my_machine.my_memory.ram[4],my_machine.my_memory.ram[5]," to ")
my_machine.my_registers.A[0] = 4
my_machine.my_registers.A[1] = 5
my_machine.my_registers.A[2] = 6
print(my_machine.my_registers.A[0],my_machine.my_registers.A[1],my_machine.my_registers.A[2])
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 3
my_machine.my_ALU.ADD(32768)
print("yields")
print(my_machine.my_registers.A[0],my_machine.my_registers.A[1],my_machine.my_registers.A[2])

my_machine.my_memory.ram[3] = 255
my_machine.my_memory.ram[4] = 255
my_machine.my_memory.ram[5] = 255
print("adding",my_machine.my_memory.ram[3],my_machine.my_memory.ram[4],my_machine.my_memory.ram[5]," to ")
my_machine.my_registers.A[0] = 4
my_machine.my_registers.A[1] = 5
my_machine.my_registers.A[2] = 6
print(my_machine.my_registers.A[0],my_machine.my_registers.A[1],my_machine.my_registers.A[2])
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 3
my_machine.my_ALU.ADD(32768)
print("yields")
print(my_machine.my_registers.A[0],my_machine.my_registers.A[1],my_machine.my_registers.A[2])

my_machine.my_memory.ram[3] = 1
my_machine.my_memory.ram[4] = 2
my_machine.my_memory.ram[5] = 3
print("adding",my_machine.my_memory.ram[3],my_machine.my_memory.ram[4],my_machine.my_memory.ram[5]," to ")
my_machine.my_registers.A[0] = 255
my_machine.my_registers.A[1] = 255
my_machine.my_registers.A[2] = 250
print(my_machine.my_registers.A[0],my_machine.my_registers.A[1],my_machine.my_registers.A[2])
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 3
my_machine.my_ALU.ADD(32768)
print("yields")
print(my_machine.my_registers.A[0],my_machine.my_registers.A[1],my_machine.my_registers.A[2])

my_machine.my_memory.ram[3] = 255
my_machine.my_memory.ram[4] = 255
my_machine.my_memory.ram[5] = 255
print("adding",my_machine.my_memory.ram[3],my_machine.my_memory.ram[4],my_machine.my_memory.ram[5]," to ")
my_machine.my_registers.A[0] = 255
my_machine.my_registers.A[1] = 255
my_machine.my_registers.A[2] = 255
print(my_machine.my_registers.A[0],my_machine.my_registers.A[1],my_machine.my_registers.A[2])
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 3
my_machine.my_ALU.ADD(32768)
print("yields")
print(my_machine.my_registers.A[0],my_machine.my_registers.A[1],my_machine.my_registers.A[2])

print

#test bitwise AND function
my_machine.my_memory.ram[5] = 3
my_machine.my_registers.X[2] = 3
my_machine.my_registers.A[2] = 6
my_machine.my_ALU.AND(32768)
print("6 AND 3 is:")
print(my_machine.my_registers.A[2])
print

#test comparison function
print("Testing comparison function")
my_machine.my_memory.ram[5] = 3
my_machine.my_registers.X[2] = 3
my_machine.my_registers.A[2] = 6
my_machine.my_ALU.COMP(32768)
print("6 compared to 3 is:")
print(my_machine.my_registers.SW[0])

#test comparison function
my_machine.my_memory.ram[5] = 6
my_machine.my_registers.X[2] = 3
my_machine.my_registers.A[2] = 3
my_machine.my_ALU.COMP(32768)
print("3 compared to 6 is:")
print(my_machine.my_registers.SW[0])

#test comparison function
my_machine.my_memory.ram[5] = 3
my_machine.my_registers.X[2] = 3
my_machine.my_registers.A[2] = 3
my_machine.my_ALU.COMP(32768)
print("3 compared to 3 is:")
print(my_machine.my_registers.SW[0])

#test comparison function
my_machine.my_memory.ram[5] = 6
my_machine.my_registers.X[2] = 3
my_machine.my_registers.A[2] = 3
my_machine.my_ALU.COMP(32768)
print("3 compared to 6 is:")
print(my_machine.my_registers.SW[0])

#test comparison function
my_machine.my_memory.ram[5] = 3
my_machine.my_registers.X[2] = 3
my_machine.my_registers.A[2] = 6
my_machine.my_ALU.COMP(32768)
print("6 compared to 3 is:")
print(my_machine.my_registers.SW[0])
print

# test integer division function
my_machine.my_memory.ram[3] = 0
my_machine.my_memory.ram[4] = 0
my_machine.my_memory.ram[5] = 3
my_machine.my_registers.A[0] = 0
my_machine.my_registers.A[1] = 0
my_machine.my_registers.A[2] = 6
my_machine.my_registers.X[2] = 3
my_machine.my_ALU.DIV(32768)
print("6/3 is:")
print(my_machine.my_registers.A[2])
print

# test the jump instruction
my_machine.my_registers.X[2] = 1
my_machine.my_registers.X[1] = 2
my_machine.my_ALU.J(32768+87)
print("next instruction to be fetched from:")
print(my_machine.my_registers.PC[0],my_machine.my_registers.PC[1],my_machine.my_registers.PC[2])
print

# test the JEQ instruction
my_machine.my_memory.ram[5] = 3
my_machine.my_registers.X[2] = 3
my_machine.my_registers.X[1] = 0 
my_machine.my_registers.A[2] = 3
my_machine.my_ALU.COMP(32768)
print("3 compared to 3 is:")
print(my_machine.my_registers.SW[0])
my_machine.my_registers.X[2] = 2
my_machine.my_registers.X[1] = 3
my_machine.my_ALU.JEQ(32768+87)
print("next instruction to be fetched from:")
print(my_machine.my_registers.PC[0],my_machine.my_registers.PC[1],my_machine.my_registers.PC[2])
print

# test the JGT instruction
my_machine.my_memory.ram[5] = 3
my_machine.my_registers.X[2] = 3
my_machine.my_registers.X[1] = 0 
my_machine.my_registers.A[2] = 6
my_machine.my_ALU.COMP(32768)
print("6 compared to 3 is:")
print(my_machine.my_registers.SW[0])
my_machine.my_registers.X[2] = 3
my_machine.my_registers.X[1] = 4
my_machine.my_ALU.JGT(32768+87)
print("next instruction to be fetched from:")
print(my_machine.my_registers.PC[0],my_machine.my_registers.PC[1],my_machine.my_registers.PC[2])
print

# test the JLT instruction
my_machine.my_memory.ram[5] = 6
my_machine.my_registers.X[2] = 3
my_machine.my_registers.X[1] = 0 
my_machine.my_registers.A[2] = 3
my_machine.my_ALU.COMP(32768)
print("3 compared to 6 is:")
print(my_machine.my_registers.SW[0])
my_machine.my_registers.X[2] = 4
my_machine.my_registers.X[1] = 5
my_machine.my_ALU.JLT(32768+87)
print("next instruction to be fetched from:")
print(my_machine.my_registers.PC[0],my_machine.my_registers.PC[1],my_machine.my_registers.PC[2])
print

# test the JSUB instruction
my_machine.my_registers.X[2] = 5
my_machine.my_registers.X[1] = 6
my_machine.my_ALU.JSUB(32768+87)
print("testing JSUB, next instruction to be fetched from:")
print(my_machine.my_registers.PC[0],my_machine.my_registers.PC[1],my_machine.my_registers.PC[2])
print("L register contains:")
print(my_machine.my_registers.L[0],my_machine.my_registers.L[1],my_machine.my_registers.L[2])
print

#test the LDA instruction
my_machine.my_memory.ram[5] = 6
my_machine.my_registers.X[2] = 3
my_machine.my_registers.X[1] = 0
my_machine.my_ALU.LDA(32768+0)
print("loading",my_machine.my_memory.ram[3],my_machine.my_memory.ram[4],my_machine.my_memory.ram[5]," into A results in:")
print(my_machine.my_registers.A[0],my_machine.my_registers.A[1],my_machine.my_registers.A[2])
print

#test the LDCH instruction
my_machine.my_memory.ram[5] = 7
my_machine.my_registers.X[2] = 3
my_machine.my_registers.X[1] = 0
my_machine.my_ALU.LDCH(32768+2)
print("loading",my_machine.my_memory.ram[5]," into A[2] results in:")
print(my_machine.my_registers.A[2])
print

#test the LDL instruction
my_machine.my_memory.ram[5] = 8
my_machine.my_registers.X[2] = 3
my_machine.my_registers.X[1] = 0
my_machine.my_ALU.LDL(32768+0)
print("loading",my_machine.my_memory.ram[3],my_machine.my_memory.ram[4],my_machine.my_memory.ram[5]," into L results in:")
print(my_machine.my_registers.L[0],my_machine.my_registers.L[1],my_machine.my_registers.L[2])
print

# test the MUL instruction
my_machine.my_memory.ram[3] = 0
my_machine.my_memory.ram[4] = 0
my_machine.my_memory.ram[5] = 100
my_machine.my_registers.X[2] = 3
my_machine.my_registers.X[1] = 0
print("multiplying",my_machine.my_memory.ram[3],my_machine.my_memory.ram[4],my_machine.my_memory.ram[5]," by ")
print(my_machine.my_registers.A[0],my_machine.my_registers.A[1],my_machine.my_registers.A[2]," results in")
my_machine.my_ALU.MUL(32768+0)
print(my_machine.my_registers.A[0],my_machine.my_registers.A[1],my_machine.my_registers.A[2])
print

# test the OR instruction
my_machine.my_memory.ram[3] = 64
my_machine.my_memory.ram[4] = 7
my_machine.my_memory.ram[5] = 9
print("OR",my_machine.my_memory.ram[3],my_machine.my_memory.ram[4],my_machine.my_memory.ram[5]," by ")
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 3
my_machine.my_registers.A[0] = 1
my_machine.my_registers.A[1] = 64
my_machine.my_registers.A[2] = 6
print(my_machine.my_registers.A[0],my_machine.my_registers.A[1],my_machine.my_registers.A[2]," results in")
my_machine.my_ALU.OR(32768+0)
print(my_machine.my_registers.A[0],my_machine.my_registers.A[1],my_machine.my_registers.A[2])
print

#test reading from a simulated device number 0
my_machine.my_memory.ram[3] = 0
my_machine.my_memory.ram[4] = 0
my_machine.my_memory.ram[5] = 0
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 3
my_machine.my_ALU.RD(32768+0)
print("read in character from device 00 ",my_machine.my_registers.A[2])
print

#test reading from a simulated device number 1
my_machine.my_memory.ram[3] = 0
my_machine.my_memory.ram[4] = 0
my_machine.my_memory.ram[5] = 0
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 3
my_machine.my_ALU.RD(32768+0)
print("read in character from device 00 ",my_machine.my_registers.A[2])
print

# test the RSUB instruction
my_machine.my_ALU.RSUB(32768+87)
print("testing RSUB, next instruction to be fetched from:")
print(my_machine.my_registers.PC[0],my_machine.my_registers.PC[1],my_machine.my_registers.PC[2])
print("L register contains:")
print(my_machine.my_registers.L[0],my_machine.my_registers.L[1],my_machine.my_registers.L[2])
print

# testing the STA instruction
my_machine.my_registers.A[0] = 6
my_machine.my_registers.A[1] = 7
my_machine.my_registers.A[2] = 8
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 6
my_machine.my_ALU.STA(32768+3)
print("testing STA instruction with A containing ",my_machine.my_registers.A[0],my_machine.my_registers.A[1],my_machine.my_registers.A[2])
print("results in ",my_machine.my_memory.ram[9],my_machine.my_memory.ram[10],my_machine.my_memory.ram[11])
print

# testing the STCH instruction
my_machine.my_registers.A[0] = 6
my_machine.my_registers.A[1] = 7
my_machine.my_registers.A[2] = 9
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 9
my_machine.my_ALU.STCH(32768+3)
print("testing STA instruction with A[2] containing ",my_machine.my_registers.A[2])
print("results in ",my_machine.my_memory.ram[12])
print

# testing the STL instruction
my_machine.my_registers.L[0] = 2
my_machine.my_registers.L[1] = 3
my_machine.my_registers.L[2] = 4
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 12
my_machine.my_ALU.STL(32768+3)
print("testing STL instruction with L containing ",my_machine.my_registers.L[0],my_machine.my_registers.L[1],my_machine.my_registers.L[2])
print("results in ",my_machine.my_memory.ram[15],my_machine.my_memory.ram[16],my_machine.my_memory.ram[17])
print

#testing STSW
print("testing STSW")
my_machine.my_registers.SW[0] = 2
my_machine.my_registers.SW[1] = 3
my_machine.my_registers.SW[2] = 4
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 15
# set machine to supervisor mode
print("initial SW[0] is ",my_machine.my_registers.SW[0])
my_machine.my_registers.SW[0]= my_machine.my_registers.SW[0].__or__(my_machine.my_registers.supervisor_mode_mask)
print("after switching to upervisor mode, SW[0] is",my_machine.my_registers.SW[0])
print("testing STSW instruction with SW containing ",my_machine.my_registers.SW[0],my_machine.my_registers.SW[1],my_machine.my_registers.SW[2])
my_machine.my_ALU.STSW(32768+3)
print("results in ",my_machine.my_memory.ram[18],my_machine.my_memory.ram[19],my_machine.my_memory.ram[20])
# reset machine to user mode
my_machine.my_registers.SW[0] = my_machine.my_registers.SW[0].__and__(my_machine.my_registers.not_supervisor_mode_mask)
print("reset SW[0] is", my_machine.my_registers.SW[0])
print

# testing the STX instruction
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 18
my_machine.my_ALU.STX(32768+3)
print("testing STX instruction with X containing ",my_machine.my_registers.X[0],my_machine.my_registers.X[1],my_machine.my_registers.X[2])
print("results in ",my_machine.my_memory.ram[21],my_machine.my_memory.ram[22],my_machine.my_memory.ram[23])
print

# testing the SUB instruction
my_machine.my_registers.A[0] = 0
my_machine.my_registers.A[1] = 0
my_machine.my_registers.A[2] = 3
my_machine.my_memory.ram[3] = 0
my_machine.my_memory.ram[4] = 0
my_machine.my_memory.ram[5] = 100
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 3
print("subtracting",my_machine.my_memory.ram[3],my_machine.my_memory.ram[4],my_machine.my_memory.ram[5]," from ")
print(my_machine.my_registers.A[0],my_machine.my_registers.A[1],my_machine.my_registers.A[2]," results in")
my_machine.my_ALU.SUB(32768+0)
print(my_machine.my_registers.A[0],my_machine.my_registers.A[1],my_machine.my_registers.A[2])

# testing TD instruction
my_machine.my_memory.ram[3] = 0
my_machine.my_memory.ram[4] = 0
my_machine.my_memory.ram[5] = 1
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 3
my_machine.my_ALU.TD(32768+0)
print("SW after testing device is",my_machine.my_registers.SW[0])
my_machine.my_memory.ram[3] = 0
my_machine.my_memory.ram[4] = 0
my_machine.my_memory.ram[5] = 1
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 3
my_machine.my_ALU.TD(32768+0)
print("SW after testing device is",my_machine.my_registers.SW[0])
my_machine.my_memory.ram[3] = 0
my_machine.my_memory.ram[4] = 0
my_machine.my_memory.ram[5] = 1
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 3
my_machine.my_ALU.TD(32768+0)
print("SW after testing device is",my_machine.my_registers.SW[0])
print

#testing TIX instruction

my_machine.my_memory.ram[3] = 0
my_machine.my_memory.ram[4] = 0
my_machine.my_memory.ram[5] = 5
print("testing TIX, ram is",my_machine.my_memory.ram[3],my_machine.my_memory.ram[4],my_machine.my_memory.ram[5])
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 3
print("X is",my_machine.my_registers.X[0],my_machine.my_registers.X[1],my_machine.my_registers.X[2])
my_machine.my_ALU.TIX(3)
print("after TIX instruction, X is",my_machine.my_registers.X[0],my_machine.my_registers.X[1],my_machine.my_registers.X[2])
print("and SW is",my_machine.my_registers.SW[0])
print("X is",my_machine.my_registers.X[0],my_machine.my_registers.X[1],my_machine.my_registers.X[2])
my_machine.my_ALU.TIX(3)
print("after TIX instruction, X is",my_machine.my_registers.X[0],my_machine.my_registers.X[1],my_machine.my_registers.X[2])
print("and SW is",my_machine.my_registers.SW[0])
print("X is",my_machine.my_registers.X[0],my_machine.my_registers.X[1],my_machine.my_registers.X[2])
my_machine.my_ALU.TIX(3)
print("after TIX instruction, X is",my_machine.my_registers.X[0],my_machine.my_registers.X[1],my_machine.my_registers.X[2])
print("and SW is",my_machine.my_registers.SW[0])
print

# testing WD command

my_machine.my_memory.ram[3] = 0
my_machine.my_memory.ram[4] = 0
my_machine.my_memory.ram[5] = 0
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 3
my_machine.my_registers.A[0] = 0
my_machine.my_registers.A[1] = 0
my_machine.my_registers.A[2] = 35
print("testing writing '#' to Device 01")
my_machine.my_ALU.WD(32768+0)

my_machine.my_memory.ram[3] = 0
my_machine.my_memory.ram[4] = 0
my_machine.my_memory.ram[5] = 1
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 3
my_machine.my_registers.A[0] = 0
my_machine.my_registers.A[1] = 0
my_machine.my_registers.A[2] = 36
print("testing writing '$' to Device 01")
my_machine.my_ALU.WD(32768+0)
my_machine.my_ALU.my_io_supervisor.shutdown()
print

#testing conversion from integers to hex strings
print("253 in hex is",my_machine.my_ALU.convert_int_to_hex_string(253))
print

#testing instruction decode
print("instruction associated with '0C' is",my_machine.my_ALU.entire_instruction_set_decode_table['0C'])
print

#testing fetch next instruction
print("testing fetch next instruction with PC 0,0,3")
my_machine.my_registers.PC[0] = 0
my_machine.my_registers.PC[1] = 0
my_machine.my_registers.PC[2] = 3
print("instruction is 8,0,6 (LDL 0,6)")
my_machine.my_memory.ram[3] = 8
my_machine.my_memory.ram[4] = 0
my_machine.my_memory.ram[5] = 6
print("word at 0,6 is 23,34,45")
my_machine.my_memory.ram[6] = 23
my_machine.my_memory.ram[7] = 34
my_machine.my_memory.ram[8] = 45
temp = my_machine.my_ALU.fetch_next_instruction()
print("next instruction word is",temp[0],temp[1],temp[2])
print("executing instruction ....")
my_machine.my_ALU.execute_instruction(temp)
print("new contents of L are ",my_machine.my_registers.L[0],my_machine.my_registers.L[1],my_machine.my_registers.L[2])
print

# testing ALU clock tic function
my_machine.my_ALU.running = True
print("testing clock tic with PC 0,0,3")
my_machine.my_registers.PC[0] = 0
my_machine.my_registers.PC[1] = 0
my_machine.my_registers.PC[2] = 3
print("instruction is 8,0,6 (LDL 0,6)")
my_machine.my_memory.ram[3] = 8
my_machine.my_memory.ram[4] = 0
my_machine.my_memory.ram[5] = 6
print("word at 0,6 is 34,45,56")
my_machine.my_memory.ram[6] = 34
my_machine.my_memory.ram[7] = 45
my_machine.my_memory.ram[8] = 56
print("executing instruction ....")
my_machine.my_ALU.received_clock_tic()
print("new contents of L are ",my_machine.my_registers.L[0],my_machine.my_registers.L[1],my_machine.my_registers.L[2])
print("IT'S ALIVE!")
print


#test reading from a simulated device number 0
my_machine.my_ALU.my_io_supervisor.restart()
my_machine.my_memory.ram[3] = 0
my_machine.my_memory.ram[4] = 0
my_machine.my_memory.ram[5] = 0
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 3
my_machine.my_ALU.RD(32768+0)
print("read in character from device 00 ",my_machine.my_registers.A[2])
print



#test reading from a simulated device number 0
my_machine.my_memory.ram[3] = 0
my_machine.my_memory.ram[4] = 0
my_machine.my_memory.ram[5] = 0
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 3
my_machine.my_ALU.RD(32768+0)
print("read in character from device 00 ",my_machine.my_registers.A[2])
print

#test reading from a simulated device number 0
my_machine.my_memory.ram[3] = 0
my_machine.my_memory.ram[4] = 0
my_machine.my_memory.ram[5] = 0
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 3
my_machine.my_ALU.RD(32768+0)
print("read in character from device 00 ",my_machine.my_registers.A[2])
print

#test reading from a simulated device number 0
my_machine.my_memory.ram[3] = 0
my_machine.my_memory.ram[4] = 0
my_machine.my_memory.ram[5] = 0
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 3
my_machine.my_ALU.RD(32768+0)
print("read in character from device 00 ",my_machine.my_registers.A[2])
print

#test reading from a simulated device number 0
my_machine.my_memory.ram[3] = 0
my_machine.my_memory.ram[4] = 0
my_machine.my_memory.ram[5] = 0
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 3
my_machine.my_ALU.RD(32768+0)
print("read in character from device 00 ",my_machine.my_registers.A[2])
print

#test reading from a simulated device number 0
my_machine.my_memory.ram[3] = 0
my_machine.my_memory.ram[4] = 0
my_machine.my_memory.ram[5] = 0
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 3
my_machine.my_ALU.RD(32768+0)
print("read in character from device 00 ",my_machine.my_registers.A[2])
print


# testing WD command

my_machine.my_memory.ram[3] = 0
my_machine.my_memory.ram[4] = 0
my_machine.my_memory.ram[5] = 1
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 3
my_machine.my_registers.A[0] = 0
my_machine.my_registers.A[1] = 0
my_machine.my_registers.A[2] = 35
print("testing writing '#' to Device 01")
my_machine.my_ALU.WD(32768+0)

my_machine.my_memory.ram[3] = 0
my_machine.my_memory.ram[4] = 0
my_machine.my_memory.ram[5] = 1
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 3
my_machine.my_registers.A[0] = 0
my_machine.my_registers.A[1] = 0
my_machine.my_registers.A[2] = 36
print("testing writing '$' to Device 01")
my_machine.my_ALU.WD(32768+0)
print

my_machine.my_memory.ram[3] = 0
my_machine.my_memory.ram[4] = 0
my_machine.my_memory.ram[5] = 1
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 3
my_machine.my_registers.A[0] = 0
my_machine.my_registers.A[1] = 0
my_machine.my_registers.A[2] = 35
print("testing writing '#' to Device 01")
my_machine.my_ALU.WD(32768+0)
print

my_machine.my_memory.ram[3] = 0
my_machine.my_memory.ram[4] = 0
my_machine.my_memory.ram[5] = 1
my_machine.my_registers.X[0] = 0
my_machine.my_registers.X[1] = 0
my_machine.my_registers.X[2] = 3
my_machine.my_registers.A[0] = 0
my_machine.my_registers.A[1] = 0
my_machine.my_registers.A[2] = 36
print("testing writing '$' to Device 01")
my_machine.my_ALU.WD(32768+0)
print

print("shutting down IO")
my_machine.my_ALU.my_io_supervisor.shutdown()

# testing the function for converting internal representations of floating
# point numbers to python floats and back

float_array = bytearray(6)
for i in range(0,10):
    for j in range(0,6):
        float_array[j] = int(random()*256.0)
    temp_result = my_machine.my_ALU.convert_byte_array_float_to_float(float_array)
    temp_result2 = my_machine.my_ALU.convert_float_to_byte_array_float(temp_result)
    for j in range(0,6):
        if temp_result2[j] <> float_array[j]:
            for k in range(0,6):
                print(float_array[k],temp_result2[k])
            print(temp_result,\
                  my_machine.my_ALU.convert_byte_array_float_to_float(temp_result2))
            break

print("done with random comparisons")
float_array[0] = (0*128)+63
float_array[1] = (13*16)+8
float_array[2] = 0
float_array[3] = 0
float_array[4] = 0
float_array[5] = 0
temp_result = my_machine.my_ALU.convert_byte_array_float_to_float(float_array)
print(temp_result)

print
temp_result2 = my_machine.my_ALU.convert_float_to_byte_array_float(temp_result)
for i in range(0,6):print(temp_result2[i])

# test of addressing modes using the LDA command (page 10 from SS:AITSP)
#   set up the machine state
print("Testing the various addressing modes.")
my_machine.my_registers.B[0] = 0 * 16 + 0
my_machine.my_registers.B[1] = 6 * 16 + 0
my_machine.my_registers.B[2] = 0 * 16 + 0
my_machine.my_registers.PC[0] = 0 * 16 + 0
my_machine.my_registers.PC[1] = 3 * 16 + 0
my_machine.my_registers.PC[2] = 0 * 16 + 0
my_machine.my_registers.X[0] = 0 * 16 + 0
my_machine.my_registers.X[1] = 0 * 16 + 0
my_machine.my_registers.X[2] = 9 * 16 + 0

my_machine.my_ALU.my_memory.ram[3*2**12+0*2**8+3*2**4+0+0] = 0*2**4 + 0
my_machine.my_ALU.my_memory.ram[3*2**12+0*2**8+3*2**4+0+1] = 3*2**4 + 6
my_machine.my_ALU.my_memory.ram[3*2**12+0*2**8+3*2**4+0+2] = 0*2**4 + 0

my_machine.my_ALU.my_memory.ram[3*2**12+6*2**8+0*2**4+0+0] = 1*2**4 + 0
my_machine.my_ALU.my_memory.ram[3*2**12+6*2**8+0*2**4+0+1] = 3*2**4 + 0
my_machine.my_ALU.my_memory.ram[3*2**12+6*2**8+0*2**4+0+2] = 0*2**4 + 0

my_machine.my_ALU.my_memory.ram[6*2**12+3*2**8+9*2**4+0+0] = 0*2**4 + 0
my_machine.my_ALU.my_memory.ram[6*2**12+3*2**8+9*2**4+0+1] = 12*2**4 + 3
my_machine.my_ALU.my_memory.ram[6*2**12+3*2**8+9*2**4+0+2] = 0*2**4 + 3

my_machine.my_ALU.my_memory.ram[12*2**12+3*2**8+0*2**4+3+0] = 0*2**4 + 0
my_machine.my_ALU.my_memory.ram[12*2**12+3*2**8+0*2**4+3+1] = 3*2**4 + 0
my_machine.my_ALU.my_memory.ram[12*2**12+3*2**8+0*2**4+3+2] = 3*2**4 + 0


#Testing LDA instruction
instruction_word = [3,2*16+6,0]
print("operand is ",(2*16+6)*256)
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of A",1*16,3*16,0)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print

instruction_word = [3,12*16+3,0]
print("operand is ",(12*16+3)*256+(0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of A",0,12*16+3,3)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print

instruction_word = [2,2*16,3*16]
print("operand is ",(2*16)*256+(3*16))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of A",16,3*16,0)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print

instruction_word = [1,0*16+0,3*16+0]
print("operand is ",(0)*256+(3*16+0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of A",0,0,3*16)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print

instruction_word = [0,3*16+6,0*16+0]
print("operand is ",(3*16+6)*256+(0*16+0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of A",16,3*16,0)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print

instruction_word = [3,1*16+0,12*16+3,0*16+3]
print("operand is ",(1*16+0)*2**16+(1*16+0)*256+(0*16+3))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of A",0,3*16,3*16)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print

# test ADD with different addressing modes
print("testing ADD function")
my_machine.my_registers.A[0] = 0
my_machine.my_registers.A[1] = 0
my_machine.my_registers.A[2] = 0

instruction_word = [1*16+8+3,2*16+6,0]
print("operand is ",(2*16+6)*256)
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of A",1*16,3*16,0)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print

my_machine.my_registers.A[0] = 0
my_machine.my_registers.A[1] = 0
my_machine.my_registers.A[2] = 0

instruction_word = [1*16+8+3,12*16+3,0]
print("operand is ",(12*16+3)*256+(0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of A",0,12*16+3,3)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print

my_machine.my_registers.A[0] = 0
my_machine.my_registers.A[1] = 0
my_machine.my_registers.A[2] = 0

instruction_word = [1*16+8+2,2*16,3*16]
print("operand is ",(2*16)*256+(3*16))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of A",16,3*16,0)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print

my_machine.my_registers.A[0] = 0
my_machine.my_registers.A[1] = 0
my_machine.my_registers.A[2] = 0

instruction_word = [1*16+8+1,0*16+0,3*16+0]
print("operand is ",(0)*256+(3*16+0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of A",0,0,3*16)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print

my_machine.my_registers.A[0] = 0
my_machine.my_registers.A[1] = 0
my_machine.my_registers.A[2] = 0

instruction_word = [1*16+8+0,3*16+6,0*16+0]
print("operand is ",(3*16+6)*256+(0*16+0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of A",16,3*16,0)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print

my_machine.my_registers.A[0] = 0
my_machine.my_registers.A[1] = 0
my_machine.my_registers.A[2] = 0

instruction_word = [1*16+8+3,1*16+0,12*16+3,0*16+3]
print("operand is ",(1*16+0)*2**16+(1*16+0)*256+(0*16+3))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of A",0,3*16,3*16)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print


# test AND with different addressing modes
print("testing AND function")
my_machine.my_registers.A[0] = 255
my_machine.my_registers.A[1] = 255
my_machine.my_registers.A[2] = 255

instruction_word = [4*16+0+3,2*16+6,0]
print("operand is ",(2*16+6)*256)
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of A",1*16,3*16,0)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print

my_machine.my_registers.A[0] = 255
my_machine.my_registers.A[1] = 255
my_machine.my_registers.A[2] = 255

instruction_word = [4*16+0+3,12*16+3,0]
print("operand is ",(12*16+3)*256+(0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of A",0,12*16+3,3)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print

my_machine.my_registers.A[0] = 255
my_machine.my_registers.A[1] = 255
my_machine.my_registers.A[2] = 255

instruction_word = [4*16+0+2,2*16,3*16]
print("operand is ",(2*16)*256+(3*16))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of A",16,3*16,0)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print

my_machine.my_registers.A[0] = 255
my_machine.my_registers.A[1] = 255
my_machine.my_registers.A[2] = 255

instruction_word = [4*16+0+1,0*16+0,3*16+0]
print("operand is ",(0)*256+(3*16+0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of A",0,0,3*16)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print

my_machine.my_registers.A[0] = 255
my_machine.my_registers.A[1] = 255
my_machine.my_registers.A[2] = 255

instruction_word = [4*16+0+0,3*16+6,0*16+0]
print("operand is ",(3*16+6)*256+(0*16+0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of A",16,3*16,0)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print

my_machine.my_registers.A[0] = 255
my_machine.my_registers.A[1] = 255
my_machine.my_registers.A[2] = 255

instruction_word = [4*16+0+3,1*16+0,12*16+3,0*16+3]
print("operand is ",(1*16+0)*2**16+(1*16+0)*256+(0*16+3))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of A",0,3*16,3*16)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print

# test COMP with different addressing modes
print("testing COMP function")
my_machine.my_registers.A[0] = 1*16+0
my_machine.my_registers.A[1] = 3*16+0
my_machine.my_registers.A[2] = 0*16+1

instruction_word = [2*16+8+3,2*16+6,0]
print("operand is ",(2*16+6)*256)
my_machine.my_ALU.execute_instruction(instruction_word)
print("status word is",my_machine.my_registers.SW[0])
print("A is 1 greater than reference")
print("CC_gt_query is",my_machine.my_registers.CC_gt_query())
print

my_machine.my_registers.A[0] = 0*16+0
my_machine.my_registers.A[1] = 12*16+3
my_machine.my_registers.A[2] = 0*16+2

instruction_word = [2*16+8+3,12*16+3,0]
print("operand is ",(12*16+3)*256+(0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("status word is",my_machine.my_registers.SW[0])
print("A is 1 less than reference")
print("CC_lt_query is",my_machine.my_registers.CC_lt_query())
print

my_machine.my_registers.A[0] = 1*16+0
my_machine.my_registers.A[1] = 3*16+1
my_machine.my_registers.A[2] = 0*16+0

instruction_word = [2*16+8+2,2*16,3*16]
print("operand is ",(2*16)*256+(3*16))
my_machine.my_ALU.execute_instruction(instruction_word)
print("status word is",my_machine.my_registers.SW[0])
print("A is 256 greater than reference")
print("CC_gt_query is",my_machine.my_registers.CC_gt_query())
print

my_machine.my_registers.A[0] = 0*16+1
my_machine.my_registers.A[1] = 0*16+0
my_machine.my_registers.A[2] = 3*16+0

instruction_word = [2*16+8+1,0*16+0,3*16+0]
print("operand is ",(0)*256+(3*16+0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("status word is",my_machine.my_registers.SW[0])
print("A is 256**2 greater than reference")
print("CC_gt_query is",my_machine.my_registers.CC_gt_query())
print

my_machine.my_registers.A[0] = 1*16+0
my_machine.my_registers.A[1] = 2*16+15
my_machine.my_registers.A[2] = 0*16+0

instruction_word = [2*16+8+0,3*16+6,0*16+0]
print("operand is ",(3*16+6)*256+(0*16+0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("status word is",my_machine.my_registers.SW[0])
print("A is 256 less than reference")
print("CC_lt_query is",my_machine.my_registers.CC_lt_query())
print

my_machine.my_registers.A[0] = 0*16+0
my_machine.my_registers.A[1] = 3*16+0
my_machine.my_registers.A[2] = 3*16+0

instruction_word = [2*16+8+3,1*16+0,12*16+3,0*16+3]
print("operand is ",(1*16+0)*2**16+(1*16+0)*256+(0*16+3))
my_machine.my_ALU.execute_instruction(instruction_word)
print("status word is",my_machine.my_registers.SW[0])
print("A is equal to reference")
print("CC_eq_query is",my_machine.my_registers.CC_eq_query())
print


# test DIV with different addressing modes
print("testing DIV function")
my_machine.my_registers.A[0] = 2*(1*16+0)
my_machine.my_registers.A[1] = 2*(3*16+0)
my_machine.my_registers.A[2] = 2*(0*16+0)

instruction_word = [2*16+4+3,2*16+6,0]
print("operand is ",(2*16+6)*256)
my_machine.my_ALU.execute_instruction(instruction_word)
print("A is 2x greater than divisor")
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print("integer representation is",my_machine.my_ALU.convert_twos_compliment_A_to_int())
print

my_machine.my_registers.A[0] = 0*16+0
my_machine.my_registers.A[1] = 12*16+3
my_machine.my_registers.A[2] = 0*16+2

instruction_word = [2*16+4+3,12*16+3,0]
print("operand is ",(12*16+3)*256+(0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("A is 1 less than divisor")
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print("integer representation is",my_machine.my_ALU.convert_twos_compliment_A_to_int())
print

my_machine.my_registers.A[0] = 3*(1*16+0)
my_machine.my_registers.A[1] = 3*(3*16+0)
my_machine.my_registers.A[2] = 3*(0*16+0)

instruction_word = [2*16+4+2,2*16,3*16]
print("operand is ",(2*16)*256+(3*16))
my_machine.my_ALU.execute_instruction(instruction_word)
print("A is 3x greater than divisor")
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print("integer representation is",my_machine.my_ALU.convert_twos_compliment_A_to_int())
print

my_machine.my_registers.A[0] = 0*16+1
my_machine.my_registers.A[1] = 0*16+0
my_machine.my_registers.A[2] = 3*16+0

instruction_word = [2*16+4+1,0*16+0,3*16+0]
print("operand is ",(0)*256+(3*16+0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("A is 256**2 greater than divisor")
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print("integer representation is",my_machine.my_ALU.convert_twos_compliment_A_to_int())
print

my_machine.my_registers.A[0] = 1*16+0
my_machine.my_registers.A[1] = 3*16+0
my_machine.my_registers.A[2] = 0*16+0

instruction_word = [2*16+4+0,3*16+6,0*16+0]
print("operand is ",(3*16+6)*256+(0*16+0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("A is equal divisor")
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print("integer representation is",my_machine.my_ALU.convert_twos_compliment_A_to_int())
print

my_machine.my_registers.A[0] = 8*16+15
my_machine.my_registers.A[1] = 3*16+0
my_machine.my_registers.A[2] = 3*16+0

instruction_word = [2*16+4+3,1*16+0,12*16+3,0*16+3]
print("operand is ",(1*16+0)*2**16+(1*16+0)*256+(0*16+3))
my_machine.my_ALU.execute_instruction(instruction_word)
print("A is a large negative number")
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print("integer representation is",my_machine.my_ALU.convert_twos_compliment_A_to_int())
print

# Test the J instruction
instruction_word = [3*16+12+3,2*16+6,0]
print("operand is ",(2*16+6)*256)
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of PC",0*16,3*16+6,0)
print("Actual value of PC",my_machine.my_registers.PC[0],my_machine.my_registers.PC[1],\
      my_machine.my_registers.PC[2])
print

my_machine.my_registers.PC[0] = 0 * 16 + 0
my_machine.my_registers.PC[1] = 3 * 16 + 0
my_machine.my_registers.PC[2] = 0 * 16 + 0

instruction_word = [3*16+12+3,12*16+3,0]
print("operand is ",(12*16+3)*256+(0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of PC",0,6*16+3,9*16+0)
print("Actual value of PC",my_machine.my_registers.PC[0],my_machine.my_registers.PC[1],\
      my_machine.my_registers.PC[2])
print
my_machine.my_registers.PC[0] = 0 * 16 + 0
my_machine.my_registers.PC[1] = 3 * 16 + 0
my_machine.my_registers.PC[2] = 0 * 16 + 0

instruction_word = [3*16+12+2,2*16,3*16] #indirect addressing
print("operand is ",(2*16)*256+(3*16))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of PC",0,3*16+6,0*16+0)
print("Actual value of PC",my_machine.my_registers.PC[0],my_machine.my_registers.PC[1],\
      my_machine.my_registers.PC[2])
print
my_machine.my_registers.PC[0] = 0 * 16 + 0
my_machine.my_registers.PC[1] = 3 * 16 + 0
my_machine.my_registers.PC[2] = 0 * 16 + 0

instruction_word = [3*16+12+1,0*16+0,3*16+0]
print("operand is ",(0)*256+(3*16+0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of PC",0,0,3*16)
print("Actual value of PC",my_machine.my_registers.PC[0],my_machine.my_registers.PC[1],\
      my_machine.my_registers.PC[2])
print
my_machine.my_registers.PC[0] = 0 * 16 + 0
my_machine.my_registers.PC[1] = 3 * 16 + 0
my_machine.my_registers.PC[2] = 0 * 16 + 0

instruction_word = [3*16+12+0,3*16+6,0*16+0]
print("operand is ",(3*16+6)*256+(0*16+0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of PC",0,3*16+6,0)
print("Actual value of PC",my_machine.my_registers.PC[0],my_machine.my_registers.PC[1],\
      my_machine.my_registers.PC[2])
print
my_machine.my_registers.PC[0] = 0 * 16 + 0
my_machine.my_registers.PC[1] = 3 * 16 + 0
my_machine.my_registers.PC[2] = 0 * 16 + 0

instruction_word = [3*16+12+3,1*16+0,12*16+3,0*16+3]
print("operand is ",(1*16+0)*2**16+(1*16+0)*256+(0*16+3))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of PC",0,12*16+3,0*16+3)
print("Actual value of PC",my_machine.my_registers.PC[0],my_machine.my_registers.PC[1],\
      my_machine.my_registers.PC[2])
print
my_machine.my_registers.PC[0] = 0 * 16 + 0
my_machine.my_registers.PC[1] = 3 * 16 + 0
my_machine.my_registers.PC[2] = 0 * 16 + 0

# Testing LDCH instruction
instruction_word = [5*16+0+3,2*16+6,0]
print("operand is ",(2*16+6)*256)
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of A[2]",1*16)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print

instruction_word = [5*16+0+3,12*16+3,0]
print("operand is ",(12*16+3)*256+(0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of A[2]",0)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print

instruction_word = [5*16+0+2,2*16,3*16]
print("operand is ",(2*16)*256+(3*16))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of A[2]",16)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print

instruction_word = [5*16+0+1,0*16+0,3*16+0]
print("operand is ",(0)*256+(3*16+0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of A[2]",3*16)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print

instruction_word = [5*16+0+0,3*16+6,0*16+0]
print("operand is ",(3*16+6)*256+(0*16+0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of A[2]",16)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print

instruction_word = [5*16+0+3,1*16+0,12*16+3,0*16+3]
print("operand is ",(1*16+0)*2**16+(1*16+0)*256+(0*16+3))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of A[2]",0)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print

#Testing LDL instruction
instruction_word = [8+3,2*16+6,0]
print("operand is ",(2*16+6)*256)
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of L",1*16,3*16,0)
print("Actual value of L",my_machine.my_registers.L[0],my_machine.my_registers.L[1],\
      my_machine.my_registers.L[2])
print

instruction_word = [8+3,12*16+3,0]
print("operand is ",(12*16+3)*256+(0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of L",0,12*16+3,3)
print("Actual value of L",my_machine.my_registers.L[0],my_machine.my_registers.L[1],\
      my_machine.my_registers.L[2])
print

instruction_word = [8+2,2*16,3*16]
print("operand is ",(2*16)*256+(3*16))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of L",16,3*16,0)
print("Actual value of L",my_machine.my_registers.L[0],my_machine.my_registers.L[1],\
      my_machine.my_registers.L[2])
print

instruction_word = [8+1,0*16+0,3*16+0]
print("operand is ",(0)*256+(3*16+0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of L",0,0,3*16)
print("Actual value of L",my_machine.my_registers.L[0],my_machine.my_registers.L[1],\
      my_machine.my_registers.L[2])
print

instruction_word = [8+0,3*16+6,0*16+0]
print("operand is ",(3*16+6)*256+(0*16+0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of L",16,3*16,0)
print("Actual value of L",my_machine.my_registers.L[0],my_machine.my_registers.L[1],\
      my_machine.my_registers.L[2])
print

instruction_word = [8+3,1*16+0,12*16+3,0*16+3]
print("operand is ",(1*16+0)*2**16+(1*16+0)*256+(0*16+3))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of L",0,3*16,3*16)
print("Actual value of L",my_machine.my_registers.L[0],my_machine.my_registers.L[1],\
      my_machine.my_registers.L[2])
print

#Testing LDX instruction
instruction_word = [4+3,2*16+6,0]
print("operand is ",(2*16+6)*256)
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of X",1*16,3*16,0)
print("Actual value of X",my_machine.my_registers.X[0],my_machine.my_registers.X[1],\
      my_machine.my_registers.X[2])
print

my_machine.my_registers.X[0] = 0 * 16 + 0
my_machine.my_registers.X[1] = 0 * 16 + 0
my_machine.my_registers.X[2] = 9 * 16 + 0
instruction_word = [4+3,12*16+3,0]
print("operand is ",(12*16+3)*256+(0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of X",0,12*16+3,3)
print("Actual value of X",my_machine.my_registers.X[0],my_machine.my_registers.X[1],\
      my_machine.my_registers.X[2])
print

my_machine.my_registers.X[0] = 0 * 16 + 0
my_machine.my_registers.X[1] = 0 * 16 + 0
my_machine.my_registers.X[2] = 9 * 16 + 0
instruction_word = [4+2,2*16,3*16]
print("operand is ",(2*16)*256+(3*16))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of X",16,3*16,0)
print("Actual value of X",my_machine.my_registers.X[0],my_machine.my_registers.X[1],\
      my_machine.my_registers.X[2])
print

my_machine.my_registers.X[0] = 0 * 16 + 0
my_machine.my_registers.X[1] = 0 * 16 + 0
my_machine.my_registers.X[2] = 9 * 16 + 0
instruction_word = [4+1,0*16+0,3*16+0]
print("operand is ",(0)*256+(3*16+0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of X",0,0,3*16)
print("Actual value of X",my_machine.my_registers.X[0],my_machine.my_registers.X[1],\
      my_machine.my_registers.X[2])
print

my_machine.my_registers.X[0] = 0 * 16 + 0
my_machine.my_registers.X[1] = 0 * 16 + 0
my_machine.my_registers.X[2] = 9 * 16 + 0
instruction_word = [4+0,3*16+6,0*16+0]
print("operand is ",(3*16+6)*256+(0*16+0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of X",16,3*16,0)
print("Actual value of X",my_machine.my_registers.X[0],my_machine.my_registers.X[1],\
      my_machine.my_registers.X[2])
print

my_machine.my_registers.X[0] = 0 * 16 + 0
my_machine.my_registers.X[1] = 0 * 16 + 0
my_machine.my_registers.X[2] = 9 * 16 + 0
instruction_word = [4+3,1*16+0,12*16+3,0*16+3]
print("operand is ",(1*16+0)*2**16+(1*16+0)*256+(0*16+3))
my_machine.my_ALU.execute_instruction(instruction_word)
print("Expected value of X",0,3*16,3*16)
print("Actual value of X",my_machine.my_registers.X[0],my_machine.my_registers.X[1],\
      my_machine.my_registers.X[2])
print

my_machine.my_registers.X[0] = 0 * 16 + 0
my_machine.my_registers.X[1] = 0 * 16 + 0
my_machine.my_registers.X[2] = 9 * 16 + 0

# Testing conversion routines for converting integers to internal representations in A
print("Testing converting integers to internal representations in A")
my_machine.my_ALU.convert_int_to_twos_compliment_in_A(-1)
print("A representation of -1",my_machine.my_registers.A[0],\
      my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
my_machine.my_ALU.convert_int_to_twos_compliment_in_A(127)
print("A representation of 127",my_machine.my_registers.A[0],\
      my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
my_machine.my_ALU.convert_int_to_twos_compliment_in_A(2)
print("A representation of 2",my_machine.my_registers.A[0],\
      my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
my_machine.my_ALU.convert_int_to_twos_compliment_in_A(0)
print("A representation of 0",my_machine.my_registers.A[0],\
      my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
my_machine.my_ALU.convert_int_to_twos_compliment_in_A(-128)
print("A representation of -128",my_machine.my_registers.A[0],\
      my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
my_machine.my_ALU.convert_int_to_twos_compliment_in_A(-256)
print("A representation of -256",my_machine.my_registers.A[0],\
      my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
my_machine.my_ALU.convert_int_to_twos_compliment_in_A(2**23-1)
print("A representation of 2**23-1",my_machine.my_registers.A[0],\
      my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
my_machine.my_ALU.convert_int_to_twos_compliment_in_A(-1*2**23)
print("A representation of -2**23",my_machine.my_registers.A[0],\
      my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])

# test MUL with different addressing modes

my_machine.my_ALU.my_memory.ram[3*2**12+0*2**8+3*2**4+0+0] = 0*2**4 + 0
my_machine.my_ALU.my_memory.ram[3*2**12+0*2**8+3*2**4+0+1] = 3*2**4 + 6
my_machine.my_ALU.my_memory.ram[3*2**12+0*2**8+3*2**4+0+2] = 0*2**4 + 0

my_machine.my_ALU.my_memory.ram[3*2**12+6*2**8+0*2**4+0+0] = 0*2**4 + 0
my_machine.my_ALU.my_memory.ram[3*2**12+6*2**8+0*2**4+0+1] = 0*2**4 + 0
my_machine.my_ALU.my_memory.ram[3*2**12+6*2**8+0*2**4+0+2] = 0*2**4 + 2

my_machine.my_ALU.my_memory.ram[6*2**12+3*2**8+9*2**4+0+0] = 15*2**4 + 15
my_machine.my_ALU.my_memory.ram[6*2**12+3*2**8+9*2**4+0+1] = 15*2**4 + 15
my_machine.my_ALU.my_memory.ram[6*2**12+3*2**8+9*2**4+0+2] = 15*2**4 + 15

my_machine.my_ALU.my_memory.ram[12*2**12+3*2**8+0*2**4+3+0] = 15*2**4 + 15
my_machine.my_ALU.my_memory.ram[12*2**12+3*2**8+0*2**4+3+1] = 15*2**4 + 15
my_machine.my_ALU.my_memory.ram[12*2**12+3*2**8+0*2**4+3+2] = 15*2**4 + 14

print("testing MUL function")
my_machine.my_registers.A[0] = (0*16+0)
my_machine.my_registers.A[1] = (0*16+0)
my_machine.my_registers.A[2] = (0*16+2)

instruction_word = [2*16+0+3,2*16+6,0]
print("operand is ",(2*16+6)*256)
my_machine.my_ALU.execute_instruction(instruction_word)
print("A is 2, memory value is 2")
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print("integer representation is",my_machine.my_ALU.convert_twos_compliment_A_to_int())
print

my_machine.my_registers.A[0] = 15*16+15
my_machine.my_registers.A[1] = 15*16+15
my_machine.my_registers.A[2] = 15*16+15

instruction_word = [2*16+0+3,12*16+3,0]
print("operand is ",(12*16+3)*256+(0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("A is -1, memory value is -1")
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print("integer representation is",my_machine.my_ALU.convert_twos_compliment_A_to_int())
print

my_machine.my_registers.A[0] = (0*16+0)
my_machine.my_registers.A[1] = (0*16+0)
my_machine.my_registers.A[2] = (0*16+3)

instruction_word = [2*16+0+2,2*16+0,3*16+0]
print("operand is ",(2*16)*256+(3*16))
print("machine memory pointer is",my_machine.my_ALU.my_memory.ram[3*2**12+0*2**8+3*2**4+0+0],\
      my_machine.my_ALU.my_memory.ram[3*2**12+0*2**8+3*2**4+0+1],\
      my_machine.my_ALU.my_memory.ram[3*2**12+0*2**8+3*2**4+0+2])
print("Actual value of A prior to multiplication is",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print("A is 3, memory value is 2")
my_machine.my_ALU.execute_instruction(instruction_word)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print("integer representation is",my_machine.my_ALU.convert_twos_compliment_A_to_int())
print

my_machine.my_registers.A[0] = 0*16+0
my_machine.my_registers.A[1] = 0*16+1
my_machine.my_registers.A[2] = 0*16+0

instruction_word = [2*16+0+1,0*16+0,3*16+0]
print("operand is ",(0)*256+(3*16+0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("A is 256, memory value is 48 immediate with product",256*48)
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print("integer representation is",my_machine.my_ALU.convert_twos_compliment_A_to_int())
print

my_machine.my_registers.A[0] = 0*16+0
my_machine.my_registers.A[1] = 0*16+0
my_machine.my_registers.A[2] = 0*16+4

instruction_word = [2*16+0+0,3*16+6,0*16+0]
print("operand is ",(3*16+6)*256+(0*16+0))
my_machine.my_ALU.execute_instruction(instruction_word)
print("A is 4, memory value is 2")
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print("integer representation is",my_machine.my_ALU.convert_twos_compliment_A_to_int())
print

my_machine.my_registers.A[0] = 15*16+15
my_machine.my_registers.A[1] = 15*16+15
my_machine.my_registers.A[2] = 15*16+14

instruction_word = [2*16+0+3,1*16+0,12*16+3,0*16+3]
print("operand is ",(1*16+0)*2**16+(1*16+0)*256+(0*16+3))
my_machine.my_ALU.execute_instruction(instruction_word)
print("A is -2, memory value is -2")
print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
      my_machine.my_registers.A[2])
print("integer representation is",my_machine.my_ALU.convert_twos_compliment_A_to_int())
print

my_machine.my_registers.B[0] = 0 * 16 + 0
my_machine.my_registers.B[1] = 6 * 16 + 0
my_machine.my_registers.B[2] = 0 * 16 + 0
my_machine.my_registers.PC[0] = 0 * 16 + 0
my_machine.my_registers.PC[1] = 3 * 16 + 0
my_machine.my_registers.PC[2] = 0 * 16 + 0
my_machine.my_registers.X[0] = 0 * 16 + 0
my_machine.my_registers.X[1] = 0 * 16 + 0
my_machine.my_registers.X[2] = 9 * 16 + 0

my_machine.my_ALU.my_memory.ram[3*2**12+0*2**8+3*2**4+0+0] = 0*2**4 + 0
my_machine.my_ALU.my_memory.ram[3*2**12+0*2**8+3*2**4+0+1] = 3*2**4 + 6
my_machine.my_ALU.my_memory.ram[3*2**12+0*2**8+3*2**4+0+2] = 0*2**4 + 0

my_machine.my_ALU.my_memory.ram[3*2**12+6*2**8+0*2**4+0+0] = 1*2**4 + 0
my_machine.my_ALU.my_memory.ram[3*2**12+6*2**8+0*2**4+0+1] = 3*2**4 + 0
my_machine.my_ALU.my_memory.ram[3*2**12+6*2**8+0*2**4+0+2] = 0*2**4 + 0

my_machine.my_ALU.my_memory.ram[6*2**12+3*2**8+9*2**4+0+0] = 0*2**4 + 0
my_machine.my_ALU.my_memory.ram[6*2**12+3*2**8+9*2**4+0+1] = 12*2**4 + 3
my_machine.my_ALU.my_memory.ram[6*2**12+3*2**8+9*2**4+0+2] = 0*2**4 + 3

my_machine.my_ALU.my_memory.ram[12*2**12+3*2**8+0*2**4+3+0] = 0*2**4 + 0
my_machine.my_ALU.my_memory.ram[12*2**12+3*2**8+0*2**4+3+1] = 3*2**4 + 0
my_machine.my_ALU.my_memory.ram[12*2**12+3*2**8+0*2**4+3+2] = 3*2**4 + 0

