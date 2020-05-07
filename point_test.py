import unittest
from point import point
from routes_list import route_set_2, route_set_3, route_set_4, route_set_5
from route import route

class Testpoint(unittest.TestCase):

    def test_with_two_paths(self):
        head = point()
        p = point(head)

        list1 = [1, 2]
        list2 = [3, 4]
        p.add_paths(list1)
        p.add_paths(list2)

        selected_list = p.switch_path()
        self.assertEqual(list2, selected_list)

        selected_list = p.switch_path()
        self.assertEqual(list1, selected_list)

    def test_with_exceed_max_paths(self):
        head = point()
        p = point(head)

        list1 = [1, 2]
        list2 = [3, 4]
        list3 = [5, 6]
        max_path = [7,8]
        p.add_paths(list1)
        p.add_paths(list2)
        p.add_paths(list3)
        self.assertEqual(p.add_paths(max_path), -1)

    def test_with_three_paths(self):
        head = point()
        p = point(head)

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
        head = point()
        p = point(head)

        list1 = [1, 2]
        p.add_paths(list1)

        selected_list = p.switch_path()
        self.assertEqual(list1, selected_list)

    def test_with_no_path(self):
        head = point()
        p = point(head)

        selected_list = p.switch_path()
        self.assertEqual(None, selected_list)

    def test_traverse_paths_in_points(self):
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

        path_c = []
        path_c.append(route(pygame, screen, route_set_4.route0['routeName'], route_set_4.route0['start_xy'], route_set_4.route0['end_xy']))
        path_c.append(route(pygame, screen, route_set_4.route1['routeName'], route_set_4.route1['start_xy'], route_set_4.route1['end_xy']))
        path_c.append(route(pygame, screen, route_set_4.route2['routeName'], route_set_4.route2['start_xy'], route_set_4.route2['end_xy']))

        path_d = []
        path_d.append(route(pygame, screen, route_set_5.route0['routeName'], route_set_5.route0['start_xy'], route_set_5.route0['end_xy']))
        path_d.append(route(pygame, screen, route_set_5.route1['routeName'], route_set_5.route1['start_xy'], route_set_5.route1['end_xy']))
        path_d.append(route(pygame, screen, route_set_5.route2['routeName'], route_set_5.route2['start_xy'], route_set_5.route2['end_xy']))

        point2 = point()
        point2.add_paths(path_c)
        point2.add_paths(path_d)

        # lets add point to point
        point1.add_next_point(point2)
        point1.traverse_active_paths() # returns all paths and routes within, based on active point position


        self.assertIsNotNone(point1)
        self.assertIsNotNone(point2)


if __name__ == '__main__':
    unittest.main()