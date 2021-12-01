# class defining knob function

import sys, pygame, os

class knobs():

    def __init__(self,name,location,settings,initial_setting,screen):

        self.name = name

        working_directory = os.getcwd()
        self.screen = screen
        self.max_positions = 7
        self.settings = settings
        self.sprites = {}
        self.rects = {}
        self.current_setting = initial_setting
        self.ordered_directions = {0:'North',1:'NorthEast',2:'East',\
                                   3:'SouthEast',4:'South',5:'SouthWest',\
                                   6:'West',7:'NorthWest'}

        #initialize a group of sprites which will be colocated
        # it is not intended that any of the seperate sprites will
        # move independently
        for meaning, direction in settings.iteritems():
            self.sprites[meaning] = pygame.image.load(\
                os.path.join(working_directory,"GraphicDrawing","Knob"+direction+".png"))
            self.rects[meaning] = self.sprites[meaning].get_rect()
            self.rects[meaning].center = location
##        print("rectangle topleft  and bottomright ")
##        print(self.rects[meaning].topleft,self.rects[meaning].bottomright)

        return

    def process_click(self,mx,my,sounds):
        # figure out where the knob is, where the mouse click occurred
        # and rotate the knob in the correct direction

        #figure out the direction of the current knob setting
        if self.settings[self.current_setting] == 'North':
            (tempx,tempy) = self.rects[self.current_setting].midtop
        elif self.settings[self.current_setting] == 'NorthEast':
            (tempx,tempy) = self.rects[self.current_setting].topright
        elif self.settings[self.current_setting] == 'East':
            (tempx,tempy) = self.rects[self.current_setting].midright
        elif self.settings[self.current_setting] == 'SouthEast':
            (tempx,tempy) = self.rects[self.current_setting].bottomright
        elif self.settings[self.current_setting] == 'South':
            (tempx,tempy) = self.rects[self.current_setting].midbottom
        elif self.settings[self.current_setting] == 'SouthWest':
            (tempx,tempy) = self.rects[self.current_setting].bottomleft
        elif self.settings[self.current_setting] == 'West':
            (tempx,tempy) = self.rects[self.current_setting].midleft
        elif self.settings[self.current_setting] == 'NorthWest':
            (tempx,tempy) = self.rects[self.current_setting].topleft
        else:
            raise internal_error_in_process_click


        (centx,centy) = self.rects[self.current_setting].center

        delta_x = tempx - centx
        delta_y = tempy - centy

        delta_mx = mx - centx
        delta_my = my - centy

        #figure out if we are on the right hand side of the knob or the
        # left hand side
        if delta_mx*delta_y - delta_my*delta_x < 0:
            # we are on the right hand side of the knob
            right_hand_side = True
        elif delta_mx*delta_y - delta_my*delta_x > 0:
            # we are on the left hand side
            right_hand_side = False
        else:
            return

        # loop through all possible directions for a knob
        for key in self.ordered_directions.keys():
            temp_key = key
            if self.settings[self.current_setting] == self.ordered_directions[key]:
                # we found the current setting, find the next appropriate setting
                if right_hand_side:
                    found_next = False
                    while not found_next:
                        #rotate the knob to the right
                        if temp_key < self.max_positions:
                            temp_key = temp_key + 1
                        else:
                            temp_key = 0
                        for temp_setting in self.settings.keys():
                            temp_direction = self.settings[temp_setting]
                            if temp_direction == self.ordered_directions[temp_key]:
##                                sounds[temp_key].play()
                                found_next = True
                    break # out of looping over the directions
                else:
                    found_next = False
                    while not found_next:
                        # we are rotating knob to the left
                        if temp_key == 0:
                            temp_key = self.max_positions
                        else:
                            temp_key = temp_key - 1
                        for temp_setting in self.settings.keys():
                            temp_direction = self.settings[temp_setting]
                            if temp_direction == self.ordered_directions[temp_key]:
##                                sounds[temp_key].play()
                                found_next = True
                    break # out of looping over the directions
                                
        current_direction = self.ordered_directions[temp_key]

        # now update current setting
        
        for key in self.settings.keys():
            if current_direction == self.settings[key]:
                self.current_setting = key
                break
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

    def blit_dongle(self,screen):
        screen.blit(self.sprites[self.current_setting],\
                    self.rects[self.current_setting])
        return

    def change_setting(self,new_setting):
        self.current_setting = new_setting
        return

    def my_move(self,speed):
        # move all of the sprites associated with the knob together to a new location

        for meaning, direction in self.settings.iteritems():
            self.rects[meaning] = self.rects[meaning].move(speed)

        return

    def my_left(self):
        # return the left of the colocated rectangles

        for meaning, direction in self.settings.iteritems():
            return self.rects[meaning].left

    def my_right(self):
        # return the right of the colocated rectangles

        for meaning, direction in self.settings.iteritems():
            return self.rects[meaning].right

    def my_top(self):
        # return the top of the colocated rectangles

        for meaning, direction in self.settings.iteritems():
            return self.rects[meaning].top

    def my_bottom(self):
        # return the bottom of the colocated rectangles

        for meaning, direction in self.settings.iteritems():
            return self.rects[meaning].bottom

