import pygame
import pygame.math as math
import math as mathpy
from enum import Enum
from routes_list import route_set_1, route_set_2, route_set_3, route_set_4, route_set_5, route_set_6
from point import point
from signal import signal, aspect
from route import route
from traverse_util import traverse

pygame.init()
screen = pygame.display.set_mode((1000, 480))
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
screen.blit(background, (0, 0))

class train(object):

    def __init__(self, headcode, journey):
        self.x = None
        self.y = None
        self.headcode = headcode
        self.journey = journey
        self.allow_move = False
        self.next_position = 0
        self.yx = 0
        self.yd = 0
        self.init_journey()

    def set_move_status(self, status):
        self.allow_move = status

    def draw(self):
        self.move()
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y, -40, -10))

    def move(self):
        distance = mathpy.sqrt((self.yx * self.yx) + (self.yd * self.yd))
        speed = 10 
        if distance > 1:
            if self.x <= self.journey.routes()[self.next_position].get_start_route_coord()[0]:
                speed_x = speed * (self.yx / distance)
                self.x -= speed_x

            scale = 1
            if (self.y != self.journey.routes()[self.next_position].get_start_route_coord()[1]): # this used to be self.y !=
                scale = scale * -1
                speed_y = speed * (self.yd / distance) * scale
                self.y += speed_y
                self.y = round(self.y, -1) # this rounds to nearest 10 pixels.

    def init_journey(self):
        for x in self.journey.routes():
            x.set_headcode(None)
        self.journey.routes()[0].set_headcode(self.headcode) # train always starts at the first route
        self.x = self.journey.routes()[0].get_start_route_coord()[0]
        self.y = self.journey.routes()[0].get_start_route_coord()[1]
        print(self.x, self.y, 'ooh ok')

    def update_journey(self, journey): # this will always cause a restart at the beginning. Not what we want
        self.journey = journey
        self.init_journey()

    def show_journey(self):
        return self.journey

    def get_current_route(self):
        for i, n in enumerate(self.journey.routes()):
            if n.get_headcode() == self.headcode:
                print('inside ', i)
                return n

    def step(self, screen): # to next route in journey.
        print('moving')
        current_position = None
        for route in self.journey.routes():
            if route.get_headcode() == self.headcode:
                current_position = self.journey.routes().index(route)
                break
        print('current position number: ', current_position)
        try:
            if current_position is not None:
                self.journey.routes()[current_position].set_headcode(None) #['headcode'] = None
                self.journey.routes()[current_position+1].set_headcode(self.headcode) #['headcode'] = self.headcode # move headcode to next position
               
                # but in order to use new position above, this is your difference to get there
                self.yd = self.journey.routes()[current_position].get_start_route_coord()[1] - self.journey.routes()[current_position].get_end_route_coord()[1] 
                self.yx = self.journey.routes()[current_position].get_start_route_coord()[0] - self.journey.routes()[current_position].get_end_route_coord()[0]

                # and lets lock in the new position globally so draw() can have a target
                self.next_position = current_position+1
 
        except IndexError:
            print('end of the road')

class journey(object):

    valid_order_routes = [] # remove this
    ordered_routes = []
    
    def __init__(self):
        pass

    def add_route(self, routex): # not using this anymore. move to routes or points

        if (self.valid_order_routes.__contains__(routex)):
            print('already exists')

        if self.valid_order_routes:
            print('last value in list is', self.valid_order_routes[-1])
            last_route = self.valid_order_routes[-1]

            if routex['start_xy'] != last_route['end_xy']:
                print('cant add it wont add it')
            else:
                self.valid_order_routes.append(routex)
                self.ordered_routes.append(route(pygame, screen, routex['routeName'], routex['start_xy'], routex['end_xy']))
        else:
            self.valid_order_routes.append(routex)
            self.ordered_routes.append(route(pygame, screen, routex['routeName'], routex['start_xy'], routex['end_xy']))
    
    def set_routes(self, routes): # hacky,
        self.ordered_routes = routes

    def routes(self):
        return self.ordered_routes

    # no need to draw a journey anymore
    # def draw(self):
    #     for route in self.ordered_routes: # draw route lines
    #         route.draw()

def redrawGameWindow():

    screen.blit(background, (0, 0))
    # journey.draw()

    train.draw()

    for p in points:
        p.draw(pygame, screen)

    if train.allow_move:
        if train.get_current_route().signal.colour != aspect.RED:
            train.step(screen)
        train.set_move_status(False)

    pygame.display.update()
            
journey = journey()

path_f = []
path_f.append(route(pygame, screen, route_set_6.route0['routeName'], route_set_6.route0['start_xy'], route_set_6.route0['end_xy']))
path_f.append(route(pygame, screen, route_set_6.route1['routeName'], route_set_6.route1['start_xy'], route_set_6.route1['end_xy']))
path_f.append(route(pygame, screen, route_set_6.route2['routeName'], route_set_6.route2['start_xy'], route_set_6.route2['end_xy']))

point3 = point()
point3.add_paths(path_f)

path_c = []
path_c.append(route(pygame, screen, route_set_4.route0['routeName'], route_set_4.route0['start_xy'], route_set_4.route0['end_xy']))
path_c.append(route(pygame, screen, route_set_4.route1['routeName'], route_set_4.route1['start_xy'], route_set_4.route1['end_xy'], point3))
path_c.append(route(pygame, screen, route_set_4.route2['routeName'], route_set_4.route2['start_xy'], route_set_4.route2['end_xy']))
path_d = []
path_d.append(route(pygame, screen, route_set_5.route0['routeName'], route_set_5.route0['start_xy'], route_set_5.route0['end_xy']))
path_d.append(route(pygame, screen, route_set_5.route1['routeName'], route_set_5.route1['start_xy'], route_set_5.route1['end_xy']))
path_d.append(route(pygame, screen, route_set_5.route2['routeName'], route_set_5.route2['start_xy'], route_set_5.route2['end_xy']))

point2 = point()
point2.add_paths(path_c)
point2.add_paths(path_d)

path_a = []
path_a.append(route(pygame, screen, route_set_2.route0['routeName'], route_set_2.route0['start_xy'], route_set_2.route0['end_xy']))
path_a.append(route(pygame, screen, route_set_2.route1['routeName'], route_set_2.route1['start_xy'], route_set_2.route1['end_xy']))
path_a.append(route(pygame, screen, route_set_2.route2['routeName'], route_set_2.route2['start_xy'], route_set_2.route2['end_xy']))
path_b = []
path_b.append(route(pygame, screen, route_set_3.route0['routeName'], route_set_3.route0['start_xy'], route_set_3.route0['end_xy']))
path_b.append(route(pygame, screen, route_set_3.route1['routeName'], route_set_3.route1['start_xy'], route_set_3.route1['end_xy']))
path_b.append(route(pygame, screen, route_set_3.route2['routeName'], route_set_3.route2['start_xy'], route_set_3.route2['end_xy'], point2))

point1 = point()
point1.add_paths(path_a)
point1.add_paths(path_b)

points = [point1, point2, point3]

# lets add point to point
# returns all paths and routes within, based on active point position

trav = traverse()
routes = trav.traverse_journey(point1, [])
journey.set_routes(routes)
train = train('1A11', journey)

clock = pygame.time.Clock()
shootLoop = 0
run = True
while run:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            # check signal for route
            for route in journey.routes():
                if(route.signal.bulb_space.collidepoint(pos)):
                    route.signal.iterate_aspect()

            for p in points:
                if(p.point_space.collidepoint(pos)):
                    print('hit me')
                    p.switch_path()

                    # once switched, if train is behind point, update its route ahead - calculate it again
                    # routes = trav.traverse_journey(p, [])
                    routes = trav.traverse_journey(point1, [])
                    journey.set_routes(routes)
                    train.update_journey(journey)


    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        print('lets move the train')
        train.set_move_status(True)

    redrawGameWindow()

pygame.quit()