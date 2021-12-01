# Second file of ALU emulator testing 

import random
from Machine import *

my_machine = Machine('My first SIC Machine')

print(my_machine.my_name,", testing part two")


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

### Testing OR function
##
##my_machine.my_registers.A[0] = (1*16+0)
##my_machine.my_registers.A[1] = (3*16+0)
##my_machine.my_registers.A[2] = (0*16+1)
##
##instruction_word = [4*16+4+3,2*16+6,0]
##print("operand is ",(2*16+6)*256)
##my_machine.my_ALU.execute_instruction(instruction_word)
##print("A is 103001H, memory value is 103000H")
##print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
##      my_machine.my_registers.A[2])
##print
##
##my_machine.my_registers.A[0] = 0*16+1
##my_machine.my_registers.A[1] = 12*16+3
##my_machine.my_registers.A[2] = 0*16+3
##
##instruction_word = [4*16+4+3,12*16+3,0]
##print("operand is ",(12*16+3)*256+(0))
##my_machine.my_ALU.execute_instruction(instruction_word)
##print("A is 01C303, memory value is 00C303H")
##print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
##      my_machine.my_registers.A[2])
##print
##
##my_machine.my_registers.A[0] = (1*16+0)
##my_machine.my_registers.A[1] = (3*16+0)
##my_machine.my_registers.A[2] = (0*16+2)
##
##instruction_word = [4*16+4+2,2*16+0,3*16+0]
##print("operand is ",(2*16)*256+(3*16))
##print("machine memory pointer is",my_machine.my_ALU.my_memory.ram[3*2**12+0*2**8+3*2**4+0+0],\
##      my_machine.my_ALU.my_memory.ram[3*2**12+0*2**8+3*2**4+0+1],\
##      my_machine.my_ALU.my_memory.ram[3*2**12+0*2**8+3*2**4+0+2])
##print("Actual value of A prior to multiplication is",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
##      my_machine.my_registers.A[2])
##print("A is 10302, memory value is 10300")
##my_machine.my_ALU.execute_instruction(instruction_word)
##print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
##      my_machine.my_registers.A[2])
##print
##
##my_machine.my_registers.A[0] = 0*16+0
##my_machine.my_registers.A[1] = 0*16+1
##my_machine.my_registers.A[2] = 0*16+0
##
##instruction_word = [4*16+4+1,0*16+0,3*16+0]
##print("operand is ",(0)*256+(3*16+0))
##my_machine.my_ALU.execute_instruction(instruction_word)
##print("A is 256, memory value is 48 immediate")
##print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
##      my_machine.my_registers.A[2])
##print
##
##my_machine.my_registers.A[0] = 2*16+0
##my_machine.my_registers.A[1] = 3*16+0
##my_machine.my_registers.A[2] = 0*16+0
##
##instruction_word = [4*16+4+0,3*16+6,0*16+0]
##print("operand is ",(3*16+6)*256+(0*16+0))
##my_machine.my_ALU.execute_instruction(instruction_word)
##print("A is 20300H, memory value is 10300H")
##print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
##      my_machine.my_registers.A[2])
##print
##
##my_machine.my_registers.A[0] = 0*16+0
##my_machine.my_registers.A[1] = 0*16+0
##my_machine.my_registers.A[2] = 0*16+0
##
##instruction_word = [4*16+4+3,1*16+0,12*16+3,0*16+3]
##print("operand is ",(1*16+0)*2**16+(1*16+0)*256+(0*16+3))
##my_machine.my_ALU.execute_instruction(instruction_word)
##print("A is 0, memory value is 003030H")
##print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
##      my_machine.my_registers.A[2])
##print

### Testing RD function
##print("Testing RD function")
##my_machine.my_ALU.my_memory.ram[3*2**12+0*2**8+3*2**4+0+0] = 0*2**4 + 0
##my_machine.my_ALU.my_memory.ram[3*2**12+0*2**8+3*2**4+0+1] = 3*2**4 + 6
##my_machine.my_ALU.my_memory.ram[3*2**12+0*2**8+3*2**4+0+2] = 0*2**4 + 0
##
##my_machine.my_ALU.my_memory.ram[3*2**12+6*2**8+0*2**4+0+0] = 0*2**4 + 0
##my_machine.my_ALU.my_memory.ram[3*2**12+6*2**8+0*2**4+0+1] = 0*2**4 + 0
##my_machine.my_ALU.my_memory.ram[3*2**12+6*2**8+0*2**4+0+2] = 0*2**4 + 0
##
##my_machine.my_ALU.my_memory.ram[6*2**12+3*2**8+9*2**4+0+0] = 0*2**4 + 0
##my_machine.my_ALU.my_memory.ram[6*2**12+3*2**8+9*2**4+0+1] = 0*2**4 + 0
##my_machine.my_ALU.my_memory.ram[6*2**12+3*2**8+9*2**4+0+2] = 0*2**4 + 1
##
##my_machine.my_ALU.my_memory.ram[12*2**12+3*2**8+0*2**4+3+0] = 0*2**4 + 0
##my_machine.my_ALU.my_memory.ram[12*2**12+3*2**8+0*2**4+3+1] = 0*2**4 + 0
##my_machine.my_ALU.my_memory.ram[12*2**12+3*2**8+0*2**4+3+2] = 0*2**4 + 0
##
##
##instruction_word = [4*16+4+3,2*16+6,0]
##print("operand is ",(2*16+6)*256)
##my_machine.my_ALU.execute_instruction(instruction_word)
##print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
##      my_machine.my_registers.A[2])
##print
##
##my_machine.my_io.shutdown()
##my_machine.my_io.restart()
##
##instruction_word = [13*16+8+3,12*16+3,0]
##print("operand is ",(12*16+3)*256+(0))
##my_machine.my_ALU.execute_instruction(instruction_word)
##print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
##      my_machine.my_registers.A[2])
##print
##
##my_machine.my_io.shutdown()
##my_machine.my_io.restart()
##
##instruction_word = [13*16+8+2,2*16+0,3*16+0]
##print("operand is ",(2*16)*256+(3*16))
##print("machine memory pointer is",my_machine.my_ALU.my_memory.ram[3*2**12+0*2**8+3*2**4+0+0],\
##      my_machine.my_ALU.my_memory.ram[3*2**12+0*2**8+3*2**4+0+1],\
##      my_machine.my_ALU.my_memory.ram[3*2**12+0*2**8+3*2**4+0+2])
##my_machine.my_ALU.execute_instruction(instruction_word)
##print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
##      my_machine.my_registers.A[2])
##print
##
##instruction_word = [13*16+8+1,0*16+0,0*16+1]
##print("operand is ",(0)*256+(3*16+0))
##my_machine.my_ALU.execute_instruction(instruction_word)
##print("value is 1 immediate")
##print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
##      my_machine.my_registers.A[2])
##print
##
##my_machine.my_io.shutdown()
##my_machine.my_io.restart()
##
##instruction_word = [13*16+8+0,3*16+6,0*16+0]
##print("operand is ",(3*16+6)*256+(0*16+0))
##my_machine.my_ALU.execute_instruction(instruction_word)
##print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
##      my_machine.my_registers.A[2])
##print
##
##my_machine.my_io.shutdown()
##my_machine.my_io.restart()
##
##instruction_word = [13*16+8+3,1*16+0,12*16+3,0*16+3]
##print("operand is ",(1*16+0)*2**16+(1*16+0)*256+(0*16+3))
##my_machine.my_ALU.execute_instruction(instruction_word)
##print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
##      my_machine.my_registers.A[2])
##print
##
##my_machine.my_io.shutdown()
##my_machine.my_io.restart()

# reset the machine for further testing
##my_machine.my_ALU.my_memory.ram[3*2**12+0*2**8+3*2**4+0+0] = 0*2**4 + 0
##my_machine.my_ALU.my_memory.ram[3*2**12+0*2**8+3*2**4+0+1] = 3*2**4 + 6
##my_machine.my_ALU.my_memory.ram[3*2**12+0*2**8+3*2**4+0+2] = 0*2**4 + 0
##
##my_machine.my_ALU.my_memory.ram[3*2**12+6*2**8+0*2**4+0+0] = 1*2**4 + 0
##my_machine.my_ALU.my_memory.ram[3*2**12+6*2**8+0*2**4+0+1] = 3*2**4 + 0
##my_machine.my_ALU.my_memory.ram[3*2**12+6*2**8+0*2**4+0+2] = 0*2**4 + 0
##
##my_machine.my_ALU.my_memory.ram[6*2**12+3*2**8+9*2**4+0+0] = 0*2**4 + 0
##my_machine.my_ALU.my_memory.ram[6*2**12+3*2**8+9*2**4+0+1] = 12*2**4 + 3
##my_machine.my_ALU.my_memory.ram[6*2**12+3*2**8+9*2**4+0+2] = 0*2**4 + 3
##
##my_machine.my_ALU.my_memory.ram[12*2**12+3*2**8+0*2**4+3+0] = 0*2**4 + 0
##my_machine.my_ALU.my_memory.ram[12*2**12+3*2**8+0*2**4+3+1] = 3*2**4 + 0
##my_machine.my_ALU.my_memory.ram[12*2**12+3*2**8+0*2**4+3+2] = 3*2**4 + 0

# Note RSUB is not tested as this has not changed from the SIC implementation

### Testing the STA command
##my_machine.my_registers.A[0] = 6
##my_machine.my_registers.A[1] = 7
##my_machine.my_registers.A[2] = 9
##
##instruction_word = [0*16+12+3,2*16+6,0]
##print("operand is ",(2*16+6)*256)
##my_machine.my_ALU.execute_instruction(instruction_word)
##instruction_word = [3,2*16+6,0]
##print("operand is ",(2*16+6)*256)
##my_machine.my_ALU.execute_instruction(instruction_word)
##print("Expected value of A",6,7,9)
##print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
##      my_machine.my_registers.A[2])
##print
##
##instruction_word = [0*16+12+3,12*16+3,0]
##print("operand is ",(12*16+3)*256+(0))
##my_machine.my_ALU.execute_instruction(instruction_word)
##instruction_word = [3,12*16+3,0]
##print("operand is ",(12*16+3)*256+(0))
##my_machine.my_ALU.execute_instruction(instruction_word)
##print("Expected value of A",6,7,9)
##print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
##      my_machine.my_registers.A[2])
##print
##
##instruction_word = [0*16+12+2,2*16,3*16]
##print("operand is ",(2*16)*256+(3*16))
##my_machine.my_ALU.execute_instruction(instruction_word)
##instruction_word = [2,2*16,3*16]
##print("operand is ",(2*16)*256+(3*16))
##my_machine.my_ALU.execute_instruction(instruction_word)
##print("Expected value of A",6,7,9)
##print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
##      my_machine.my_registers.A[2])
##print
##
##instruction_word = [0*16+12+1,0*16+0,3*16+0]
##print("operand is ",(0)*256+(3*16+0))
##print("immediate addressing")
##my_machine.my_ALU.execute_instruction(instruction_word)
##print("memory values are:",my_machine.my_memory.ram[3*16],my_machine.my_memory.ram[3*16+1],my_machine.my_memory.ram[3*16+2])
##print
##
##instruction_word = [0*16+12+0,3*16+6,0*16+0]
##print("operand is ",(3*16+6)*256+(0*16+0))
##my_machine.my_ALU.execute_instruction(instruction_word)
##instruction_word = [0,3*16+6,0*16+0]
##print("operand is ",(3*16+6)*256+(0*16+0))
##my_machine.my_ALU.execute_instruction(instruction_word)
##print("Expected value of A",6,7,9)
##print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
##      my_machine.my_registers.A[2])
##print
##
##instruction_word = [0*16+12+3,1*16+0,12*16+3,0*16+3]
##print("operand is ",(1*16+0)*2**16+(1*16+0)*256+(0*16+3))
##my_machine.my_ALU.execute_instruction(instruction_word)
##instruction_word = [3,1*16+0,12*16+3,0*16+3]
##print("operand is ",(1*16+0)*2**16+(1*16+0)*256+(0*16+3))
##my_machine.my_ALU.execute_instruction(instruction_word)
##print("Expected value of A",6,7,9)
##print("Actual value of A",my_machine.my_registers.A[0],my_machine.my_registers.A[1],\
##      my_machine.my_registers.A[2])
##print

# NOTE: STCH, STL, STSW, and STX not tested as their code is essentially identical to that of STA

# NOTE: SUB not tested as it is essentially identical to ADD




