# class defining switches

import sys, pygame, os

class switches():

    def __init__(self,name,location,screen):

        self.name = name
        self.screen = screen
        self.sprites = {}
        self.rects = {}

        working_directory = os.getcwd()
        self.switch_positions = ['Up', 'Middle','Lower']
        self.current_setting = 'Up'

        #initialize a group of sprites which will be colocated
        # it is not intended that any of the seperate sprites will
        # move independently
        for position in self.switch_positions:
            self.sprites[position] = pygame.image.load(\
                os.path.join(working_directory,"GraphicDrawing","Toggle"+position+"Small.png"))
            
            self.rects[position] = self.sprites[position].get_rect()
            self.rects[position].center = location

        return

    def my_move(self,speed):
        # move all of the sprites associated with the switch together
        #  to a new location

        for setting in self.switch_positions:
            self.rects[setting] = self.rects[setting].move(speed)

        return

    def change_setting(self,new_setting):
        self.current_setting = new_setting
        return

    def process_click(self,mx,my,sounds):
        # process clicking on a switch
        self.change_setting('Up')
        self.blit_dongle(self.screen)
        pygame.display.flip()
        self.change_setting('Middle')
        self.blit_dongle(self.screen)
        pygame.display.flip()
        self.change_setting('Lower')
        sounds[0].play()
        self.blit_dongle(self.screen)
        pygame.display.flip()
        self.change_setting('Middle')
        self.blit_dongle(self.screen)
        pygame.display.flip()
        self.change_setting('Up')
        self.blit_dongle(self.screen)
        pygame.display.flip()
        return

    def blit_dongle(self,screen):
        screen.blit(self.sprites[self.current_setting],\
                    self.rects[self.current_setting])
        return

    def click_on_me(self,mx,my):
        for meaning in self.rects.keys():
            if mx >= self.rects[meaning].topleft[0] and \
               mx <= self.rects[meaning].bottomright[0] and \
               my >= self.rects[meaning].topleft[1] and \
               my <= self.rects[meaning].bottomright[1]:
                return True
            else:
                return False

    def my_left(self):
        # return the left of the colocated rectangles
            return self.rects[self.current_setting].left

    def my_right(self):
        # return the right of the colocated rectangles
            return self.rects[self.current_setting].right

    def my_top(self):
        # return the top of the colocated rectangles
            return self.rects[self.current_setting].top

    def my_bottom(self):
        # return the bottom of the colocated rectangles
            return self.rects[self.current_setting].bottom
