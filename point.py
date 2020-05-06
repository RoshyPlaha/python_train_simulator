import abstract_point
class point(abstract_point.abstract_point):

    route_paths = []

    def __init__(self, point=None):
        self.point = point
        self.active_position = 0
        self.route_paths = []

    def add_paths(self, p):
        if len(self.route_paths) <= 2: # max paths for a point
            self.route_paths.append(p)
        else:
            print('maximum routes added to a point')
            return -1

    def get_active_path(self):
        for i, p in enumerate(self.route_paths):
            if i == self.active_position:
                return p

    def switch_path(self):
        self.active_position +=1
        if self.active_position > len(self.route_paths)-1:
            self.active_position = 0
        for i, p in enumerate(self.route_paths):
            if i == self.active_position:
                return p
    
    def draw(self, pygame, screen):
        for path in self.route_paths:
            for route in path:
                route.draw()
        
        self.draw_active_position(pygame, screen)
        self.draw_point_controller(pygame, screen)
        
    def draw_active_position(self, pygame, screen):
        active_start_xy = self.route_paths[self.active_position][0].get_start_route_coord()
        active_end_xy = self.route_paths[self.active_position][0].get_end_route_coord()
        y_start = active_start_xy[1]-2
        y_end = active_end_xy[1]-2
        pygame.draw.lines(screen, (0, 102, 204), False, [(active_start_xy[0], y_start), (active_end_xy[0], y_end)], 3)
    
    def draw_point_controller(self, pygame, screen):

        # draw triangle below point
        triangle_top_point_coord_x = self.route_paths[0][0].get_start_route_coord()[0]
        triangle_top_point_coord_y = self.route_paths[0][0].get_start_route_coord()[1]+10

        edge_distance = 5
        triangle_left_point_coord_xy = (triangle_top_point_coord_x-edge_distance, triangle_top_point_coord_y+edge_distance)
        triangle_right_point_coord_xy = (triangle_top_point_coord_x+edge_distance, triangle_top_point_coord_y+edge_distance)
        self.point_space = pygame.draw.polygon(screen, (0, 102, 204), [(triangle_top_point_coord_x, triangle_top_point_coord_y), triangle_left_point_coord_xy, triangle_right_point_coord_xy], 2)        
