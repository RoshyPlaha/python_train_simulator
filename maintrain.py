import pygame
import pygame.math as math
import math as mathpy
from enum import Enum
from journeys import journey1
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
            if (self.y != self.journey.routes()[self.next_position].get_start_route_coord()[1]):
                scale = scale * -1
                speed_y = speed * (self.yd / distance) * scale
                self.y += speed_y
                self.y = round(self.y, 0)

    def init_journey(self):
        for x in self.journey.routes():
            x.set_headcode(None)
        self.journey.routes()[0].set_headcode(self.headcode) # train always starts at the first route
        self.x = self.journey.routes()[0].get_start_route_coord()[0]
        self.y = self.journey.routes()[0].get_start_route_coord()[1]
        print(self.x, self.y, 'ooh ok')

    def show_journey(self):
        return self.journey

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

class route(object):

    def __init__(self, routeName, start_xy, end_xy):
        self.routeName = routeName
        self.start_xy = start_xy
        self.end_xy = end_xy
        self.headcode = None
        self.signal = signal(aspect.RED, self.start_xy[0], self.start_xy[1])

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
        pygame.draw.aalines(screen, (0, 0, 0), False, [start, end])
        self.signal.draw()

class aspect(Enum):
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 128, 0)

class signal(object): # A signal is at the start of a route

    def __init__(self, colour, x, y):
        self.colour = colour
        self.x = x
        self.y = y
        self.create_signal_coords()

    def create_signal_coords(self):
        self.bulb_position = (self.x-10, self.y-22)
        self.stalk = [(self.x, self.y), (self.x, self.y-22), (self.x - 8, self.y-22)]

    def draw(self):
        border_radius = 5
        colour_radius = border_radius - 2
        pygame.draw.aalines(screen, (0, 0, 0), False, self.stalk)
        self.bulb_space = pygame.draw.circle(screen, (0, 0, 0), self.bulb_position, border_radius)
        
        if (self.colour.name == 'YELLOW'):
            pygame.draw.circle(screen, self.colour.value, (self.x-10,self.y-22), colour_radius)
        elif (self.colour.name == 'GREEN'):
            pygame.draw.circle(screen, self.colour.value, (self.x-10,self.y-22), colour_radius)
        else:
            pygame.draw.circle(screen, self.colour.value, (self.x-10,self.y-22), colour_radius)
        
class journey(object):

    valid_order_routes = []
    ordered_routes = []
    
    def __init__(self):
        pass

    def add_route(self, routex):

        if (self.valid_order_routes.__contains__(routex)):
            print('already exists')

        if self.valid_order_routes:
            print('last value in list is', self.valid_order_routes[-1])
            last_route = self.valid_order_routes[-1]

            if routex['start_xy'] != last_route['end_xy']:
                print('cant add it wont add it')
            else:
                self.valid_order_routes.append(routex)
                self.ordered_routes.append(route(routex['routeName'], routex['start_xy'], routex['end_xy']))
        else:
            self.valid_order_routes.append(routex)
            self.ordered_routes.append(route(routex['routeName'], routex['start_xy'], routex['end_xy']))
    
    def routes(self):
        return self.ordered_routes

    def draw(self):
        for route in self.ordered_routes: # draw route lines
            route.draw()

def redrawGameWindow():

    last = pygame.time.get_ticks()
    cooldown = 10
    screen.blit(background, (0, 0))
    journey.draw()

    train.draw()

    if train.allow_move:
        train.step(screen)
        train.set_move_status(False)

    pygame.display.update()


journey = journey()
journey.add_route(journey1.route0)
journey.add_route(journey1.route1)
journey.add_route(journey1.route2)
journey.add_route(journey1.route3)
journey.add_route(journey1.route4)
journey.add_route(journey1.route5)
journey.add_route(journey1.route6)
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
            for route in journey.routes():
                if(route.signal.bulb_space.collidepoint(pos)):
                    print('fire')
                    route.signal.colour = aspect.GREEN


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