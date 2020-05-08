import unittest
from routes_list import route_set_2, route_set_3, route_set_4, route_set_5, route_set_6
from route import route
from point import point
from traverse_util import traverse

class Traverse_util(unittest.TestCase):

    def test_traverse_paths_in_points_one_level(self):
        pygame = None
        screen = None

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

        active_path = point1.get_active_path()

        # active route is now the second route added
        next_active_path = point1.switch_path()
        self.assertEquals('route3', next_active_path[0].get_route_name())
        print('associated point for route3 ', next_active_path[2].point)

    def test_traverse_paths_in_points_two_levels(self):
        pygame = None
        screen = None

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

        # active route is now the second route added
        next_active_path = point1.switch_path()
        self.assertEquals('route3', next_active_path[0].get_route_name())
        print('associated point for route3 ', next_active_path[2].point)

        # point 2 was associated with one of the routes in the path of point 1
        trav = traverse()
        traversed_routes = trav.traverse_journey(point1, [])
        self.assertIsNotNone(traversed_routes)

        self.assertEquals('route3', traversed_routes[0].get_route_name())
        self.assertEquals('route3', traversed_routes[1].get_route_name())
        self.assertEquals('route3', traversed_routes[2].get_route_name())
        self.assertEquals('route4', traversed_routes[3].get_route_name())
        self.assertEquals('route4', traversed_routes[4].get_route_name())
        self.assertEquals('route6', traversed_routes[5].get_route_name())
        self.assertEquals('route6', traversed_routes[6].get_route_name())
        self.assertEquals('route6', traversed_routes[7].get_route_name())


if __name__ == '__main__':
    unittest.main()