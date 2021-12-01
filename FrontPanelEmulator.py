import sys,pygame,os

from control_bank import *
from system_knobs import *
from display_register import *
from display_opcode_operand import *
from Machine import *
from my_exception_definitions import *

def simulate():
    
    working_directory = os.getcwd()
    pygame.init()

    # initialize the sounds stuff
    pygame.mixer.pre_init(44100,-16,2, 1024)
    pygame.init()
    pygame.mixer.set_num_channels(12)
    sounds=[]
    for item in range(12):
        source=os.path.join(working_directory,"Sounds","soundsquare"+str(item+1)+'.wav')
        sounds.append(pygame.mixer.Sound(source))

    # initialize the screen   
    size = width, height = 1024, 768
    black = 0, 0, 0
    screen = pygame.display.set_mode(size)

    FrontPanel = pygame.image.load(os.path.join(working_directory,"GraphicDrawing","FrontPanel.png"))
    panelrect = FrontPanel.get_rect()

    screen.fill(black)
    screen.blit(FrontPanel, panelrect)
    pygame.display.set_caption("Front Panel")
    pygame.display.flip()

    # initialize the machine and controls
    my_machine = Machine('SIC-XE Computer')

    #initialize the display objects
    the_display_register = display_register((40,188),screen,my_machine,sounds)
    the_control_bank = control_bank(screen,my_machine)
    the_knobs = system_knobs(screen,my_machine)
    the_display_opcode_operand = display_opcode_operand((40,420),screen,my_machine)

    panel_control_list = [the_knobs,the_control_bank,\
                          the_display_opcode_operand,\
                          the_display_register]

    while True:
        
        my_machine.my_clock.clock_ticks += 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                return                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                (mx,my) = pygame.mouse.get_pos()
                
                for dongle in panel_control_list:
                    if dongle.click_on_me(mx,my):
                        try:
                            dongle.process_click(mx,my,sounds)
                        except stop_the_machine as e:
                            my_machine.my_ALU.runnning = False
                        except new_register_knob_setting as e:
                            the_display_register.connect_to_register(e.value)
                        except load_register_activated as e:
                            temp_value = the_display_register.return_value()
                            target_register_string = the_knobs.my_knobs['register'].current_setting
                            my_machine.my_registers.set_register_value(target_register_string,\
                                                                       temp_value)
                            the_display_register.connected = True
                        except execute_instruction_activated as e:
                            temp_result = the_display_opcode_operand.return_value()
                            my_machine.my_ALU.execute_instruction(temp_result)
                            # zero out the array
                            the_display_opcode_operand.display_value(bytearray(b'\x00\x00\x00'))
                        except step_activated as e:
                            my_machine.my_ALU.step()
                        except halt_machine as e:
                            my_machine.my_ALU.running = False
                        except run_machine as e:
                            my_machine.my_ALU.running = True
                            

        # update the various states with a clock tick
        my_machine.my_ALU.received_clock_tic()
        the_display_register.received_clock_tic()
        the_display_opcode_operand.received_clock_tic()

        screen.fill(black)
        screen.blit(FrontPanel, panelrect)

        for dongle in panel_control_list:
            dongle.blit_dongle(screen)
        
        pygame.display.flip()
        
    return


simulate()
print("Thanks for playing.")
