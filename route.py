from signal import signal, aspect

class route(object):

    def __init__(self, pygame, screen, routeName, start_xy, end_xy):
        self.routeName = routeName
        self.start_xy = start_xy
        self.end_xy = end_xy
        self.headcode = None
        self.signal = signal(pygame, screen, aspect.RED, self.start_xy[0], self.start_xy[1])
        self.pygame = pygame
        self.screen = screen

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

    def get_signal(self):
        return self.signal()

    def draw(self):
        start = self.start_xy
        end = self.end_xy
        self.pygame.draw.aalines(self.screen, (0, 0, 0), False, [start, end])
        self.signal.draw()