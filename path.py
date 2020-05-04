from point import point

class pathNode(object): # instally mypy to do class checking

    nextPathNode = None

    def __init__(self, point):
        self.point = point
        self.active_path = self.point.get_active_path()

    def add_new_path(self, nextPathNode):
        self.nextPathNode = nextPathNode

    def switch_path(self):
        self.active_path = self.point.switch_path()





    