import unittest
from point import point
from path import pathNode
from routes_list import route_set_2
class Testroute(unittest.TestCase):

    def test_one(self):
        p = point()
        list1 = [1, 2]
        list2 = [3, 4]
        p.add_paths(list1)
        p.add_paths(list2)

        p1 = pathNode(p)
        self.assertIsNotNone(p1)

    
    def test_with_routes(self):
        p = point()
        p.add_paths(route_set_2.route0)
        p.add_paths(route_set_2.route1)

        p1 = pathNode(p)
        self.assertIsNotNone(p1)

    def test_two(self):
        a = aThing()


        alist = []
        alist.append(aThing())
        self.assertIsNotNone(a)

class aThing():

    def __init__(self):
        print('cool thing')

if __name__ == '__main__':
    unittest.main()