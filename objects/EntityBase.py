import config
import pygame


class EntityBase(pygame.sprite.Sprite):

    FRAME_WIDTH = 0
    FRAME_HEIGHT = 0
    img_file = ""
    opacity = 255

    GRAVITY = 0.4

    #maximum velocity x,y axis
    MAX_VX = 3
    MAX_VY = 20

    #velocity x,y axis
    vx = 0
    vy = 0

    # vertical and horizontal state
    h_state = "standing"
    v_state = "resting"

    # vertical and horizontal facing
    v_facing = "up"
    h_facing = "right"

    # general state
    state = ""

    # write sth...
    frames_sizes = None
    FRAMES = []

    frame_index = 0 
    rect = None
    dead = False

    def init_image_and_position(self, index, location)
        # write sth
        pass

    def __init__(self, index, location, *groups):
        # write sth
        pass

    
    def apply_gravity(self):
        dy = self.vy
        dx = self.vx
        self.vy += self.GRAVITY
        self.rect = self.rect.move(dx, dy)


    def get_position(self)
        # write sth
        pass
    