from abc import ABC
class abstract_route(ABC):
    
    point = None

    def add_next_point(self, point):
        self.point = point
        print('point succesfully added')

    def get_next_point(self):
        return self.point

    def traverse_active_paths(self):
        pass
