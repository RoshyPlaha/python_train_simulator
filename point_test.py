import unittest
from point import point
from routes_list import route_set_2, route_set_3, route_set_4, route_set_5
from route import route

class Testpoint(unittest.TestCase):

    def test_with_two_paths(self):
        p = point()

        list1 = [1, 2]
        list2 = [3, 4]
        p.add_paths(list1)
        p.add_paths(list2)

        selected_list = p.switch_path()
        self.assertEqual(list2, selected_list)

        selected_list = p.switch_path()
        self.assertEqual(list1, selected_list)

    def test_with_exceed_max_paths(self):
        p = point()

        list1 = [1, 2]
        list2 = [3, 4]
        list3 = [5, 6]
        max_path = [7,8]
        p.add_paths(list1)
        p.add_paths(list2)
        p.add_paths(list3)
        self.assertEqual(p.add_paths(max_path), -1)

    def test_with_three_paths(self):
        p = point()

        list1 = [1, 2]
        list2 = [3, 4]
        list3 = [5, 6]
        p.add_paths(list1)
        p.add_paths(list2)
        p.add_paths(list3)

        selected_list = p.switch_path()
        self.assertEqual(list2, selected_list)

        selected_list = p.switch_path()
        self.assertEqual(list3, selected_list)

        selected_list = p.switch_path()
        self.assertEqual(list1, selected_list)

    def test_with_one_path(self):
        p = point()

        list1 = [1, 2]
        p.add_paths(list1)

        selected_list = p.switch_path()
        self.assertEqual(list1, selected_list)

    def test_with_no_path(self):
        p = point()

        selected_list = p.switch_path()
        self.assertEqual(None, selected_list)

    def test_switch_paths(self):
        path_a = []
        pygame = None
        screen = None
        path_a.append(route(pygame, screen, route_set_2.route0['routeName'], route_set_2.route0['start_xy'], route_set_2.route0['end_xy']))
        path_a.append(route(pygame, screen, route_set_2.route1['routeName'], route_set_2.route1['start_xy'], route_set_2.route1['end_xy']))
        path_a.append(route(pygame, screen, route_set_2.route2['routeName'], route_set_2.route2['start_xy'], route_set_2.route2['end_xy']))

        path_b = []
        path_b.append(route(pygame, screen, route_set_3.route0['routeName'], route_set_3.route0['start_xy'], route_set_3.route0['end_xy']))
        path_b.append(route(pygame, screen, route_set_3.route1['routeName'], route_set_3.route1['start_xy'], route_set_3.route1['end_xy']))
        path_b.append(route(pygame, screen, route_set_3.route2['routeName'], route_set_3.route2['start_xy'], route_set_3.route2['end_xy']))

        point1 = point()
        point1.add_paths(path_a)
        point1.add_paths(path_b)

        active_path = point1.get_active_path()
        # active route is the first route added
        self.assertEquals('route2', active_path[0].get_route_name())

        # active route is now the second route added
        next_active_path = point1.switch_path()
        self.assertEquals('route3', next_active_path[0].get_route_name())

if __name__ == '__main__':
    unittest.main()