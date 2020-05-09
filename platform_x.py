class platform_x(object):

    def __init__(self, pygame, screen, colour, x, y):
        self.colour = colour
        self.x = x
        self.y = y
        self.height = 20
        self.width = 50
        self.pygame = pygame
        self.screen = screen

    def draw(self):

        self.pygame.draw.rect(self.screen, (0, 0, 0), [self.x, self.y, self.width, self.height], 2)
