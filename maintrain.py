import pygame
import pygame.math as math
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
        self.init_journey()
        self.allow_move = False
        self.position = 0 # this is its next position

    def set_move_status(self, status):
        self.allow_move = status

    def draw(self):
        self.move()
        pygame.draw.rect(screen, (0,0,0), (self.x, self.y - 2, 40, -10))

    def move(self):
        if self.x != self.journey.routes()[self.position]['start_xy'][0]:
            if self.x < self.journey.routes()[self.position]['start_xy'][0]:
                self.x += 10
        
        if self.y != self.journey.routes()[self.position]['start_xy'][1]:
            if self.y < self.journey.routes()[self.position]['start_xy'][1]:
                self.y += 10
            if self.y > self.journey.routes()[self.position]['start_xy'][1]:
                self.y -= 10

    def init_journey(self):
        for x in self.journey.routes():
            x['headcode'] = None
        self.journey.routes()[0]['headcode'] = self.headcode # train always starts at the first route
        self.x = self.journey.routes()[0]['start_xy'][0]
        self.y = self.journey.routes()[0]['start_xy'][1]
        print(self.x, self.y, 'ooh ok')

    def show_journey(self):
        return self.journey

    def step(self, screen): # to next route in journey.
        print('moving')
        current_position = None
        for route in self.journey.routes():
            if route['headcode'] == self.headcode:
                current_position = self.journey.routes().index(route)
                break
        print('current position number: ', current_position)
        self.position = current_position+1
        print('new position number: ', self.position)
        try:
            if current_position is not None:
                self.journey.routes()[current_position]['headcode'] = None
                self.journey.routes()[self.position]['headcode'] = self.headcode

                print('Should now start at: x ', self.journey.routes()[self.position]['start_xy'][0])
                print('Should now start at: y ', self.journey.routes()[self.position]['start_xy'][1])

        except IndexError:
            print('end of the road')
        

class journey(object):

    valid_order_routes = []
    
    def __init__(self):
        pass

    def add_route(self, route):

        if (self.valid_order_routes.__contains__(route)):
            print('already exists')

        if self.valid_order_routes:
            print('last value in list is', self.valid_order_routes[-1])
            last_route = self.valid_order_routes[-1]

            if route['start_xy'] != last_route['end_xy']:
                print('cant add it wont add it')
            else:
                self.valid_order_routes.append(route)
        else:
            self.valid_order_routes.append(route)
    
    def routes(self):
        return self.valid_order_routes

    def draw(self):
        for route in self.valid_order_routes:
            start = route['start_xy']
            end = route['end_xy']
            pygame.draw.aalines(screen, (255, 0, 0), False, [start, end])

def redrawGameWindow():

    last = pygame.time.get_ticks()
    cooldown = 10
    # man.draw(win)    
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