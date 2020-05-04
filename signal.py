from enum import Enum

class signal(object): # A signal is at the start of a route

    def __init__(self, pygame, screen, colour, x, y):
        self.colour = colour
        self.x = x
        self.y = y
        self.create_signal_coords()
        self.click = 0
        self.aspect = [aspect.RED, aspect.YELLOW, aspect.GREEN]
        self.pygame = pygame
        self.screen = screen

    def create_signal_coords(self):
        self.bulb_position = (self.x-10, self.y-22)
        self.stalk = [(self.x, self.y), (self.x, self.y-22), (self.x - 8, self.y-22)]

    def iterate_aspect(self):
        self.click +=1

        if self.click >= 3:
            self.click = 0

        for i,x in enumerate(self.aspect):
            if i == self.click:
                self.colour = x

    def draw(self):
        border_radius = 5
        colour_radius = border_radius - 2
        self.pygame.draw.aalines(self.screen, (0, 0, 0), False, self.stalk)
        self.bulb_space = self.pygame.draw.circle(self.screen, (0, 0, 0), self.bulb_position, border_radius)
        
        if (self.colour.name == 'YELLOW'):
            self.pygame.draw.circle(self.screen, self.colour.value, (self.x-10,self.y-22), colour_radius)
        elif (self.colour.name == 'GREEN'):
            self.pygame.draw.circle(self.screen, self.colour.value, (self.x-10,self.y-22), colour_radius)
        else:
            self.pygame.draw.circle(self.screen, self.colour.value, (self.x-10,self.y-22), colour_radius)

class aspect(Enum):
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 128, 0)
