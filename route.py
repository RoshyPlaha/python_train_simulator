from abstract_route import abstract_route
from signal import signal, aspect

class route(abstract_route):

    def __init__(self, pygame, screen, routeName, start_xy, end_xy, associate_point=None):
        self.routeName = routeName
        self.start_xy = start_xy
        self.end_xy = end_xy
        self.headcode = None
        self.pygame = pygame
        self.screen = screen

        if (associate_point is not None):
            print('well gosh, im normally None')
            self.add_next_point(associate_point)

        self.signal = signal(pygame, screen, aspect.RED, self.end_xy[0], self.end_xy[1])

    def get_route_coord(self):
        print ('Returning Route: ', self.start_xy, self.end_xy)
        return [self.start_xy, self.end_xy]

    def set_headcode(self, headcode):
        self.headcode = headcode

    def get_headcode(self):
        return self.headcode

    def get_start_route_coord(self):
        return self.start_xy

    def get_end_route_coord(self):
        return self.end_xy

    def get_route_name(self):
        return self.routeName

    def get_signal(self):
        return self.signal()

    def draw(self):
        start = self.start_xy
        end = self.end_xy
        self.pygame.draw.aalines(self.screen, (0, 0, 0), False, [start, end])
        self.signal.draw()