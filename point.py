class point(object):

    route_paths = []

    def __init__(self, point=None):
        self.point = point
        self.position = 0
        self.route_paths = []


    def add_paths(self, p):
        if len(self.route_paths) <= 2: # max paths for a point
            self.route_paths.append(p)
        else:
            print('maximum routes added to a point')
            return -1

    def get_active_path(self):
        for i, p in enumerate(self.route_paths):
            if i == self.position:
                return p

    def switch_path(self):
        self.position +=1
        if self.position > len(self.route_paths)-1:
            self.position = 0
        for i, p in enumerate(self.route_paths):
            if i == self.position:
                return p
            else:
                print('not found brudda: ', i)
    
    def draw(self, pygame, screen):
        for path in self.route_paths:
            for route in path:
                route.draw()