from abc import ABC, abstractmethod
class abstract_point(ABC):

    point = None

    # @abstractmethod
    # def add_next_point_x():
    #     return self.point

    def add_next_point(self, point):
        self.point = point

    def get_next_point(self):
        return self.point

    def traverse_active_paths(self):
        pass
