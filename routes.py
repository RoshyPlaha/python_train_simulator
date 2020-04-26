class train():

    def __init__(self, x, y, headcode):
        self.x = x,
        self.y = y
        self.headcode = headcode
        self.journey = None

    def add_journey(self, journey):
        self.journey = journey
        for x in self.journey.routes():
            x['headcode'] = None

    def show_journey(self):
        return self.journey

    def start(self): # train always starts at the first route
        self.journey.routes()[0]['headcode'] = self.headcode
            
    def move(self): # to next route in journey. shouldnt be in this class
        position = None
        for route in self.journey.routes():
            i = 0
            print('routes here ', route)
            if route['headcode'] == self.headcode:
                position = self.journey.routes().index(route)
                break
        
        if position is not None and self.journey.routes()[position+1]:
            self.journey.routes()[position]['headcode'] = None
            self.journey.routes()[position+1]['headcode'] = self.headcode

class journey(): # a journey has routes

    valid_order_routes = []
    def __init__(self):
        pass

    def add_route(self, route):

        if (self.valid_order_routes.__contains__(route)):
            print('already exists bitch')

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

    

journey = journey()
print(journey.routes()) # empty

route1 = (
            {'routeName': 'aaa',
            'start_xy': (10, 10),
            'end_xy': (10, 20)
            }
        )

route2 = (
    {
            'routeName': 'bbb',
            'start_xy': (10, 20),
            'end_xy': (40, 400)
    }
        )


route3 = (
    {
            'routeName': 'bbb',
            'start_xy': (10, 20),
            'end_xy': (40, 400)
    }
        )

journey.add_route(route1)
journey.add_route(route2)
journey.add_route(route3)
print(journey.routes())

a1 = train(1,2, '1A11')

a1.add_journey(journey)
a1.start()
print('bb ', a1.show_journey().routes())
a1.move()